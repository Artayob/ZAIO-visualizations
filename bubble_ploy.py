import matplotlib.pyplot as plt

def basic_bubble_chart(x, y, sizes):
    """
    Create a simple bubble chart.

    Args:
    x (list): X-axis values.
    y (list): Y-axis values.
    sizes (list): Bubble sizes.

    Returns:
    matplotlib.figure.Figure: The created figure object for testing.
    """
    # YOUR CODE HERE
    fig, ax = plt.subplots()
    ax.scatter(x, y, s= sizes, color='blue', alpha=0.5)
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    ax.set_title("Basic Bubble Chart")

    return fig

print(basic_bubble_chart([5, 7, 8, 7, 6, 9, 5], [99, 86, 87, 88, 100, 86, 103], [20, 50, 100, 200, 500, 1000, 60]))