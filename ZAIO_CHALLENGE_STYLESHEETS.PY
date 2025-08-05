import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def customize_plot_styles():
    """
    Customize plot styles using rcParams and custom stylesheets.

    Args:
    None

    Returns:
    tuple: A tuple of matplotlib.figure.Figure objects (dark_background_figure, custom_stylesheet_figure)
    """
    # YOUR CODE HERE
    print("Available Matplotlib styles:\n", plt.style.available)
    plt.style.use('dark_background')
    mpl.rcParams['lines.linewidth'] = 3
    mpl.rcParams['lines.linestyle'] = '--'
    mpl.rcParams['axes.grid'] = False
    x = np.linspace(0, 10, 100)
    y = x**2
    fig1, ax1 = plt.subplots()
    ax1.plot(x, y)
    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")
    ax1.set_title("Custom Styled Plot with Dark Background")
    with open("mystyle.mplstyle", "w") as f:
        f.write("""\
axes.titlesize : 20
axes.labelsize : 16
lines.linewidth : 5
lines.color : cyan
""")
    plt.style.use('mystyle.mplstyle')
    fig2, ax2 = plt.subplots()
    ax2.plot(x, y)
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax2.set_title("Custom Styled Plot with Dark Background")
    plt.show()
    return fig1, fig2

fig1, fig2 = customize_plot_styles()
print(fig1, fig2)