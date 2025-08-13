import matplotlib.pyplot as plt
import pandas as pd

def plot_dumbbell_chart():
    """
    Create a Dumbbell chart showing GDP changes between 2002 and 2007 for different countries.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The figure object containing the Dumbbell chart.
    """
    # YOUR CODE HERE
    data = pd.DataFrame({
        'Country': ['Country A', 'Country B', 'Country C', 'Country D', 'Country E'],
        'GDP_2002': [15000, 18000, 12000, 16000, 10000],
        'GDP_2007': [20000, 22000, 17000, 18000, 15000]
    })
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(data['GDP_2002'], data['Country'], color = 'blue', s=100, label='2002')
    ax.scatter(data['GDP_2007'], data['Country'], color = 'green', s=100, label='2007')

    for i in range(len(data)):
        ax.plot([data['GDP_2002'][i], data['GDP_2007'][i]], 
                [data['Country'][i], data['Country'][i]], 
                color='gray', linewidth=2)

    ax.set_title("Dumbbell Plot of GDP Change (2002 vs 2007)")
    ax.set_xlabel("GDP")
    ax.set_ylabel("Country")
    ax.legend()
    plt.show()
    return fig
print(plot_dumbbell_chart())