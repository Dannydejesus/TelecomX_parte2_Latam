# 🛠️ Guía de Instalación y Configuración

Esta guía detalla los pasos necesarios para configurar el entorno de desarrollo y ejecución del proyecto **TelecomX**.

## 📋 Requisitos Previos
*   **Python**: Versión 3.9 o superior.
*   **Conda**: Recomendado para la gestión de entornos (Miniconda o Anaconda).

## ⚙️ Configuración del Entorno

### 1. Clonar el repositorio
Si aún no tienes el código localmente:
```bash
git clone <url-del-repositorio>
cd TelecomX
```

### 2. Crear entorno virtual con Conda
Recomendamos usar el archivo de configuración para asegurar que todas las librerías (pandas, scikit-learn, streamlit, etc.) tengan las versiones correctas.

```bash
conda create -n TelecomX python=3.9
conda activate TelecomX
```

### 3. Instalar dependencias
Desde la raíz del proyecto, ejecuta:
```bash
pip install -r ml_project/requirements.txt
```

## 📦 Dependencias Clave
El proyecto utiliza una "lista blanca" de librerías para asegurar estabilidad en producción:
*   **Procesamiento**: `pandas`, `numpy`
*   **Machine Learning**: `scikit-learn` (Random Forest, StandardScaler)
*   **Visualización**: `matplotlib`, `seaborn`
*   **Despliegue**: `streamlit`, `joblib`

## ✅ Verificación
Para confirmar que todo está listo, intenta cargar el modelo desde una terminal de Python:
```python
import joblib
model = joblib.load('ml_project/models/churn_model_rf_optimized.joblib')
print("Modelo cargado con éxito")
```
