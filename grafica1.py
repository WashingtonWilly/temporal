import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo
data = pd.read_csv('/home/paola/Escritorio/PAOLA/DATA1.txt', delimiter='\t')

# Convertir comas a puntos decimales y luego a tipo float
data['X'] = data['X'].str.replace(',', '.').astype(float)
data['Y'] = data['Y'].str.replace(',', '.').astype(float)
data['P'] = data['P'].str.replace(',', '.').astype(float)

# Graficar X, Y y P en función del tiempo
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(data['TIME'], data['X'], label='X')
plt.xlabel('Time')
plt.ylabel('X')
plt.title('X over Time')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(data['TIME'], data['Y'], label='Y')
plt.xlabel('Time')
plt.ylabel('Y')
plt.title('Y over Time')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(data['TIME'], data['P'], label='P')
plt.xlabel('Time')
plt.ylabel('P')
plt.title('P over Time')
plt.legend()

plt.tight_layout()
plt.savefig('output_plot1.png')  # Guardar como archivo de imagen