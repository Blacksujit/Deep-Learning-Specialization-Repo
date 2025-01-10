import pandas as pd

# Define data
data = {
    'age': [25, 32, 41, 18, 55, 28, 39, 62, 21, 48],
    'EstimatedSalary': [50000, 78000, 92000, 35000, 120000, 65000, 88000, 150000, 42000, 105000],
    'purchased': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('purchase_data.csv', index=False)

print("CSV file 'purchase_data.csv' created successfully!")
