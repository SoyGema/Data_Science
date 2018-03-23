import seaborn as sns

fig, ax = plt.subplots(figsize=(15,12))

corr = df.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values, ax=ax, annot=True, cmap="Blues")
