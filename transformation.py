import pandas as pd

def drop_columns_from_csv(input_file, output_file, columns_to_drop, column_to_modify):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Drop specified columns
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    # Add a comma after each string value in the specified column
    if column_to_modify in df.columns:
        df[column_to_modify] = df[column_to_modify].astype(str) + ','
    
    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Updated CSV saved as {output_file}")

# Example usage
input_csv = "C:/Users/SBM/Desktop/Trending_Stocks.csv"   # Replace with your input CSV file path
output_csv = "C:/Users/SBM/Desktop/TV_list.csv"  # Replace with your desired output CSV file path
columns_to_remove = ["date", "52wh","close","change","volume","sector","market cap"]  # Replace with actual column names
column_to_modify = "symbol"  # Replace with actual column name to add comma

drop_columns_from_csv(input_csv, output_csv, columns_to_remove, column_to_modify)