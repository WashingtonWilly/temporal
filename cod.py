import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos del archivo CSV
file_path = 'features.csv'
features = pd.read_csv(file_path)

# Task 1: scatter plot
plt.figure()
plt.scatter(features['AspectRatio'], features['Duration'])
plt.xlabel('AspectRatio')
plt.ylabel('Duration')
plt.title('Scatter plot of AspectRatio vs Duration')
plt.ylim(0, 2)  # Ajustar el eje y
plt.yticks(range(0, 5, 1))  # Ajustar las etiquetas del eje y con un paso de 0.5
plt.savefig('scatter_plot.png')  # Guardar la gráfica como PNG
plt.close()  # Cerrar la gráfica

# Task 2: gscatter (grouped scatter plot)
plt.figure()
sns.scatterplot(x='AspectRatio', y='Duration', hue='Character', data=features, palette='Set1')
plt.xlabel('AspectRatio')
plt.ylabel('Duration')
plt.title('Grouped scatter plot of AspectRatio vs Duration')
plt.ylim(0, 2)  # Ajustar el eje y
plt.yticks(range(0, 5, 1))  # Ajustar las etiquetas del eje y con un paso de 0.5
plt.legend(title='Character')
plt.savefig('grouped_scatter_plot.png')  # Guardar la gráfica como PNG
plt.close()  # Cerrar la gráfica

