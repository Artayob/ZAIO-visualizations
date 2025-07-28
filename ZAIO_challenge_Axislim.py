import numpy as np
import matplotlib.pyplot as plt
def plot_sine_with_limits():
    """
    Plot a sine wave with customized axis limits.

    Args:
    None

    Returns:
    matplotlib.figure.Figure, matplotlib.axes._axes.Axes: The figure and axis objects for validation.
    """
    # YOUR CODE HERE
    x = np.linspace(0.2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    plt.xlim(0.2 * np.pi)
    plt.ylim(-1, 1)
    plt.axis([0, 2 * np.pi, -1.5, 1.5])

    ax.set_xlabel("Angle (radians)")
    ax.set_ylabel("Sine Value")
    ax.set_title("Sine Wave with Custom Axis Limits")
    plt.show()
    return fig, ax

print(plot_sine_with_limits())