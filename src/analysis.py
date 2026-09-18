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




import matplotlib.pyplot as plt
import os

print("\n--- 3. ANÁLISIS Y RESPUESTAS ---")

# 1. ¿Cuál es la afección más frecuente?
afeccion_frecuente = df['afeccion'].value_counts()
print("1. Afección más frecuente:\n", afeccion_frecuente.head(1))

# 2. ¿Qué grupo de edad presenta la mayor cantidad de casos graves?
graves_por_edad = df[df['gravedad'] == 'grave']['Grupo_Edad'].value_counts()
print("\n2. Casos graves por grupo de edad:\n", graves_por_edad)

# 3. ¿Cómo cambia la gravedad de los síntomas entre hombres y mujeres?
gravedad_genero = pd.crosstab(df['genero'], df['gravedad'])
print("\n3. Gravedad por género:\n", gravedad_genero)

# 4. ¿Cuál es el promedio de edad por afección?
edad_promedio_afeccion = df.groupby('afeccion')['edad'].mean().round(1)
print("\n4. Promedio de edad por afección:\n", edad_promedio_afeccion)

print("\n--- 4. GENERANDO GRÁFICAS ---")
# Asegurarnos de que la carpeta exista
os.makedirs('outputs/resultados', exist_ok=True)

# Gráfica 1: Frecuencia de afecciones
plt.figure(figsize=(10,6))
df['afeccion'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Frecuencia de Afecciones')
plt.xlabel('Afección')
plt.ylabel('Cantidad de Pacientes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/resultados/1_afecciones.png')
plt.close()

# Gráfica 2: Gravedad por género
gravedad_genero.plot(kind='bar', figsize=(8,5), colormap='viridis')
plt.title('Nivel de Gravedad por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('outputs/resultados/2_gravedad_genero.png')
plt.close()

# Gráfica 3: Histograma de edades
plt.figure(figsize=(8,5))
df['edad'].plot(kind='hist', bins=15, color='coral', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig('outputs/resultados/3_edades.png')
plt.close()

print("¡Las 3 gráficas se han guardado exitosamente en la carpeta 'outputs/resultados'!")



