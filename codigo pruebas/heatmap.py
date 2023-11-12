# pip install matplotlib seaborn

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = np.random.rand(10, 10)

# Crear el heatmap con Seaborn
sns.heatmap(data, annot=True, cmap="YlGnBu", cbar=True)

# Añadir etiquetas y título
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Heatmap de Datos")

# Mostrar el gráfico
plt.show()
