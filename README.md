# 📋 Reporte Ejecutivo: Predicción de Abandono (Churn) - TelecomX

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telecomxparte2latam-4hwne3gpaqsfzhqmrqz5qp.streamlit.app/)

## 1. Resumen del Problema y Objetivo
El proyecto **TelecomX** surge de la necesidad de identificar proactivamente a los clientes con alta probabilidad de cancelar sus servicios. El objetivo principal fue desarrollar un modelo de Machine Learning capaz de clasificar a los clientes en riesgo, permitiendo al equipo de retención actuar antes de que el abandono se concrete.

## 2. Metodología Aplicada
Se siguió un pipeline robusto de ciencia de datos:
*   **Ingesta y Limpieza**: Procesamiento de datos jerárquicos (JSON), manejo de valores nulos y estandarización de tipos.
*   **Ingeniería de Características**: Conversión de variables binarias, One-Hot Encoding para variables categóricas y escalado de variables numéricas.
*   **Análisis Exploratorio (EDA)**: Identificación de patrones de comportamiento y correlaciones clave.
*   **Modelado**: Evolución desde un modelo base (Regresión Logística) hasta modelos de ensamble avanzados (**Random Forest** y **HistGradientBoosting**).
*   **Optimización**: Ajuste de hiperparámetros mediante *GridSearchCV* y calibración del umbral de decisión (*Threshold*) para maximizar la sensibilidad (Recall).

## 3. Resultados Finales
El modelo final (**Random Forest Optimizado**) alcanzó los siguientes hitos:
*   **Recall (Sensibilidad)**: **> 80%** (utilizando un umbral de 0.3), asegurando la detección de la gran mayoría de clientes en riesgo.
*   **ROC-AUC**: **0.85+**, demostrando una excelente capacidad de discriminación entre clases.
*   **Robustez**: Validado mediante validación cruzada y evaluación en un set de prueba independiente.

## 4. Top 5 Insights del Negocio
1.  **Antigüedad (Tenure)**: El riesgo de abandono es crítico en los primeros 6 meses. La fidelización temprana es clave.
2.  **Tipo de Contrato**: Los contratos "mes a mes" presentan una tasa de churn significativamente superior a los contratos anuales o bianuales.
3.  **Cargos Mensuales**: Existe un umbral de precio donde la probabilidad de abandono aumenta drásticamente; los clientes con cargos altos son más sensibles al precio.
4.  **Método de Pago**: Los clientes que utilizan "Electronic Check" muestran una mayor propensión al abandono frente a métodos automáticos.
5.  **Servicio Técnico**: La falta de soporte técnico ("No Tech Support") es un predictor fuerte de insatisfacción y churn.

## 5. Recomendaciones de Implementación
*   **Intervención Proactiva**: Desplegar alertas automáticas cuando el score del modelo supere 0.3.
*   **Estrategia de Fidelización**: Ofrecer incentivos para migrar a clientes de contratos mensuales a contratos de largo plazo.
*   **Mejora de Producto**: Revisar la calidad o el precio del servicio de fibra óptica, dado su alto índice de correlación con el churn.
*   **Monitoreo**: Re-entrenar el modelo trimestralmente para capturar cambios en las tendencias del mercado.
