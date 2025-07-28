import matplotlib.pyplot as plt
def create_scatter_and_line(x, y):
    """
    Create a scatter plot and line plot using the given data.

    Args:
    x (list): List of x-values for the plot.
    y (list): List of y-values for the plot.

    Returns:
    matplotlib.figure.Figure: The matplotlib figure object for validation.
    """
    # YOUR CODE HERE
    fig, ax = plt.subplots()

    ax.scatter(
        x, y, 
        color = 'red',
        s = 100,
        facecolors = 'yellow',
        edgecolors = 'blue',
        linewidth = 2
    )

    ax.plot(x, y, color = 'black', linestyle = '-')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Scatter Plot with Line")

    plt.show()

    return fig, ax
print(create_scatter_and_line([1, 2, 3, 4], [10, 20, 30, 40]))