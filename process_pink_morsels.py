import pandas as pd
import os

# Path to the folder containing your CSV files
data_folder = 'data'

# List all CSV files in the folder
csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]

# Prepare a list to hold processed DataFrames
processed_dfs = []

for file in csv_files:
    # Read CSV
    df = pd.read_csv(file)

    # Filter for Pink Morsel only
    df = df[df['product'] == 'Pink Morsel']

    # Calculate sales = quantity * price
    df['sales'] = df['quantity'] * df['price']

    # Keep only required columns
    df = df[['sales', 'date', 'region']]

    # Add to list
    processed_dfs.append(df)

# Combine all processed CSVs into one DataFrame
combined_df = pd.concat(processed_dfs, ignore_index=True)

# Save to a new CSV
output_file = os.path.join(data_folder, 'pink_morsels_sales.csv')
combined_df.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")