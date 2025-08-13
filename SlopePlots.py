import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_slopeplot():
    """
    Create a slopeplot comparing total bills between Lunch and Dinner.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The figure object containing the slopeplot.
    """
    # YOUR CODE HERE
    np.random.seed(32)
    n = 200
    data = pd.DataFrame({
        'time': np.random.choice(['Lunch', 'Dinner'], size=n),
        'smoker': np.random.choice(['Yes', 'No'], size=n),
        'total_bill': np.random.uniform(10, 50, size=n)
    })
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.pointplot(
        data=data,
        x='time',
        y='total_bill',
        hue='smoker',
        dodge=True,
        markers='o',
        capsize=0.1,
        err_kws={'linewidth': 1.5}
    )

    ax.set_title("Slopeplot: Comparing Total Bills Between Lunch and Dinner", fontsize=14)
    ax.set_xlabel("Time")
    ax.set_ylabel("Average Total Bill")
    plt.show()
    return fig
    
print(plot_slopeplot())