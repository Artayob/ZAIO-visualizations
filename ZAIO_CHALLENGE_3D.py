import matplotlib.pyplot as plt
import numpy as np
def plot_3d_visualizations():
    """
    Create 3D line plot, scatter plot, and contour plot.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The generated Matplotlib figure for validation
    """
    # YOUR CODE HERE
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(-12, 12, 100)
    r = 2
    c = 3
    x_line = r * np.sin(theta)
    y_line = r * np.cos(theta)
    z_line = c * theta
    ax.plot3D(x_line, y_line, z_line, label="3D Line (Helix)")

    x_scatter = np.random.randn(100)
    y_scatter = np.random.randn(100)
    z_scatter = np.random.randn(100)
    ax.scatter3D(x_scatter, y_scatter, z_scatter, c=z_scatter, cmap='viridis', label="3D Scatter")

    def f(x, y):
        return np.sin(np.sqrt(x**2 + y**2))
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.contour3D(X, Y, Z, 50, cmap="viridis")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("3D Visualizations")
    ax.legend()

    plt.tight_layout()
    plt.show()
    return fig
print(plot_3d_visualizations())