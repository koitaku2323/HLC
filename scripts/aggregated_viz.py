import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

# Function to visualize aggregated transaction amounts by month
def visualize_aggregated_transactions(input_file):
    # Read aggregated CSV into a pandas DataFrame
    df_aggregated = pd.read_csv(input_file)
    
    # Convert 'Date' column to datetime format
    df_aggregated['Date'] = pd.to_datetime(df_aggregated['Date'])
    
    # Set figure size
    plt.figure(figsize=(12, 6))
    
    # Plotting
    plt.bar(df_aggregated['Date'], df_aggregated['Amount'], color='skyblue', width=20)
    plt.title('Total Transaction Amounts per Month')
    plt.xlabel('Month')
    plt.ylabel('Total Amount ($)')
    plt.xticks(df_aggregated['Date'], df_aggregated['Date'].dt.strftime('%Y-%m'), rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage:
input_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/aggregated_transactions.csv"
visualize_aggregated_transactions(input_file)
