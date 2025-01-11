import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/raw/heart.csv')

numerical_columns = ['chol', 'trestbps', 'thalach', 'oldpeak', 'target']

# Calcular la correlación de Pearson
correlation_matrix = df[numerical_columns].corr(method='pearson')

print("Correlaciones:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
