import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/raw/heart.csv')

chol_relation = df.groupby('age')['chol'].agg(['mean', 'min', 'max', 'std', 'count'])

chol_relation.rename(columns={
        'mean': 'Average Chol',
        'min': 'Minimum chol',
        'max': 'Maximum chol',
        'count': 'Number of results'
    }, inplace=True)

plt.figure(figsize=(10, 6))

# Graficar estadísticas de colesterol
plt.plot(chol_relation.index, chol_relation['Average Chol'], label='Average Chol', color='blue', marker='o')

plt.title('Cholesterol Statistics by Age', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Cholesterol Level', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()