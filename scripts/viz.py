import pandas as pd
import matplotlib.pyplot as plt

# Function to process CSV and create visualization
def visualize_transactions(input_file):
    # Read CSV into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Filter for transactions with Status 'PROCESSED'
    df_processed = df[df['Status'] == 'PROCESSED']
    
    # Convert 'Amount' column to numeric (remove '$' and ',' and convert to float)
    df_processed['Amount'] = df_processed['Amount'].replace('[\$,]', '', regex=True).astype(float)
    
    # Convert 'Date' column to datetime format
    df_processed['Date'] = pd.to_datetime(df_processed['Date'], format='%m/%d/%Y %H:%M')
    
    # Group by date and sum the amounts
    df_daily_total = df_processed.groupby(df_processed['Date'].dt.date)['Amount'].sum()
    
    # Plotting
    plt.figure(figsize=(10, 6))
    df_daily_total.plot(kind='bar', color='skyblue')
    plt.title('Total Amount of Processed Transactions per Day')
    plt.xlabel('Date')
    plt.ylabel('Total Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage:
input_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/transactions.csv"
visualize_transactions(input_file)
