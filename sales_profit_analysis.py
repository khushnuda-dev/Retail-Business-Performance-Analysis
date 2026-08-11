import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/superstore_cleaned.csv")

print("SUPERSTORE SALES & PROFIT ANALYSIS")
print("----------------------------------")

# 1. Overall KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
average_discount = df["Discount"].mean()

print("\nOVERALL KPIs")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Average Discount:", round(average_discount * 100, 2), "%")


# 2. Category analysis
category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Profit", ascending=False)

print("\nCATEGORY PERFORMANCE")
print(category_analysis)


# 3. Sub-category analysis
subcategory_analysis = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Profit", ascending=False)

print("\nSUB-CATEGORY PERFORMANCE")
print(subcategory_analysis)


# 4. Region analysis
region_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Profit", ascending=False)

print("\nREGION PERFORMANCE")
print(region_analysis)


# 5. Yearly analysis
year_analysis = df.groupby("Order Year").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

print("\nYEARLY PERFORMANCE")
print(year_analysis)


# 6. Loss-making products
loss_products = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
)

loss_products = loss_products[
    loss_products["Profit"] < 0
].sort_values("Profit")

print("\nTOP 10 LOSS-MAKING PRODUCTS")
print(loss_products.head(10))


# 7. High sales but low profit
product_analysis = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
)

high_sales_low_profit = product_analysis[
    (product_analysis["Sales"] > product_analysis["Sales"].median()) &
    (product_analysis["Profit"] < 0)
].sort_values("Sales", ascending=False)

print("\nHIGH SALES BUT LOSS-MAKING PRODUCTS")
print(high_sales_low_profit.head(10))


# 8. Save analysis results
category_analysis.to_csv("../data/category_analysis.csv")
subcategory_analysis.to_csv("../data/subcategory_analysis.csv")
region_analysis.to_csv("../data/region_analysis.csv")
year_analysis.to_csv("../data/year_analysis.csv")
loss_products.to_csv("../data/loss_making_products.csv")

print("\nAnalysis files saved successfully!")