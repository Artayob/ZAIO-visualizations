import matplotlib.pyplot as plt 
import pandas as pd
def plot_countries_per_continent():
    """
    Create a bar chart showing the number of countries per continent.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The bar chart figure object.
    """
    # YOUR CODE HERE
    data = {
    'country': ['India', 'China', 'USA', 'Germany', 'France', 'Nigeria', 'Kenya', 'Brazil', 'Argentina', 'Australia'],
    'continent': ['Asia', 'Asia', 'North America', 'Europe', 'Europe', 'Africa', 'Africa', 'South America', 'South America', 'Oceania']
    }
    df = pd.DataFrame(data)
    continent_count = df.groupby('continent')['country'].nunique()

    fig, ax = plt.subplots()
    continent_count.plot(kind='bar', ax=ax)

    ax.set_xlabel("Continent")
    ax.set_ylabel("Number of Countries")
    ax.set_title("Number of Countries per Continent")
    plt.show()
    return fig

print(plot_countries_per_continent())