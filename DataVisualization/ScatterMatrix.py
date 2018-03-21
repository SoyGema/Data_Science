import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.csv')
plt.figure()

scattermatrix = pd.scatter_matrix(dataset, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()


# In seaborn
import seaborn as sns 
sns.set(style="ticks")
sns.pairplot(dataset, hue="data")

# Or 
fig, ax = plt.subplots(figsize=(15,12))

corr = dataset.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values, ax=ax)
