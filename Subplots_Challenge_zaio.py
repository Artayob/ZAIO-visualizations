import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
def create_subplots():
    """
    Create subplots using different Matplotlib methods: plt.subplot, plt.subplots, and GridSpec.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The final figure created for validation
    """
    fig = plt.figure(figsize=(8, 6))
    gs = gridspec.GridSpec(3, 3)
    ax_main = fig.add_subplot(gs[1:, :2])
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    ax_main.scatter(x, y, alpha=0.5)
    ax_main.set_title("Main Plot")
    ax_main.set_xlabel("X-axis")
    ax_main.set_ylabel("Y-axis")
    ax_top = fig.add_subplot(gs[0, :2], sharex=ax_main)
    ax_top.hist(x, bins=30, color='skyblue')
    ax_top.axis('off')
    ax_right = fig.add_subplot(gs[1:, 2], sharey=ax_main)
    ax_right.hist(y, bins=30, orientation='horizontal', color='lightgreen')
    ax_right.axis('off')

    fig.suptitle("GridSpec Layout with Marginal Histograms", fontsize=16)
    plt.tight_layout()
    plt.show()
    return fig
print(create_subplots())