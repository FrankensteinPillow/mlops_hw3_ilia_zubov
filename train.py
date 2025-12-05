from pathlib import Path
from pickle import dump

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris.data
y = iris.target

print(f"Тип данных X: {type(X)}")
print(f"Размерность X: {X.shape}")
print(f"Классы ирисов: {iris.target_names}")
print("-" * 30)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Точность (Accuracy): {accuracy:.2f}\n")

print("Отчет о классификации:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = model.predict(new_sample)
print(f"Предсказание для new_sample: {iris.target_names[prediction][0]}")

model_path = Path("model.pkl")
with open(model_path, "wb") as f:
    dump(model, f)

print(f"Модель сохранена в файл: {model_path}")
