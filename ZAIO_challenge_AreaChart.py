import pandas as pd
import matplotlib.pyplot as plt
def plot_area_charts():
    """
    Create and return stacked and overlapped area charts for Covid data.

    Args:
    None

    Returns:
    tuple: Two Matplotlib figures for the stacked and overlapped area charts
    """
    # YOUR CODE HERE
    data = {
        "Total Daily Infection": [1326, 1456, 1794, 1712, 1634, 1565],
        "Vaccine Jab 1": [651, 670, 710, 736, 722, 768],
        "Vaccine Jab 2": [322, 341, 361, 383, 399, 404]
    }

    # Step 2: Create a 6-day date index starting from 2021-04-01
    dates = pd.date_range(start="2021-04-01", periods=6, freq='D')

    # Step 3: Create the DataFrame
    df = pd.DataFrame(data, index=dates)

    # Step 4: Plot stacked area chart
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    df.plot.area(ax=ax1, stacked=True)
    ax1.set_title("Stacked Area Chart: Covid Data")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Values")
    ax1.legend(loc="upper left")
    ax1.grid(True)
    fig1.tight_layout()
    plt.show()

    # Step 5: Plot overlapped area chart (not stacked)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    df.plot.area(ax=ax2, stacked=False)
    ax2.set_title("Overlapped Area Chart: Covid Data")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Values")
    ax2.legend(loc="upper left")
    ax2.grid(True)
    fig2.tight_layout()
    plt.show()
    return fig1, fig2

print(plot_area_charts())