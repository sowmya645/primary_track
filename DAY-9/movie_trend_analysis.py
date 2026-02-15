import numpy as np
import pandas as pd
# data={
#     "movie":["dhurandar","bazigarr","kabhi kushi kabhi gum","devadas"],
#     "genre":["action","drama","action","romcom"],
#     "rating":[4.4,5,6,3]
    
# }
# df=pd.DataFrame(data)
# print(df)
# print("avg rating",df["rating"].mean())
# top_movies=df[df["rating"]>=4.5]
# print(top_movies)
# df["need_improv"]=df["rating"]<3.5
# print(df)
data={
    "transaction_id":[1,2,3,4],
    "type":["deposit","withdraw","deposit","withdraw"],
    "amount":[1000,300,1500,2000]
}
df=pd.DataFrame(data)
transaction_deposit=df[df["type"]=="deposit"]
print(df)
print(transaction_deposit)
transaction_withdraw=df[df["type"]=="withdraw"]
print(transaction_withdraw)
balance=0
for index, row in df.iterrows():
    if row["type"]=="deposit":
        balance=balance+row["amount"]
    else:
        balance=balance-row["amount"]
print("balance")
print(balance)
highest_row = df.loc[df["amount"].idxmax()]
print("highest value transaction")
print(highest_row)