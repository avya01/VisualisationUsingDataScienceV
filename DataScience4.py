import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("USA_Housing (1).csv")

sns.pairplot(df)
plt.show()