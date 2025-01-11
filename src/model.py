import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

df = pd.read_csv('../data/raw/heart.csv')

X, y = df.drop('target', axis=1), df['target']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
forest = RandomForestClassifier(random_state=9)
forest.fit(x_train, y_train)

# Predicciones
y_preds = forest.predict(x_test)

print('Model Score:', forest.score(x_test, y_test))

cm = confusion_matrix(y_test, y_preds)

accuracy = accuracy_score(y_test, y_preds)
precision = precision_score(y_test, y_preds)
recall = recall_score(y_test, y_preds)
f1 = f1_score(y_test, y_preds)

# Mostrar métricas
print(f"Accuracy: {accuracy:.3f} ({accuracy * 100:.1f}%)")
print(f"Precision: {precision:.3f} ({precision * 100:.1f}%)")
print(f"Recall: {recall:.3f} ({recall * 100:.1f}%)")
print(f"F1 Score: {f1:.3f} ({f1 * 100:.1f}%)")

# Visualizar la matriz de confusión
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=forest.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title('Matriz de Confusión')
plt.show()
