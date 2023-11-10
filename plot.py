import pandas as pd
import matplotlib.pyplot as plt

def plot_monthly_sales(df):
    """
    Plot the monthly sales of different food types.

    Parameters:
    - df: DataFrame containing sales data with columns 'date' and 'item_type'.
    """
        
    # Convert the 'date' column to datetime format with the correct format specification
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce')

    # Extract month and year from the 'date' column and create a new 'MonthYear' column
    df['MonthYear'] = df['date'].dt.to_period('M')
    # Group by month and food type, then calculate the sum
    monthly_sales = df.groupby(['MonthYear', 'item_type']).size().unstack().fillna(0)

    # Plotting
    plt.figure(figsize=(12, 10))

    # Loop through each food type and plot a line for it
    for food_type in monthly_sales.columns:
        plt.plot(monthly_sales.index.astype(str), monthly_sales[food_type], label=food_type)

    # Customize the plot
    plt.xlabel('Month-Year')
    plt.ylabel('Total Sales')
    plt.title('Monthly Sales of Food Types')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_received_by_distribution(df):
    """
    Plot the distribution of 'received_by' for each year using pie charts.

    Parameters:
    - df: DataFrame containing sales data with columns 'date' and 'received_by'.
    """
   
    # Extract year from the 'date' column and create a new 'Year' column
    df['Year'] = pd.to_datetime(df['date']).dt.year

    # Count the occurrences of each category in 'received_by' for each year
    yearly_received_by = df.groupby(['Year', 'received_by']).size().unstack().fillna(0)

    # Plotting pie charts for each year
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

    for i, year in enumerate(yearly_received_by.index):
        ax = axes[i]
        received_by_count = yearly_received_by.loc[year]
        ax.pie(received_by_count, labels=received_by_count.index, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Distribution of Received By - {year}')

    plt.tight_layout()
    plt.show()

def plot_yearly_transactions(df):
    """
    Plot the yearly transactions by transaction type using a bar chart.

    Parameters:
    - df: DataFrame containing sales data with columns 'date' and 'transaction_type'.
    """
    # Convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Extract year from the 'date' column and create a new 'Year' column
    df['Year'] = df['date'].dt.year

    # Count the transactions for each transaction type, year-wise
    yearly_transactions = df.groupby(['Year', 'transaction_type']).size().unstack().fillna(0)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Bar plot for each transaction type
    yearly_transactions.plot(kind='bar', stacked=False)

    # Customize the plot
    plt.xlabel('Year')
    plt.ylabel('Number of Transactions')
    plt.title('Yearly Transactions by Transaction Type')
    plt.legend(title='Transaction Type')
    plt.xticks(rotation=0)  # Rotate x-axis labels if needed
    plt.show()

# Sample DataFrame (replace this with your actual DataFrame)
df = pd.read_csv('Balaji Fast Food Sales.csv')

# Using the functions
plot_monthly_sales(df)
plot_received_by_distribution(df)
plot_yearly_transactions(df)
