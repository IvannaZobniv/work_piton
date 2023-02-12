import numpy as np
import matplotlib.pyplot as plt

# Читання даних із вхідного файлу
data = np.genfromtxt('data.txt')

# Параметри фільтра Калмана
k = 0.2 # Фактор згладжування
M = data[0] # Початкове значення М

# Застосування до даних фільтр Калмана
filtered_data = []
for A in data:
    Mi = k*A + (1-k)*M
    filtered_data.append(Mi)
    M = Mi

# Збереження необроблених та відфільтрованих даних у файл CSV
np.savetxt('output.csv', np.column_stack((data, filtered_data)), delimiter=',')

# Побудудова необроблених та відфільтрованих дані в графік
plt.plot(data, label='Raw Data')
plt.plot(filtered_data, label='Filtered Data')
plt.legend()
plt.show()
