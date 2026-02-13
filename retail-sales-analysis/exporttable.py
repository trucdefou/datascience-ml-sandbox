import pandas as pd

# Data for the models
data = {
    'Método': ['Regresión Lineal', 'KNN', 'Random Forests', 'LGBM'],
    'R²': [0.692116, 0.636330, 0.636330, 0.694374],
    'RMSE': [284.850434, 309.582978, 309.582978, 283.804123],
    'MSE': [81139.770000, 95841.620000, 95841.620000, 80544.780342],
    'MAE': [179.643333, 190.000000, 190.000000, 177.043178]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Export the DataFrame to Excel
df.to_excel('model_comparison.xlsx', index=False)

# Optionally, display the DataFrame to check the result
print(df)