import matplotlib.pyplot as plt
import numpy as np
def plot_simple_bar_chart():
    """
    Create and return a simple bar chart for monthly sales.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [100, 123, 210, 178, 201]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(months, sales, color='royalblue')
    ax.set_xlabel("Months")
    ax.set_ylabel("Number of Units Sold")
    ax.set_title("Monthly Sales of TVs")
    plt.show()
    return fig
    
print(plot_simple_bar_chart())

def plot_grouped_bar_chart():
    """
    Create and return a grouped bar chart for two sales agents.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    john_sales = [100, 123, 210, 178, 201]
    mary_sales = [107, 121, 232, 155, 232]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    bar_width = 0.4
    x = np.arange(len(months))
    john_color = (0.0, 0.0, 1.0)  
    mary_color = (0.0, 1.0, 0.0) 
    fig, ax = plt.subplots()
    ax.bar(x, john_sales, width=bar_width, color=john_color, label='John')
    ax.bar(x + bar_width, mary_sales, width=bar_width, color=mary_color, label='Mary')
    ax.set_xlabel('Months')
    ax.set_ylabel('Number of Units Sold')
    ax.set_title('Monthly Sales Comparison')
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(months)
    ax.legend()
    plt.show()
    return fig

print(plot_grouped_bar_chart())

def plot_stacked_bar_chart():
    """
    Create and return a stacked bar chart for two sales agents.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    john_sales = [100, 123, 210, 178, 201]
    mary_sales = [107, 121, 232, 155, 232]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    fig, ax = plt.subplots()
    ax.bar(months, john_sales, color='blue', label='John')
    ax.bar(months, mary_sales, bottom=john_sales, color='green', label='Mary')
    ax.set_xlabel("Months")
    ax.set_ylabel("Number of Units Sold")
    ax.set_title("Monthly Sales Stacked Comparison")
    ax.legend()
    plt.show()
    return fig
print(plot_stacked_bar_chart())

def plot_grouped_bar_chart():
    """
    Create and return a grouped bar chart for two sales agents.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    john_sales = [100, 123, 210, 178, 201]
    mary_sales = [107, 121, 232, 155, 232]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    x = np.arange(len(months))       
    bar_width = 0.4                  
    fig, ax = plt.subplots()
    ax.bar(x, john_sales, width=bar_width, color='blue', label='John')
    ax.bar(x + bar_width, mary_sales, width=bar_width, color='green', label='Mary')
    ax.set_xlabel('Months')
    ax.set_ylabel('Number of Units Sold')
    ax.set_title('Monthly Sales Grouped Comparison')
    ax.set_xticks(x + bar_width / 2) 
    ax.set_xticklabels(months)
    ax.legend()
    plt.show()
    return fig
print(plot_grouped_bar_chart())

def plot_horizontal_bar_chart():
    """
    Create and return a horizontal bar chart for monthly sales.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    sales = [100, -123, 210, 178, 201]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    fig, ax = plt.subplots()
    bars = ax.barh(months, sales, color='royalblue')
    for bar in bars:
        width = bar.get_width()
        y_pos = bar.get_y() + bar.get_height() / 2
        if width >= 0:
            ax.text(width + 5, y_pos, f'{width}', va='center')
        else:
            ax.text(width - 5, y_pos, f'{width}', va='center', ha='right')
    ax.set_xlabel('Number of Units Sold')
    ax.set_ylabel('Months')
    ax.set_title('Monthly Sales Horizontal Chart')
    plt.show()
    return fig
print(plot_horizontal_bar_chart())