import pandas as pd

# Load dataset
df = pd.read_csv("leads-100.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display missing values before cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values in numeric columns
df = df.fillna(df.mean(numeric_only=True))

# Fill missing values in text columns
for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Display missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("leads-100-cleaned.csv", index=False)

print("\nData cleaning completed successfully!")
