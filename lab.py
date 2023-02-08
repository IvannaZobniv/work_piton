import matplotlib.pyplot as plt
import numpy as np

# Open the input text file
with open('input.txt') as f:
    # Read the first line which defines the window size for moving average
    Oser = float(f.readline().strip().replace(',', '.'))

    # Check that Oser is greater than zero
    if Oser <= 0:
        print("Window size must be greater than zero.")
        exit()

    # Read all the rest of the data into a list
    List_data = [float(line.strip().replace(',', '.')) for line in f.readlines()]

# Initialize lists for storing smoothed data and differences
List_oseredn = []
List_minus = []
List_copia = []

# Calculate the moving average of the data
for i in range(int(Oser // 2), len(List_data) - int(Oser // 2)):
    window_sum = 0
    for j in range(-int(Oser // 2), int(Oser // 2) + 1):
        window_sum += List_data[i + j]
    smoothed = window_sum / Oser
    List_oseredn.append(smoothed)
    List_copia.append(List_data[i])
    List_minus.append(List_data[i] - smoothed)

# Plot the raw data, smoothed data, and difference
x = np.arange(len(List_oseredn))
plt.plot(x, List_data[int(Oser // 2):len(List_data) - int(Oser // 2)], label='Raw Data')
plt.plot(x, List_oseredn, label='Smoothed Data')
plt.legend()
plt.show()

plt.plot(x, List_minus, label='Difference')
plt.legend()
plt.show()
