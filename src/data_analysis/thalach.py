import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../../data/raw/heart.csv')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 10))

sns.histplot(data=df, x='thalach', hue='target', kde=True, palette='coolwarm', bins=30)
plt.title('Thalach Distribution by Heart Disease (Target)', fontsize=14)
plt.xlabel('Maximum Heart Rate', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

plt.show()
