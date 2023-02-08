# import matplotlib.pyplot as plt
# import numpy as np
# import csv
#
# # Відкрийття вхідного текстового файлу
# with open('input.txt') as f:
#     # Прочитання першого рядока, який визначає розмір вікна для ковзного середнього
#     Oser = float(f.readline().strip().replace(',', '.'))
#
#     # Переконатися, що Oser більше нуля
#     if Oser <= 0:
#         print("Window size must be greater than zero.")
#         exit()
#
#     # Прочити всі інші дані в списку
#     List_data = [float(line.strip().replace(',', '.')) for line in f.readlines()]
#
# # Ініціалізація списків для зберігання згладжених даних і відмінностей
# List_oseredn = []
# List_minus = []
# List_copia = []
#
# # Обчислення ковзного середнього даних
# for i in range(int(Oser // 2), len(List_data) - int(Oser // 2)):
#     window_sum = 0
#     for j in range(-int(Oser // 2), int(Oser // 2) + 1):
#         window_sum += List_data[i + j]
#     smoothed = window_sum / Oser
#     List_oseredn.append(smoothed)
#     List_copia.append(List_data[i])
#     List_minus.append(List_data[i] - smoothed)
#
# # Побудудова необроблених даних, згладжені дані та різниця
# x = np.arange(len(List_oseredn))
# plt.plot(x, List_data[int(Oser // 2):len(List_data) - int(Oser // 2)], label='Raw Data')
# plt.plot(x, List_oseredn, label='Smoothed Data')
# plt.legend()
# plt.show()
#
# plt.plot(x, List_minus, label='Difference')
# plt.legend()
# plt.show()
#
# # Збереження згладжених даних у файлі CSV
# with open("smoothed_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     for i, value in enumerate(List_oseredn):
#         writer.writerow([i, value])