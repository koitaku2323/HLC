import pandas as pd

# Function to filter and process CSV using pandas
def process_csv(input_file, output_file):
    # Read CSV into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Filter for transactions with Status 'PROCESSED'
    df_filtered = df[df['Status'] == 'PROCESSED']
    
    # Select Date and Amount columns
    df_filtered = df_filtered[['Date', 'Amount']]
    
    # Write filtered DataFrame to CSV
    df_filtered.to_csv(output_file, index=False)

# Example usage:
input_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/transactions.csv"
output_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/processed_transactions.csv"
process_csv(input_file, output_file)
