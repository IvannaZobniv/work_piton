import matplotlib.pyplot as plt
import numpy as np
import csv

with open('input.txt') as f:
    List_data = [float(line.strip()) for line in f]

Oser = int(input("Enter the size of the moving average window (Oser): "))
List_oseredn = []
List_minus = []
List_copia = []

i = int((Oser + 1) / 2) # Mark the first element for smoothing
p = i
delta = i - 1

# Smoothing by values of elements
while i < len(List_data) - p:
    left = i - delta
    Summa = 0
    u = 1

    # Sum within the smoothing window
    while u < Oser+1:
        Summa = Summa + List_data[left + u - 1]
        u = u + 1

    List_oseredn.append(Summa / Oser) # Add the smoothed value to the list
    List_copia.append(List_data[i]) # Make a copy
    List_minus.append(List_data[i] - Summa / Oser) # Add the difference to the list
    i = i + 1

x = np.arange(1, i-delta, 1)
plt.plot(x, List_oseredn, x, List_copia)
plt.show()

x = np.arange(1, i-delta, 1)
plt.plot(x, List_minus)
plt.show()
# Збереження згладжених даних у файлі CSV
with open("smoothed_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for i, value in enumerate(List_oseredn):
        writer.writerow([i, value])