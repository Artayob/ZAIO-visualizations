import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
def plot_marginal_histograms():
    """
    Create a scatter plot with marginal histograms to visualize data distribution.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The Matplotlib figure object.
    """
    # YOUR CODE HERE
    x = np.random.randn(10000)
    y = np.random.randn(10000)
    fig = plt.figure(figsize=(8, 8))
    gs = GridSpec(4, 4, figure=fig)
    ax_main = fig.add_subplot(gs[1:4, 0:3])
    ax_main.scatter(x, y, alpha=0.5, edgecolors='none')
    ax_main.set_xlabel('X-axis')
    ax_main.set_ylabel('Y-axis')
    ax_main.set_title('Scatter Plot with Marginal Histograms')
    ax_xhist = fig.add_subplot(gs[0, 0:3], sharex=ax_main)
    ax_xhist.hist(x, bins=100, color='skyblue')
    ax_xhist.axis('off')
    ax_yhist = fig.add_subplot(gs[1:4, 3], sharey=ax_main)
    ax_yhist.hist(y, bins=100, orientation='horizontal', color='salmon')
    ax_yhist.axis('off')

    plt.tight_layout()
    plt.show()
    return fig

print(plot_marginal_histograms())


def plot_marginal_boxplots():
    """
    Create a scatter plot with marginal boxplots to visualize data distribution.
    
    Args:
        None

    Returns:
        matplotlib.figure.Figure: The Matplotlib figure object.
    """
    # YOUR CODE HERE
    x = np.random.randn(10000)
    y = np.random.randn(10000)
    fig = plt.figure(figsize=(8, 8))
    gs = GridSpec(4, 4, figure=fig)
    ax_main = fig.add_subplot(gs[1:4, 0:3])
    scatter = ax_main.scatter(x, y, alpha=0.5, color='blue', edgecolors='none')
    ax_main.set_xlabel('X-axis')
    ax_main.set_ylabel('Y-axis')
    ax_main.set_title('Scatter Plot with Marginal Boxplots')
    ax_top = fig.add_subplot(gs[0, 0:3], sharex=ax_main)
    ax_top.boxplot(x, vert=False, patch_artist=True,
                   boxprops=dict(facecolor='skyblue', alpha=0.5),
                   medianprops=dict(color='black'))
    ax_top.axis('off') 
    ax_right = fig.add_subplot(gs[1:4, 3], sharey=ax_main)
    ax_right.boxplot(y, vert=True, patch_artist=True,
                     boxprops=dict(facecolor='salmon', alpha=0.5),
                     medianprops=dict(color='black'))
    ax_right.axis('off')  
    plt.tight_layout()
    plt.show()
    return fig

print(plot_marginal_boxplots())

