
# pip install plotly

# https://www.kaggle.com/code/anandhuh/7-basic-plotly-charts-for-beginners/notebook

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Leer los datos de la aerolínea en un DataFrame de pandas
url = 'https://bit.ly/3AVBLcJ'
data = pd.read_csv(url, encoding="ISO-8859-1", dtype={'Month': str, 'DestStateName': str,'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str})

data.head()

# Elegimos solo 500 ejemplos de datos
data = data.sample(n=500, random_state=42)
data.shape

# Eliminamos los valores vacíos
data = data.dropna(subset=['Month'])
data = data.dropna(subset=['DestStateName'])

# Crear el gráfico Sunburst
fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights')

# Mostrar el gráfico
fig.show()