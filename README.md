# 📡 TelecomX: Churn Prediction Project

Este proyecto implementa un pipeline completo de Machine Learning para la prediccion y retencion de clientes en una empresa de telecomunicaciones.

## 🚀 Estructura del Proyecto
- `app/`: Aplicacion Streamlit y scripts de inferencia.
- `data/`: Datos crudos y procesados.
- `models/`: Modelos entrenados y escaladores.
- `notebooks/`: Desarrollo y experimentacion.
- `docs/`: Reportes ejecutivos y documentacion tecnica.

## 🛠️ Instalacion
1. Asegurate de tener Python 3.9+ instalado.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Ejecucion de la Aplicacion
Para lanzar el dashboard interactivo de Streamlit, ejecuta el siguiente comando desde la raiz del proyecto:

```bash
streamlit run ml_project/app/streamlit_app.py
```

## 🔮 Inferencia de Nuevos Datos
Para generar predicciones sobre nuevos clientes:
1. Coloca tu archivo CSV en `data/raw/ventas_2025_inferencia.csv`.
2. Ejecuta:
   ```bash
   python ml_project/app/predict.py
   ```
3. Los resultados se guardaran en `data/processed/clientes_en_riesgo_2025.csv`.

## 🤖 Detalles del Modelo
- **Algoritmo**: Random Forest Classifier (Optimizado).
- **Balanceo**: Class Weight Balanced.
- **Recall**: > 80% (Threshold 0.3).
