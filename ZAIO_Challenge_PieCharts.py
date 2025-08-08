#### STUDENT CODE CELL
import matplotlib.pyplot as plt
import warnings
def plot_sales_pie_chart(sales, labels):
    """
    Create and return a pie chart for sales proportions.

    Args:
    sales (list): List of integers representing sales data.
    labels (list): List of strings representing labels for the sales.

    Returns:
    matplotlib.figure.Figure: The created Matplotlib figure for validation.
    """
    # YOUR CODE HERE
    max_index = sales.index(max(sales))
    explode = [0.1 if i == max_index else 0 for i in range(len(sales))]
    colors = ['limegreen', 'lavender', 'orange', 'yellow', 'seagreen']

    fig = plt.figure()
    plt.pie(
        sales,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Sales Proportions")

    plt.show()

    return fig

print(plot_sales_pie_chart([300, 500, 150, 200, 100], ['North', 'South', 'East', 'West', 'Central']))

