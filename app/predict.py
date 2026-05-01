import pandas as pd
import numpy as np
import joblib
import os

def run_inference(input_path, output_path, model_path, scaler_path, threshold=0.3):
    """
    Carga el modelo y realiza inferencia sobre nuevos datos.
    """
    if not os.path.exists(input_path):
        print(f"Error: No se encontro el archivo de entrada en {input_path}")
        return

    # 1. Cargar modelo y escalador
    print("Cargando modelos...")
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # 2. Cargar datos
    print(f"Cargando datos desde {input_path}...")
    df_new = pd.read_csv(input_path)
    customer_ids = df_new['customerID']
    
    # 3. Preprocesamiento (Consistente con el entrenamiento)
    # A. Limpieza de TotalCharges
    df_new['account_Charges_Total'] = pd.to_numeric(df_new['account_Charges_Total'], errors='coerce').fillna(0)
    
    # B. Mapeo de variables binarias
    mappings = {
        'Yes': 1, 'No': 0,
        'True': 1, 'False': 0,
        'Male': 1, 'Female': 0,
        True: 1, False: 0
    }
    
    binary_cols = ['customer_gender', 'customer_Partner', 'customer_Dependents', 
                   'phone_PhoneService', 'account_PaperlessBilling']
    
    for col in binary_cols:
        if col in df_new.columns:
            df_new[col] = df_new[col].map(mappings)

    # C. One-Hot Encoding
    multiclass_cols = ['phone_MultipleLines', 'internet_InternetService', 'internet_OnlineSecurity', 
                       'internet_OnlineBackup', 'internet_DeviceProtection', 'internet_TechSupport', 
                       'internet_StreamingTV', 'internet_StreamingMovies', 'account_Contract', 
                       'account_PaymentMethod']
    
    df_encoded = pd.get_dummies(df_new, columns=multiclass_cols, drop_first=True, dtype=int)
    
    # D. Alinear columnas con el modelo original
    expected_cols = scaler.feature_names_in_
    
    for col in expected_cols:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
            
    X = df_encoded[expected_cols]

    # E. Escalado
    X_scaled = scaler.transform(X)

    # 4. Prediccion con Threshold
    print(f"Realizando predicciones (Threshold = {threshold})...")
    probs = model.predict_proba(X_scaled)[:, 1]
    preds = (probs >= threshold).astype(int)

    # 5. Exportar Resultados
    results = pd.DataFrame({
        'customerID': customer_ids,
        'Churn_Probability': probs,
        'Risk_Prediction': preds
    })
    
    # Filtrar solo clientes en riesgo
    at_risk = results[results['Risk_Prediction'] == 1]
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    at_risk.to_csv(output_path, index=False)
    
    print(f"Proceso completado. Clientes en riesgo exportados a: {output_path}")
    print(f"Clientes analizados: {len(results)}, Clientes en riesgo detectados: {len(at_risk)}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    INPUT = os.path.join(project_root, 'data', 'raw', 'ventas_2025_inferencia.csv')
    OUTPUT = os.path.join(project_root, 'data', 'processed', 'clientes_en_riesgo_2025.csv')
    MODEL = os.path.join(project_root, 'models', 'churn_model_rf_optimized.joblib')
    SCALER = os.path.join(project_root, 'models', 'scaler.joblib')

    run_inference(INPUT, OUTPUT, MODEL, SCALER, threshold=0.3)
