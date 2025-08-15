import matplotlib.pyplot as plt
import pandas as pd

def plot_seasonal_trendchart():
    """
    Plot a simple seasonal trend chart for airline passenger counts over time.

    Args:
    None

    Returns:
    matplotlib.figure.Figure: The figure object containing the trend chart.
    """
    # YOUR CODE HERE
    data = pd.DataFrame({
        'year': [
            1949, 1949, 1949, 1949, 1949, 1949, 1949, 1949, 1949, 1949, 1949, 1949,
            1950, 1950, 1950, 1950, 1950, 1950, 1950, 1950, 1950, 1950, 1950, 1950
        ],
        'month': [
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December',
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ],
        'passengers': [
            112, 118, 132, 129, 121, 135, 148, 148, 136, 119, 104, 118,
            115, 126, 141, 135, 125, 149, 170, 170, 158, 133, 114, 140
        ]
    })

    data['date'] = pd.to_datetime(data['year'].astype(str) +'-'+ data['month'], format='%Y-%B')
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(data['date'], data['passengers'], marker='o', linestyle='-')

    ymin, ymax = min(data['passengers']) - 10, max(data['passengers']) + 10
    ax.set_ylim(ymin, ymax)

    ax.set_title("Seasonal Trend of Airline Passengers")
    ax.set_xlabel("Time")
    ax.set_ylabel("Passengers")
    tick_labels = [f"{y}-{m}" for y, m in zip(data['year'], data['month'])]
    ax.set_xticks(data['date'])
    ax.set_xticklabels(tick_labels, rotation=45)
    plt.show()
    plt.tight_layout()
    return fig

print(plot_seasonal_trendchart())