
# pip install plotly

# https://www.kaggle.com/code/anandhuh/7-basic-plotly-charts-for-beginners/notebook

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Leer los datos de la aerolínea en un DataFrame de pandas
# url = './../4018.csv'
# data = pd.read_csv(url)
# import pandas as pd
# import os

# Sunburst
# https://datos.gob.es/es/catalogo/ea0010587-ocupados-por-situacion-profesional-sexo-y-sector-economico-por-comunidad-autonoma-epa-identificador-api-4018
# 4018.csv
# Tabla de INEbase Ocupados por situación profesional, sexo y sector económico, por comunidad autónoma. Trimestral. Comunidades y Ciudades Autónomas. Encuesta de Población Activa (EPA)

# Ruta al archivo CSV
archivo_csv = os.path.join('datasets', '4018.csv')

# Cargar datos desde el archivo CSV
df = pd.read_csv(archivo_csv, sep=';')

# Cambiamos los valores .. por NA
df['Total'] = df['Total'].replace('..', pd.NA)

# Eliminar filas con valores NaN en la columna 'Total'
df = df.dropna(subset=['Total'])

# Convertir la columna 'Total' a tipo numérico
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

# Eliminamos los totales de todas las columnas a visualizar
df_filtrado = df[(df['Comunidades y Ciudades Autónomas'] != 'Total') & (df['Sector económico'] != 'Total') & (df['Situación profesional'] != 'Total')]
# df_filtrado = df[df['Sector económico'] != 'Total']
# df_filtrado = df[df['Situación profesional'] != 'Total']

# Crear el gráfico sunburst
fig = px.sunburst(
    df_filtrado,
    # path=['Comunidades y Ciudades Autónomas', 'Situación profesional', 'Sector económico'],
    path=['Comunidades y Ciudades Autónomas', 'Sector económico', 'Situación profesional'],
    # path=['Sector económico', 'Situación profesional'],
    values='Total',
    title='Sunburst por Comunidades y Ciudades Autónomas, Sector económico y Situación profesional (2008T4)'
)

# Mostrar el gráfico
fig.show()