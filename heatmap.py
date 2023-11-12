# pip install matplotlib seaborn

# Crime Data from 2020 to Present - City of Los Angeles
# This dataset reflects incidents of crime in the City of Los Angeles dating back to 2020. This data is transcribed from original crime reports that are typed on paper and therefore there
# https://catalog.data.gov/dataset/crime-data-from-2020-to-present
# https://catalog.data.gov/dataset/crime-data-from-2020-to-present/resource/5eb6507e-fa82-4595-a604-023f8a326099
# https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD

# reducido el dataset a 399000 registros por la limitación de Github a no soportar ficheros de más de 100MB

# import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import plotly.express as px
import plotly.graph_objects as go


# Crear datos de ejemplo
# data = np.random.rand(10, 10)

# COLUMNAS = ['AREA NAME', 'Crm Cd Desc']
COLUMNAS = ['AREA NAME', 'Vict Sex']

# Ruta al archivo CSV
archivo_csv = os.path.join('datasets', 'Crime_Data_from_2020_to_Present_reducido.csv')

# Cargar datos desde el archivo CSV
df = pd.read_csv(archivo_csv, sep=',')

print(df.head())
print(df.describe())
print(df.shape)
print(df.columns)

# Renombra la columna si es necesario
# df = df.rename(columns={'área': 'area', 'tipo_de_asalto': 'tipo_asalto'})

# Porcentajes de Asalto por Tipo en Cada Área
df = df[COLUMNAS]

# probabilidad_asalto = df.groupby(['AREA NAME', 'Crm Cd Desc']).size() / df.groupby('AREA NAME').size()
# probabilidad_asalto = probabilidad_asalto.unstack().fillna(0)

# plt.figure(figsize=(10, 8))
# # sns.heatmap(probabilidad_asalto, cmap='YlGnBu', annot=True, fmt=".2%", cbar_kws={'label': 'Probabilidad de Asalto'})
# sns.heatmap(probabilidad_asalto, cmap='YlGnBu', annot=False, cbar_kws={'label': 'Probabilidad de Asalto'})

# plt.title('Porcentajes de Asalto por Tipo en Cada Área - Los Ángeles')
# plt.show()

# Porcentajes de Asalto por Sexo y Área
probabilidad_asalto = df.groupby(['AREA NAME', 'Vict Sex']).size() / df.groupby('AREA NAME').size()
probabilidad_asalto = probabilidad_asalto.unstack().fillna(0)

plt.figure(figsize=(10, 8))
sns.heatmap(probabilidad_asalto, cmap='YlGnBu', annot=False, cbar_kws={'label': 'Probabilidad de Asalto'})

plt.title('Porcentajes de Asalto por Sexo y Área - Los Ángeles')
plt.show()


# heatmap = sns.heatmap(probabilidad_asalto, cmap='YlGnBu', annot=False, cbar_kws={'label': 'Probabilidad de Asalto'})

# # Añade etiquetas al eje X con los códigos del tipo de asalto
# tipos_asalto = df['Crm Cd Desc'].unique()
# heatmap.set_xticks(range(len(tipos_asalto)))
# heatmap.set_xticklabels(tipos_asalto, rotation=45, ha='right')

# # Añade la leyenda
# cbar = plt.colorbar(heatmap)
# cbar.set_label('Probabilidad de Asalto')

# plt.title('Probabilidad de Asalto por Tipo en Cada Área')
# plt.show()

# heatmap = sns.heatmap(probabilidad_asalto, cmap='YlGnBu', annot=False, cbar_kws={'label': 'Probabilidad de Asalto'})

# # Añade etiquetas al eje X con los códigos del tipo de asalto
# tipos_asalto = df['tipo_de_asalto'].unique()
# heatmap.set_xticks(range(len(tipos_asalto)))
# heatmap.set_xticklabels(tipos_asalto, rotation=45, ha='right')

# # Añade la leyenda
# plt.legend(title='Tipo de Asalto', loc='upper left', bbox_to_anchor=(1, 1))

# plt.title('Probabilidad de Asalto por Tipo en Cada Área')
# plt.show()


# # Crear el heatmap con Seaborn
# sns.heatmap(data, annot=True, cmap="YlGnBu", cbar=True)

# # Añadir etiquetas y título
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.title("Heatmap de Datos")

# # Mostrar el gráfico
# plt.show()
