import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Cargar datos del archivo CSV
features = pd.read_csv('features.csv')
testdata = pd.read_csv('testdata.csv')

# Task 1: Entrenar el modelo KNN
X_train = features.drop(columns=['Character'])
y_train = features['Character']

knnmodel = KNeighborsClassifier(n_neighbors=5)  # Puedes ajustar el número de vecinos
knnmodel.fit(X_train, y_train)

# Task 2: Predecir con el modelo KNN
X_test = testdata.drop(columns=['Character'])  # Si la columna 'Character' no está en testdata, omite este paso
predictions = knnmodel.predict(X_test)

# Si quieres guardar las predicciones en un archivo CSV
testdata['Predictions'] = predictions
testdata.to_csv('predictions.csv', index=False)

print("Predictions saved to predictions.csv")

