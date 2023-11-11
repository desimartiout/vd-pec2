# pip install plotly

import plotly.graph_objects as go
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

# Crear el gráfico de horizonte con plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y1, fill='tozeroy', name='Seno'))
fig.add_trace(go.Scatter(x=x, y=y2, fill='tozeroy', name='Coseno'))
fig.add_trace(go.Scatter(x=x, y=y3, fill='tozeroy', name='Seno + Coseno'))

# Personalizar el diseño
fig.update_layout(
    title='Gráfico de Horizonte',
    xaxis_title='Tiempo',
    yaxis_title='Valor',
)

# Mostrar el gráfico
fig.show()
