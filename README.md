# Análisis de Dataset Clínico Simulado

Explica brevemente de qué trata:
Este proyecto consiste en el análisis exploratorio y visualización de registros médicos de pacientes para descubrir patrones de salud, desarrollado para la práctica de Git, GitHub y Reproducibilidad.

## Dataset
* Nombre del dataset: dataset_clinico_simulado_200.csv
* Fuente: Datos simulados proporcionados para la práctica escolar de análisis clínico.
* Descripción breve: Conjunto de datos con 200 registros de pacientes que incluye texto clínico, edad, género, afección y gravedad.

## Objetivo
El objetivo es analizar y automatizar la limpieza de datos, crear clasificaciones por grupos de edad y descubrir patrones estadísticos entre las características de los pacientes y la gravedad de sus enfermedades.

## Requisitos
Se requiere Python y las dependencias incluidas en el archivo requirements.txt (pandas y matplotlib).

## Instalación

Explica cómo clonar el repositorio:
git clone https://github.com/issavm/proyecto-clinico.git

Entrar al proyecto:
cd proyecto-clinico

Crear el entorno:
python -m venv .venv

Activarlo e instalar dependencias (en Windows usa .\.venv\Scripts\activate):
pip install -r requirements.txt

## Ejecución
Para ejecutar el proyecto, corre este comando en la terminal:
python src/analysis.py

## Análisis realizados
* Preprocesamiento de datos y creación de la variable categórica "Grupo_Edad".
* Identificación de la afección clínica más frecuente.
* Conteo de pacientes con casos "graves", segmentados por edad.
* Tabla cruzada de gravedad de los síntomas según el género del paciente.
* Cálculo del promedio de edad por cada tipo de afección.

## Resultados y conclusiones
* Se lograron limpiar y procesar los 200 registros clínicos de manera automatizada usando Pandas.
* Se generaron 3 visualizaciones (distribución de edades, afecciones y gravedad por género) guardadas en la carpeta de resultados.
* El uso del entorno virtual y el archivo requirements.txt aseguran que el análisis es 100% reproducible en cualquier otro equipo.