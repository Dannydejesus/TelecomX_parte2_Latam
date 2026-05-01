# Análisis de Datos: TelecomX_Data.json

## 1. Resumen General
- **Total Filas:** 7267
- **Total Columnas (después de aplanar):** 21
- **Valores Duplicados:** 0

## 2. Columnas, Tipos de Datos y Nulos
`	ext
                 DataType  Nulls  Unique
customerID            str      0    7267
Churn                 str      0       3
gender                str      0       2
SeniorCitizen       int64      0       2
Partner               str      0       2
Dependents            str      0       2
tenure              int64      0      73
PhoneService          str      0       2
MultipleLines         str      0       3
InternetService       str      0       3
OnlineSecurity        str      0       3
OnlineBackup          str      0       3
DeviceProtection      str      0       3
TechSupport           str      0       3
StreamingTV           str      0       3
StreamingMovies       str      0       3
Contract              str      0       3
PaperlessBilling      str      0       2
PaymentMethod         str      0       4
Charges.Monthly   float64      0    1585
Charges.Total         str      0    6531
`

## 3. Estadísticas Descriptivas
`	ext
                   count unique               top  freq       mean        std    min     25%   50%     75%     max
customerID          7267   7267        0002-ORFBO     1        NaN        NaN    NaN     NaN   NaN     NaN     NaN
Churn               7267      3                No  5174        NaN        NaN    NaN     NaN   NaN     NaN     NaN
gender              7267      2              Male  3675        NaN        NaN    NaN     NaN   NaN     NaN     NaN
SeniorCitizen     7267.0    NaN               NaN   NaN   0.162653   0.369074    0.0     0.0   0.0     0.0     1.0
Partner             7267      2                No  3749        NaN        NaN    NaN     NaN   NaN     NaN     NaN
Dependents          7267      2                No  5086        NaN        NaN    NaN     NaN   NaN     NaN     NaN
tenure            7267.0    NaN               NaN   NaN  32.346498  24.571773    0.0     9.0  29.0    55.0    72.0
PhoneService        7267      2               Yes  6560        NaN        NaN    NaN     NaN   NaN     NaN     NaN
MultipleLines       7267      3                No  3495        NaN        NaN    NaN     NaN   NaN     NaN     NaN
InternetService     7267      3       Fiber optic  3198        NaN        NaN    NaN     NaN   NaN     NaN     NaN
OnlineSecurity      7267      3                No  3608        NaN        NaN    NaN     NaN   NaN     NaN     NaN
OnlineBackup        7267      3                No  3182        NaN        NaN    NaN     NaN   NaN     NaN     NaN
DeviceProtection    7267      3                No  3195        NaN        NaN    NaN     NaN   NaN     NaN     NaN
TechSupport         7267      3                No  3582        NaN        NaN    NaN     NaN   NaN     NaN     NaN
StreamingTV         7267      3                No  2896        NaN        NaN    NaN     NaN   NaN     NaN     NaN
StreamingMovies     7267      3                No  2870        NaN        NaN    NaN     NaN   NaN     NaN     NaN
Contract            7267      3    Month-to-month  4005        NaN        NaN    NaN     NaN   NaN     NaN     NaN
PaperlessBilling    7267      2               Yes  4311        NaN        NaN    NaN     NaN   NaN     NaN     NaN
PaymentMethod       7267      4  Electronic check  2445        NaN        NaN    NaN     NaN   NaN     NaN     NaN
Charges.Monthly   7267.0    NaN               NaN   NaN  64.720098  30.129572  18.25  35.425  70.3  89.875  118.75
Charges.Total       7267   6531                      11        NaN        NaN    NaN     NaN   NaN     NaN     NaN
`

## 4. Detección de Outliers (Método IQR)
- **SeniorCitizen:** 1182 outliers detectados
- **tenure:** 0 outliers detectados
- **Charges.Monthly:** 0 outliers detectados
