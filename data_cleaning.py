import pandas as pd

# -----------------------------------
# 1. Load the dataset
# -----------------------------------

file_path = "../data/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("DATASET LOADED SUCCESSFULLY")
print("--------------------------------")

# -----------------------------------
# 2. Display basic information
# -----------------------------------

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

# -----------------------------------
# 3. Check missing values
# -----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------
# 4. Check duplicate records
# -----------------------------------

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# -----------------------------------
# 5. Convert date columns
# -----------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDate columns converted successfully.")

# -----------------------------------
# 6. Check data types
# -----------------------------------

print("\nData Types:")
print(df.dtypes)

# -----------------------------------
# 7. Remove duplicates
# -----------------------------------

df = df.drop_duplicates()

# -----------------------------------
# 8. Create useful date columns
# -----------------------------------

df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.month_name()

# -----------------------------------
# 9. Calculate Profit Margin
# -----------------------------------

df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

# -----------------------------------
# 10. Save cleaned dataset
# -----------------------------------

output_path = "../data/superstore_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_path)

# -----------------------------------
# 11. Final dataset information
# -----------------------------------

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())