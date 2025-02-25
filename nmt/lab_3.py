import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from tensorflow import keras

wine = load_wine()
X = wine.data
y = wine.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

encoder = OneHotEncoder(sparse_output=False)
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

k = 10
kmeans = KMeans(n_clusters=k, random_state=42).fit(X_train)
centers = kmeans.cluster_centers_


def rbf(x, centers, sigma=1.0):
    return np.exp(-np.linalg.norm(x - centers, axis=1)**2 / (2 * sigma**2))


X_train_rbf = np.array([rbf(x, centers) for x in X_train])
X_test_rbf = np.array([rbf(x, centers) for x in X_test])

model = keras.Sequential([
    keras.layers.Dense(y_train.shape[1], activation='softmax', input_shape=(k,))
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train_rbf, y_train, epochs=100, batch_size=8, validation_data=(X_test_rbf, y_test))

loss, accuracy = model.evaluate(X_test_rbf, y_test)
print(f'Тестова точність: {accuracy:.4f}')

plt.plot(history.history['accuracy'], label='Навчання')
plt.plot(history.history['val_accuracy'], label='Валідація')
plt.title('Точність RBF-мережі для Wine dataset')
plt.xlabel('Епоха')
plt.ylabel('Точність')
plt.legend()
plt.show()
