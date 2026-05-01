import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuracion de pagina
st.set_page_config(page_title="TelecomX - Churn Dashboard", layout="wide", page_icon="📡")

# Estilo corporativo
st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CARGA DE DATOS Y MODELOS ---
# Quitamos el cache momentaneamente para asegurar que lee los datos nuevos
def load_assets():
    try:
        current_file = os.path.abspath(__file__)
    except NameError:
        current_file = os.path.abspath('ml_project/app/streamlit_app.py')
        
    base_dir = os.path.dirname(os.path.dirname(current_file))
    model_path = os.path.join(base_dir, 'models', 'churn_model_rf_optimized.joblib')
    scaler_path = os.path.join(base_dir, 'models', 'scaler.joblib')
    data_path = os.path.join(base_dir, 'data', 'processed', 'clientes_en_riesgo_2025.csv')
    
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        df_risk = pd.read_csv(data_path)
        # Limpiar nombres de columnas (quitar espacios y normalizar)
        df_risk.columns = df_risk.columns.str.strip()
        return model, scaler, df_risk
    except Exception as e:
        return None, None, None

model, scaler, df_risk = load_assets()

if df_risk is not None and not df_risk.empty:
    
    # Mapeo de seguridad si los nombres vienen con prefijos
    col_map = {
        'account_Contract': 'Contract',
        'account_Charges_Monthly': 'MonthlyCharges'
    }
    for old_col, new_col in col_map.items():
        if old_col in df_risk.columns and new_col not in df_risk.columns:
            df_risk = df_risk.rename(columns={old_col: new_col})

    # --- SIDEBAR: FILTROS ---
    st.sidebar.header("🛠️ Filtros de Analisis")
    
    # Filtro de Contrato
    if 'Contract' in df_risk.columns:
        all_contracts = sorted(df_risk['Contract'].unique().tolist())
        selected_contracts = st.sidebar.multiselect("Tipo de Contrato", all_contracts, default=all_contracts)
    else:
        st.sidebar.error("❌ Error: Columna 'Contract' no encontrada en el CSV.")
        st.sidebar.write("Columnas detectadas:", list(df_risk.columns))
        selected_contracts = []

    # Filtro de Probabilidad
    score_range = st.sidebar.slider("Score de Probabilidad (%)", 0, 100, (30, 100))
    min_score, max_score = score_range[0] / 100, score_range[1] / 100
    
    # Filtro de Cargos Mensuales
    if 'MonthlyCharges' in df_risk.columns:
        min_charge_val = float(df_risk['MonthlyCharges'].min())
        max_charge_val = float(df_risk['MonthlyCharges'].max())
        charge_range = st.sidebar.slider("Rango de Cargos Mensuales (USD)", 
                                         min_charge_val, max_charge_val, 
                                         (min_charge_val, max_charge_val))
    else:
        charge_range = (0, 1000)

    # Aplicar Filtros
    mask = (df_risk['Churn_Probability'] >= min_score) & (df_risk['Churn_Probability'] <= max_score)
    if selected_contracts:
        mask = mask & (df_risk['Contract'].isin(selected_contracts))
    if 'MonthlyCharges' in df_risk.columns:
        mask = mask & (df_risk['MonthlyCharges'] >= charge_range[0]) & (df_risk['MonthlyCharges'] <= charge_range[1])
    
    df_filtered = df_risk[mask]

    # --- CUERPO PRINCIPAL ---
    st.title("📡 TelecomX: Dashboard de Retencion")
    st.markdown("Analisis proactivo de clientes en riesgo de abandono.")

    # KPIs
    kpi1, kpi2, kpi3 = st.columns(3)
    total_base = 7043
    risk_count = len(df_filtered)
    avg_score = df_filtered['Churn_Probability'].mean() if not df_filtered.empty else 0

    with kpi1:
        st.metric("Clientes Filtrados", f"{risk_count:,}")
    with kpi2:
        st.metric("% en Riesgo", f"{(risk_count/total_base)*100:.1f}%")
    with kpi3:
        st.metric("Score Promedio", f"{avg_score:.2%}")

    st.divider()

    # GRAFICOS
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📊 Distribucion de Scores")
        if not df_filtered.empty:
            fig_hist, ax_hist = plt.subplots(figsize=(10, 6))
            sns.histplot(df_filtered['Churn_Probability'], bins=20, kde=True, color='#3498db', ax=ax_hist)
            ax_hist.set_xlabel("Probabilidad")
            st.pyplot(fig_hist)
        else:
            st.info("Sin datos para filtrar.")

    with col_right:
        st.subheader("📄 Riesgo por Contrato")
        if not df_filtered.empty and 'Contract' in df_filtered.columns:
            contract_dist = df_filtered['Contract'].value_counts()
            fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
            sns.barplot(x=contract_dist.index, y=contract_dist.values, palette='viridis', ax=ax_bar)
            st.pyplot(fig_bar)
        else:
            st.info("Selecciona al menos un contrato en el filtro lateral.")

    # TOP 10 CLIENTES
    st.subheader("🔝 Top 10 Clientes con Mayor Riesgo")
    if not df_filtered.empty:
        top_10 = df_filtered.sort_values(by='Churn_Probability', ascending=False).head(10)
        display_cols = ['customerID', 'Churn_Probability']
        if 'Contract' in top_10.columns: display_cols.append('Contract')
        if 'MonthlyCharges' in top_10.columns: display_cols.append('MonthlyCharges')
        
        st.table(top_10[display_cols].style.format({
            'Churn_Probability': '{:.2%}', 
            'MonthlyCharges': '${:.2f}'
        } if 'MonthlyCharges' in top_10.columns else {'Churn_Probability': '{:.2%}'}))

    # TABLA COMPLETA
    st.subheader("📋 Detalle de Clientes")
    st.dataframe(df_filtered.style.format({
        'Churn_Probability': '{:.2%}', 
        'MonthlyCharges': '${:.2f}'
    } if 'MonthlyCharges' in df_filtered.columns else {'Churn_Probability': '{:.2%}'}), use_container_width=True)

    # BOTON DE EXPORTACION
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar CSV", data=csv, file_name='riesgo_churn.csv', mime='text/csv')

else:
    st.title("📡 TelecomX: Dashboard de Retencion")
    st.warning("⚠️ No se pudo cargar el archivo de datos.")
    st.info("Asegurate de que el archivo `ml_project/data/processed/clientes_en_riesgo_2025.csv` existe y tiene datos.")
