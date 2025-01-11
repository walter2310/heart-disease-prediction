import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../../data/raw/heart.csv')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 10))

# Histograma para la distribución de colesterol por target
plt.subplot(2, 2, 1)
sns.histplot(data=df, x='chol', hue='target', kde=True, palette='coolwarm', bins=30)
plt.title('Cholesterol Distribution by Heart Disease (Target)', fontsize=14)
plt.xlabel('Cholesterol Level', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Histograma para la distribución de edad por target
plt.subplot(2, 2, 2)
sns.histplot(data=df, x='age', hue='target', kde=True, palette='coolwarm', bins=20)
plt.title('Age Distribution by Heart Disease (Target)', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Histograma para la distribución de la presión arterial en reposo por target
plt.subplot(2, 2, 3)
sns.histplot(data=df, x='trestbps', hue='target', kde=True, palette='coolwarm', bins=30)
plt.title('Resting Blood Pressure Distribution by Heart Disease (Target)', fontsize=14)
plt.xlabel('Resting Blood Pressure (mm Hg)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Histograma para la distribución de oldpeak por target
plt.subplot(2, 2, 4)
sns.histplot(data=df, x='thalach', hue='target', kde=True, palette='coolwarm', bins=30)
plt.title('Oldpeak Distribution by Heart Disease (Target)', fontsize=14)
plt.xlabel('Oldpeak (ST Depression)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.tight_layout()
plt.show()
