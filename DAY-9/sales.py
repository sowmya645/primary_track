import pandas as pd
df=pd.read_csv("sales.csv")
df["total_sales"]=df["price"]*df["quantity"]
print(df)
print("best selling product")
print(df.loc[df["total_sales"].idxmax()])
df["price_with_tax"]=df["price"]*1.10
print(df)