input_filename = "output.txt"

import matplotlib.pyplot as plt

def read_integers_from_file(filename):
    """Reads integers from a file, assuming each line contains a single integer."""
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def calculate_rolling_average(data, window_size):
    """Calculates the rolling average for the given data with the specified window size."""
    if len(data) < window_size:
        raise ValueError("Data length must be greater than or equal to the window size.")
    return [sum(data[i:i+window_size]) / window_size for i in range(len(data) - window_size + 1)]

def plot_rolling_average(rolling_averages):
    """Plots the rolling average using matplotlib."""
    plt.plot(rolling_averages)
    plt.title(f'Rolling Average (Window Size = 50)')
    plt.xlabel('Index')
    plt.ylabel('Rolling Average')
    plt.show()

def main():
    filename = "output.txt"
    window_size = 5000
    
    # Step 1: Read integers from the file
    data = read_integers_from_file(filename)
    
    # Step 2: Calculate the rolling average
    rolling_averages = calculate_rolling_average(data, window_size)
    
    # Step 3: Plot the rolling average
    plot_rolling_average(rolling_averages)

if __name__ == "__main__":
    main()
