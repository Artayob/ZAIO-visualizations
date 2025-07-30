import numpy as np
import matplotlib.pyplot as plt
def plot_2d_histogram(mean, covariance, size, bins, cmap):
    """
    Plot a 2D histogram for bi-variate data distribution.

    Args:
    mean (list): Mean of the distribution (2D vector).
    covariance (list): Covariance matrix.
    size (int): Number of data points to generate.
    bins (int): Number of bins for the histogram.
    cmap (str): Color map for the histogram.

    Returns:
    matplotlib.figure.Figure: The generated plot figure.
    """
    # YOUR CODE HERE
    data = np.random.multivariate_normal(mean, covariance, size)
    x = data[:, 0]
    y = data[:, 1]
    fig, ax = plt.subplots(figsize=(8,6))
    h = ax.hist2d(x, y, bins=bins, cmap=cmap)
    plt.colorbar(h[3], ax = ax)

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("2D Histogram of Bi-Variate Data")

    plt.tight_layout()
    plt.show()

    return fig
print(plot_2d_histogram(mean=[0,0], covariance=[[1,1],[1,2]], size=10000, bins=30, cmap='viridis' ))