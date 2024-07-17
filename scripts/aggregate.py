import pandas as pd

# Function to aggregate transaction amounts by month
def aggregate_transactions(input_file, output_file):
    # Read CSV into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Filter for transactions with Status 'PROCESSED'
    df_processed = df[df['Status'] == 'PROCESSED']
    
    # Convert 'Amount' column to numeric (remove '$' and ',' and convert to float)
    df_processed['Amount'] = df_processed['Amount'].replace('[\$,]', '', regex=True).astype(float)
    
    # Convert 'Date' column to datetime format
    df_processed['Date'] = pd.to_datetime(df_processed['Date'], format='%m/%d/%Y %H:%M')
    
    # Aggregate transaction amounts by month
    df_monthly_total = df_processed.groupby(df_processed['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
    
    # Write aggregated DataFrame to CSV
    df_monthly_total.to_csv(output_file, index=False)

# Example usage:
input_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/transactions.csv"
output_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/aggregated_transactions.csv"
aggregate_transactions(input_file, output_file)
