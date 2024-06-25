import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
file_path = 's.csv'  # Path to your uploaded CSV file
df = pd.read_csv(file_path)

# Display the original DataFrame
print("Original DataFrame:")
print(df.head())

# Function to generate random value based on the data type
def get_random_number():
    return np.random.uniform(low=0, high=100)  # Generate a random float number

# Initialize change indicator list
change_indicator = [0] * len(df)

# Parameters for random selection
num_rows_to_change = int(len(df) * 0.4)  # Change 40% of the rows
num_columns_to_change = int(len(df.columns) * 0.2)  # Change 20% of the columns

# Randomly select rows to change
rows_to_change = np.random.choice(df.index, num_rows_to_change, replace=False)

for row in rows_to_change:
    # Randomly select columns to change for this row
    columns_to_change = np.random.choice(df.columns, num_columns_to_change, replace=False)
    for col in columns_to_change:
        df.at[row, col] = get_random_number()
    change_indicator[row] = 1  # Mark as changed

# Add the change indicator column to the DataFrame
df['label'] = change_indicator

# Display the modified DataFrame
print("\nModified DataFrame:")
print(df.head(20))  # Display the first 20 rows to check modifications

# Save the modified DataFrame to a new CSV file
modified_file_path = '4-2.csv'  # Adjust this as needed
df.to_csv(modified_file_path, index=False)

print(f"\nModified DataFrame saved to {modified_file_path}")
