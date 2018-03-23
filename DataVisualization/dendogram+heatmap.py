
import seaborn as sns 

sns.clustermap(df.corr(), method="average" ,center=0, cmap="Blues",
               linewidths=.75, figsize=(13, 13), standard_scale=0)
