# sns.boxplot

# sns.violinplot

# sns.stripplot
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
def plot_categorical_visualizations():
    """
    Create Boxplot, Violinplot, and Stripplot for categorical data.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The figure object containing the plots.
    """
    # YOUR CODE HERE
    np.random.seed(42)

    continent = np.random.choice(
        ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],
        size=100
    )
    lifeExp = np.random.uniform(50, 85, size=100)
    population = np.random.uniform(1e6, 1e9, size=100)

    df = pd.DataFrame({
        "continent": continent,
        "lifeExp": lifeExp,
        "population": population
    })

    fig, axes = plt.subplots(3, 1, figsize=(8, 15))

    sns.boxplot(data=df, x='continent', y='lifeExp', ax=axes[0])
    axes[0].set_xlabel("Continents")
    axes[0].set_ylabel("Life Expectancy")
    axes[0].set_title("Categorical Data Visualization")

    sns.violinplot(data=df, x='continent', y='lifeExp', ax=axes[1])
    axes[1].set_xlabel("Continents")
    axes[1].set_ylabel("Life Expectancy")
    axes[1].set_title("Categorical Data Visualization")

    sns.stripplot(data=df, x='continent', y='lifeExp', jitter=True, ax=axes[2])
    axes[2].set_xlabel("Continents")
    axes[2].set_ylabel("Life Expectancy")
    axes[2].set_title("Categorical Data Visualization")

    plt.tight_layout()
    plt.show()

    return fig
    
print(plot_categorical_visualizations())
