import pandas as pd

df = pd.read_csv("superMarketData.csv")


AveragePurchaseVal = df["Total"].sum()/df["Total"].count()
print("========================================================================")
print(f"Total Revenue of the business is : R {df["Total"].sum()}")
print(f"Average purchase value : R{df["Total"].mean()}")
print(f"Highest Purchase value : R{df["Total"].max()}")
print(f"Lowest Purchase Value : R{df["Total"].min()}")
print(f"Average customer Age : {df["Age"].mean()}")
print(f"Total quantity of products sold : {df["Quantity"].sum()}\n\n")
print("===========================================================================================")

print(f"Customers from Pretoria\n {df[df["City"] == "Pretoria"]}\n")
print(f"Customers older than 30\n{df[df["Age"] > 30]}\n")
print(f"Purchases greater than R300\n{df[df["Total"] > 300]}\n")
print(f"Card Payments\n{df[df["PaymentMethod"] == "Card"]}\n")
print(f"Groceries\n{df[df["Category"] == "Groceries"]}")
print(f"Electronics\n{df[df["Category"] == "Electronics"]}")



print("============================================================================================")
cityRevenue = df.groupby("City")
categoryRev = df.groupby("Category")
pMethodRev = df.groupby("PaymentMethod") 
avgGenSpenditure = df.groupby("Gender")

print(f"Revenue by city\n{cityRevenue["Total"].sum()}\n")
print(f"Revenue by Category\n{categoryRev["Total"].sum()}\n")
print(f"Revenue by Payment Method\n{pMethodRev["Total"].sum()}\n")
print(f"Average spending by gender : {avgGenSpenditure["Total"].sum()}")
print(f"Average quantity spent by Category : {categoryRev["Quantity"].mean()}")


df["VAT"] = df["Total"] * 0.15
df["Final Price"] = df["VAT"] + df["Total"]

if df["Age"] >= 18 and df["Age"] < 25:
    df["Age group"] = ["Young  adult"]

print(df[["VAT","Product","Final Price", "Age Group"]])






