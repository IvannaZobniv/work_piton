import matplotlib.pyplot as plt
import numpy as np
import csv

with open('input.txt') as f:
    List_data = [float(line.strip()) for line in f]

Oser = int(input("Enter the size of the moving average window (Oser): "))
List_oseredn = []
List_minus = []
List_copia = []

i = int((Oser + 1) / 2) # Позначтити перший елемент для згладжування
p = i
delta = i - 1

# Згладжування за значеннями елементів
while i < len(List_data) - p:
    left = i - delta
    Summa = 0
    u = 1

    # Сума в межах вікна згладжування
    while u < Oser+1:
        Summa = Summa + List_data[left + u - 1]
        u = u + 1

    List_oseredn.append(Summa / Oser) # Додавання згладженого значення до списку
    List_copia.append(List_data[i]) # копія
    List_minus.append(List_data[i] - Summa / Oser) # Додавання різниці до списку
    i = i + 1

x = np.arange(1, i-delta, 1)
plt.plot(x, List_oseredn, x, List_copia)
plt.show()

x = np.arange(1, i-delta, 1)
plt.plot(x, List_minus)
plt.show()
# Збереження згладжених даних у файлі CSV
# with open("smoothed_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     for i, value in enumerate(List_oseredn):
#         writer.writerow([i, value])

np.savetxt('output.csv', np.column_stack((List_copia, List_oseredn, List_minus,)), delimiter=';')