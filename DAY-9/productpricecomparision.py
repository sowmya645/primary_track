import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales.csv")
d=pd.DataFrame(df)
d.plot(kind="bar",y="price",x="product")
plt.show()