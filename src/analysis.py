import pandas as pd

# 1. Cargar el dataset
print("--- 1. EXPLORACIÓN INICIAL ---")
df = pd.read_csv('data/dataset_clinico_simulado_200.csv', sep=';', encoding='latin1', quoting=3)# Limpieza rápida por si los datos tienen comillas extra
df.columns = [c.strip('"') for c in df.columns]
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip('"')

print(f"Número de pacientes (registros): {df.shape[0]}")
print(f"Número de variables (columnas): {df.shape[1]}")
print("\nTipos de datos:\n", df.dtypes)
print("\nValores faltantes por columna:\n", df.isnull().sum())

# 2. Crear nueva variable: Grupo de Edad
# Joven (<30), Adulto (30-59), Adulto Mayor (60+)
def clasificar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 60:
        return 'Adulto'
    else:
        return 'Adulto Mayor'

df['Grupo_Edad'] = df['edad'].apply(clasificar_edad)

print("\n--- 2. NUEVA VARIABLE CREADA ---")
print(df[['edad', 'Grupo_Edad']].head())