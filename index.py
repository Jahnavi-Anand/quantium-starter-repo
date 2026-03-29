import pandas as pd

# Load all 3 CSV files
df1 = pd.read_csv('daily_sales_data_0.csv')
df2 = pd.read_csv('daily_sales_data_1.csv')
df3 = pd.read_csv('daily_sales_data_2.csv')

# Combine them into one DataFrame
df = pd.concat([df1, df2, df3], ignore_index=True)

# Filter only Pink Morsels (handle case + extra spaces safely)
df['product'] = df['product'].str.strip().str.lower()
df = df[df['product'] == 'pink morsel']

# Create sales column
df['sales'] = df['quantity'] * df['price']

# Keep only required columns
df = df[['sales', 'date', 'region']]

# Save output file (inside data folder)
df.to_csv('formatted_output.csv', index=False)

print("✅ formatted_output.csv created successfully!")