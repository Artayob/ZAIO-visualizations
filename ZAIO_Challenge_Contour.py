import numpy as np 
import matplotlib.pyplot as plt
def plot_2d_contour():
    """
    Create a 2D contour plot from a 3D function.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    x = np.linspace(0, 5, 100)
    y = np.linspace(0, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(10 * X) + np.cos(10 + Y * X) * np.cos(x) 
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.contour(X, Y, Z, colors='blue')
    contour_filled = ax.contourf(X, Y, Z, cmap='RdGy')

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("2D Contour Plot")
    plt.show()
    return fig

print(plot_2d_contour())