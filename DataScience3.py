import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

sns.pairplot(df, hue="sex", palette="mako")
plt.show()