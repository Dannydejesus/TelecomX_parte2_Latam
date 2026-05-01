# 🚀 Guía de Uso y Ejecución

Esta guía explica cómo operar el pipeline de predicción y visualizar los resultados en el dashboard interactivo.

## 🔮 1. Ejecución de Predicciones (Inferencia)
El script `predict.py` es el motor que procesa nuevos datos de clientes y genera los scores de riesgo.

### Flujo de Datos
1.  **Entrada**: Coloca tus nuevos datos en `ml_project/data/raw/ventas_2025_inferencia.csv`.
2.  **Comando**:
    ```bash
    python ml_project/app/predict.py
    ```
3.  **Salida**: El script generará el archivo `ml_project/data/processed/clientes_en_riesgo_2025.csv` incluyendo la probabilidad de abandono y las variables de negocio para el dashboard.

## 📊 2. Visualización en el Dashboard (Streamlit)
Una vez generadas las predicciones, puedes explorar los insights de forma visual.

### Comando de Inicio
Desde la raíz del proyecto, ejecuta:
```bash
streamlit run ml_project/app/streamlit_app.py
```

### Funcionalidades del Dashboard
*   **Filtros**: Segmenta por tipo de contrato, rango de cargos mensuales y umbral de probabilidad.
*   **KPIs**: Visualiza el % total de clientes en riesgo y el score promedio de la selección.
*   **Exportación**: Puedes descargar la lista filtrada de clientes directamente desde el dashboard usando el botón **"Descargar CSV"**.

## 📝 Notas de Operación
*   **Threshold**: Por defecto, el sistema marca como "Riesgo" a cualquier cliente con un score >= **0.3**.
*   **Actualización**: El dashboard se actualiza automáticamente cada vez que ejecutas `predict.py` y refrescas la página del navegador.
