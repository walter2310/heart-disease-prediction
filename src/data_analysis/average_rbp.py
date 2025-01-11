import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/raw/heart.csv')

# Agrupar los datos por edad y calcular estadísticas de presión arterial en reposo
rbp_relation = df.groupby('age')['trestbps'].agg(['mean', 'min', 'max', 'std', 'count'])

rbp_relation.rename(columns={
        'mean': 'Average Resting BP',
        'min': 'Minimum Resting BP',
        'max': 'Maximum Resting BP',
        'count': 'Number of results'
    }, inplace=True)

plt.figure(figsize=(10, 6))

# Graficar las estadísticas de presión arterial en reposo
plt.plot(rbp_relation.index, rbp_relation['Average Resting BP'], label='Average Resting BP', color='blue', marker='o')

plt.title('Resting Blood Pressure Statistics by Age', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Blood Pressure (mm Hg)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
