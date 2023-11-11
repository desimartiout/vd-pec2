
# pip install plotly

import plotly.graph_objects as go

# Datos de ejemplo
labels = ["Nivel 1", "A", "B", "C", "D", "E", "F"]
parents = ["", "Nivel 1", "Nivel 1", "Nivel 1", "A", "B", "B"]
values = [10, 40, 30, 20, 15, 25, 35]

# Crear el gráfico Sunburst
fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
))

# Personalizar el diseño
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

# Mostrar el gráfico
fig.show()
