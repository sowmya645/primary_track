import pandas as pd
df=pd.read_csv("s.csv")
d=pd.DataFrame(df)
print(d)
print(d.isnull())
d["marks"] = pd.to_numeric(d["marks"], errors="coerce")

d.fillna("marks":d["marks"].mean()},inplace=True)
print(d)