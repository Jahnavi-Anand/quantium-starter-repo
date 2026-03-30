import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)

df["product"] = df["product"].astype(str).str.strip().str.lower()
df = df[df["product"] == "pink morsel"].copy()

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]].dropna().sort_values("date")

df.to_csv("formatted_output.csv", index=False, date_format="%Y-%m-%d")

print("formatted_output.csv created successfully!")
