import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap():
    """
    Create a heatmap to visualize correlations in a dataset.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The figure object containing the heatmap.
    """
    # YOUR CODE HERE
    data = {
        'Engine_Size': [1.6, 2.0, 2.4, 3.0, 3.5, 4.0],
        'Horsepower': [110, 150, 180, 250, 300, 350],
        'Fuel_Efficiency': [35, 30, 28, 25, 20, 18],
        'Price': [20, 25, 28, 35, 40, 50]
    }
    df = pd.DataFrame(data)
    corr_matrix = df.corr()

    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(corr_matrix,annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("Correlation Heatmap")

    plt.tight_layout()
    plt.show()
    return fig
print(plot_correlation_heatmap())