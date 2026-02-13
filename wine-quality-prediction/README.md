# Wine Quality Prediction

Este proyecto utiliza diferentes modelos de machine learning para predecir la calidad del vino basada en sus características fisicoquímicas.

## Propósito del Proyecto

El objetivo principal es evaluar el rendimiento de diferentes modelos de clasificación en el conjunto de datos de calidad del vino (*Wine Quality Dataset*). Los modelos analizados son:

- **Regresión Logística**
- **K-Nearest Neighbors (KNN)**
- **Random Forest**

Cada modelo es evaluado usando métricas de desempeño como la exactitud, F1-score, matriz de confusión y errores cuadráticos.

---

## Técnicas y Herramientas Utilizadas

- **Librerías de Python:**
  - `scikit-learn`: Para la implementación y evaluación de modelos de machine learning.
  - `pandas`: Para la manipulación de datos.
  - `matplotlib` y `seaborn`: Para las visualizaciones.
  
- **Modelos Evaluados:**
  - **Regresión Logística:** Un modelo lineal para clasificación.
  - **K-Nearest Neighbors (KNN):** Algoritmo basado en distancia.
  - **Random Forest:** Modelo basado en ensamblaje de árboles de decisión.

- **Métricas:**
  - Exactitud (Accuracy)
  - F1-score
  - Matriz de confusión
  - Error Cuadrático Medio (MSE, RMSE)
  - R-cuadrado (R²)

---

## Cómo Ejecutar el Proyecto

### 1. Prerrequisitos

Asegúrate de tener instalado Python 3.8+ y las siguientes dependencias:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

2. Ejecutar el Notebook
Descarga el archivo wine-quality-prediction.ipynb.
Abre el archivo en Jupyter Notebook o Jupyter Lab:
```
bash
jupyter notebook wine-quality-prediction.ipynb
```

Ejecuta las celdas paso a paso para reproducir el análisis y las visualizaciones.


Resultados Clave
Random Forest es el modelo con mejor desempeño, obteniendo una exactitud del 90.7% y una macro promedio de F1-score de 0.90.
KNN también mostró buenos resultados con una exactitud del 89.9%.
Regresión Logística fue el modelo con el peor desempeño, con una exactitud del 57.1%.
Conjunto de Datos
Nombre: Wine Quality Dataset
Fuente: UCI Machine Learning Repository
Descripción: Contiene medidas fisicoquímicas de muestras de vino, junto con etiquetas de calidad (de 3 a 8).
Autor
Este proyecto fue desarrollado como parte de una práctica de machine learning. Para consultas o contribuciones, no dudes en abrir un issue o enviar un pull request.


