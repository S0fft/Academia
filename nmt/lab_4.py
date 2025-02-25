import matplotlib.pyplot as plt
import numpy as np
from minisom import MiniSom
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

wine = load_wine()
X = wine.data
y = wine.target

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

som_size = (10, 10)
som = MiniSom(som_size[0], som_size[1], X_train.shape[1], sigma=1.0, learning_rate=0.5)

som.random_weights_init(X_train)
som.train_random(X_train, 1000, verbose=True)

plt.figure(figsize=(8, 8))

for i, x in enumerate(X_train):
    winner = som.winner(x)
    plt.text(winner[0] + 0.5, winner[1] + 0.5, str(y_train[i]),
             color=plt.cm.tab10(y_train[i]), fontdict={'weight': 'bold', 'size': 12})

plt.xlim([0, som_size[0]])
plt.ylim([0, som_size[1]])
plt.title("Карта Кохонена для Wine")
plt.grid()
plt.show()
