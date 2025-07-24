#### STUDENT CODE CELL
import matplotlib.pyplot as plt
def create_pyplot_subplots(x, y, filename):
    """
    Create two subplots using the Pyplot interface and save the figure.

    Args:
    x (list): List of x-values for the plot.
    y (list): List of y-values for the plot.
    filename (str): The name of the file to save the figure.

    Returns:
    str: Success message with the filename.
    """
    # YOUR CODE HERE
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y, linestyle='-')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Subplots with Pyplot Interface")

    plt.subplot(1, 2, 2)
    plt.plot(x, y, linestyle='--')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Subplots with Pyplot Interface")

    plt.savefig(filename)
    plt.close()

    return f"Figure saved as {filename}"

print(create_pyplot_subplots([1, 2, 3, 4], [3, 4, 5, 6], "pyplot_subplots.png"))