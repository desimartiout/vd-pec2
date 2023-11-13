# pip install plotly

# import plotly.graph_objects as go
# import numpy as np

# Portal de Datos Abiertos de la Generalitat Valenciana
# https://portaldadesobertes.gva.es/es
# COVID-19 Serie de casos con PDIA positiva en la Comunitat Valenciana, según fecha en la que el laboratorio notifica el diagnóstico
# https://dadesobertes.gva.es/es/dataset/covid-19-series-casos-pdia-positiva/resource/cb50e7d2-0c0e-46b8-a359-a0fa35998577
# https://dadesobertes.gva.es/dataset/ce195af2-39ec-4f44-bb77-b14235519b0d/resource/cb50e7d2-0c0e-46b8-a359-a0fa35998577/download/covid-19-serie-de-casos-con-pdia-positiva-en-la-comunitat-valenciana.csv

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

COLUMNAS = ['Data diagnòstic laboratori/fecha diagnóstico laboratorio', 'C.Valenciana', 'Homes/Hombres','Dones/Mujeres','Prov. Alacant/Alicante','Prov. Castelló/Castellón','Prov. València']
COL_FECHA = 0
COL_ALICANTE = 4
COL_CASTELLON = 5
COL_VALENCIA = 6

# Ruta al archivo CSV
archivo_csv = os.path.join('datasets', 'covid-19-serie-de-casos-con-pdia-positiva-en-la-comunitat-valenciana.csv')

# Cargar datos desde el archivo CSV
df = pd.read_csv(archivo_csv, sep=';')

# print(df.head())
# print(df.describe())
# print(df.shape)
# print(df.columns)

# Nos quedamos solo con las columnas que nos interesan
# df_nuevo = df[COLUMNAS]
# COL_FECHA = 0
# COL_ALICANTE = 1
# COL_CASTELLON = 2
# COL_VALENCIA = 3

# Crear el gráfico de horizonte con plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=df[COLUMNAS[0]], y=df[COLUMNAS[COL_ALICANTE]], fill='tozeroy', name='Alicante'))
fig.add_trace(go.Scatter(x=df[COLUMNAS[0]], y=df[COLUMNAS[COL_CASTELLON]], fill='tozeroy', name='Castellón'))
fig.add_trace(go.Scatter(x=df[COLUMNAS[0]], y=df[COLUMNAS[COL_VALENCIA]], fill='tozeroy', name='Valencia'))

# Personalizar el diseño
fig.update_layout(
    title='COVID-19 Serie de casos con PDIA positiva en la Comunitat Valenciana - por provincias',
    xaxis_title='Fecha',
    yaxis_title='Casos de COVID',
)

# Mostrar el gráfico
fig.show()
