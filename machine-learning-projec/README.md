# Análisis de preferencias de personas entre montañas y playas. Proyecto 2 Parte 1 (Core)

A través de este proyecto, se tiene como objetivo seleccionar un dataset para el proyecto 2 del curso de Machine Learning de Coding Dojo.

## Estructura

- `data/`: Contiene los datasets analizados
- `EDA/`: Contiene los notebook Jupyter usados para los EDAs para los 4 datasets
- `selected/`: Contiene el dataset y el notebook Jupyter del dataset seleccionado
- `README.md`: Este archivo

## Notebooks

- Notebook donde se lleva a cabo la Exploración del dataset 1: [EDA-dataset-1.ipynb](EDA/EDA-dataset-1.ipynb)
- Notebook donde se lleva a cabo la Exploración del dataset 2: [EDA-dataset-2.ipynb](EDA/EDA-dataset-2.ipynb)
- Notebook donde se lleva a cabo la Exploración del dataset 3: [EDA-dataset-3.ipynb](EDA/EDA-dataset-3.ipynb)
- Notebook donde se lleva a cabo la Exploración del dataset 4: [EDA-dataset-4.ipynb](EDA/EDA-dataset-4.ipynb)

## Resúmenes

### [EDA 1](https://www.kaggle.com/datasets/ziya07/plant-health-data)

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de regresión, ya que solamente posee columnas numéricas.
- No existen muchos outliers
- No Existen correlaciones fuertes 
- Las variables más importantes se encuentran en las columnas Moisure y Nitrogen Level

### [EDA 2](https://www.kaggle.com/datasets/stephenyulinchen/epl-2425-data/data)

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de predicción
- Existen outlliers. Por este motivo, para el escalamiento de datos, tal vez lo mejor sería usar el RobustScaler
- Existen correlaciones:

Se observan varias correlaciones

- HST - HS

- HTAG - FTAG

- HTHG - FTHG

- AS - AST

Luego también ligeras correlaciones entre

- HS - FTHG

- HST - FTHG

- FTAG - AST

- AS - FTAG

- HTHG - HST

- HTAG - AST

- HS - HC

- AS - AC

### [EDA 3](https://www.kaggle.com/datasets/willianoliveiragibin/market-sales-data/data)

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de predicción
- Existen correlaciones
- Existen valores anómalos

### [EDA 4](https://www.kaggle.com/datasets/willianoliveiragibin/top-12-german-companies)

Del EDA, se puede destacar lo siguiente

- Según los histogramas, se puede notar que varias columnas no siguen una distribución estándar, por lo que se debe tener en cuenta en el escalado
- Existe una gran cantidad de outliers en varias columnas, por lo que se debe tener en cuenta también a la hora de escalar

## Problema seleccionado

El problema seleccionado es el de predicción de resultados de la Premier League (EDA 2), Se selecciona debido a que posee varios tipos de datos y también de que se trata de un dataset interesante a analizar

### Descripción del problema

Se desea realizar predicciones del ganador en base a varias caracteristicas como: arbitro, puntaje, equipo, disparos al arco, etc.

## Instrucciones de uso

1. Clonar el repositorio: `git clone git@github.com:trucdefou/machine-learning-projec.git`
2. Instalar dependencias
3. Ir a la carpeta EDA en este proyecto y acceder a los notebooks jupyter de interés.

## Autores

Benjamín Recalde

## Licencia

MIT