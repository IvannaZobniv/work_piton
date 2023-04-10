# import numpy as np
# from matplotlib import pyplot as plt
#
# f = open("data.txt")
# x,y = [], []
# m=0
# # Читаємо точки даних магнітного поля
# while True:
#     line = f.readline().strip()
#     if not line:
#         break
#     mag_val = float(line)
#     m = m+1
#     x.append(m)
#     y.append(mag_val-50750)
# f.close()
#
# print(x)
# print(y)
# plt.plot(x, y)
# plt.show()
#
# # from scipy.fft import fft, fftfreq
#
# #  число точок в normalized_tone
# # yf = fft(y)
# # xf = fftfreq(m,1)
# #
# # plt.plot(xf,np.abs(yf))
# # plt.show()
#
# from scipy.fft import rfft, rfftfreq
#
# yf = rfft(y)
# xf = rfftfreq(m,1)
#
# plt.plot(xf,np.abs(yf))
# plt.show()
#
# # Обнулим yf для індексів біля цілої частини:
# yf[10:300]=0
#
# plt.plot(xf,np.abs(yf))
# plt.show()
#
# from scipy.fft import irfft
# new_sig = irfft(yf)
# f = open("data_out.csv", "w")
# for i in range(m):
#     f.write(str(i)+";"+str(y[i])+";"+str(new_sig[i])+"\n")
# f.close()
#
# plt.plot(new_sig[:m])
# plt.show()
# --------------------------


# --------------------------
# import os
# import numpy as np
# import sys
# from matplotlib import pyplot as plt
# from scipy.fft import rfft, rfftfreq, irfft
# import re
#
# def read_data(filename):
#     x, y = [], []
#     m = 0
#     data_block = False
#
#     with open(filename, "r") as f:
#         while True:
#             line = f.readline().strip()
#             # Вийти з циклу, коли дійшли до кінця файлу
#             if not line:
#                 if f.tell() == os.fstat(f.fileno()).st_size:
#                     break
#                 else:
#                     continue
#
#             print(f"Processing line: {line}")
#
#             if line.startswith("Дата:") or line.startswith("Участок:") or line.startswith("Режим МВС"):
#                 continue
#             elif line.startswith("Поле") and line.endswith("Время"):
#                 data_block = True
#                 continue
#             elif data_block:
#                 if re.match(r'^\d+(\.\d+)?$', line):
#                     mag_val = float(line)
#                     m += 1
#                     x.append(m)
#                     y.append(mag_val - 50750)
#                 else:
#                     data_block = False
#                     print(f"Skipping line: {line}")
#             else:
#                 print(f"Skipping line: {line}")
#
#     if not x or not y:
#         raise ValueError("No valid data found in the input file")
#
#     return x, y
#
# def filter_data(data, freq_range=(10, 300)):
#     """
#     Фільтрує дані магнітного поля, використовуючи перетворення Фур'є.
#
#     :param data: Список точок магнітного поля.
#     :param freq_range: Діапазон частот для обнулення.
#     :return: Відфільтрований сигнал.
#     """
#     yf = rfft(data)
#     xf = rfftfreq(len(data), 1)
#
#     yf[slice(*freq_range)] = 0
#
#     filtered_signal = irfft(yf)
#     if len(filtered_signal) != len(data):
#         filtered_signal = np.append(filtered_signal, [0] * (len(data) - len(filtered_signal)))
#
#     return filtered_signal
#
# def save_data(file_name, original_data, filtered_data):
#     """
#     Зберігає вихідні та відфільтровані дані у файлі CSV.
#
#     :param file_name: Ім'я вихідного файлу.
#     :param original_data: Список вихідних точок магнітного поля.
#     :param filtered_data: Список відфільтрованих точок магнітного поля.
#     """
#     with open(file_name, "w") as f:
#         for i, (orig, filt) in enumerate(zip(original_data, filtered_data)):
#             f.write(f"{i};{orig};{filt}\n")
#
#
# def plot_data(original_data, filtered_data):
#     """
#     Відображає вихідні та відфільтровані дані на графіках.
#
#     :param original_data: Список вихідних точок магнітного поля.
#     :param filtered_data: Список відфільтрованих точок магнітного поля.
#     """
#     x = range(len(original_data))
#     plt.figure(figsize=(12, 6))
#
#     plt.subplot(1, 2, 1)
#     plt.plot(x, original_data)  # Змініть цей рядок
#     plt.title("Original Data")
#
#     plt.subplot(1, 2, 2)
#     plt.plot(x, filtered_data)  # Змініть цей рядок
#     plt.title("Filtered Data")
#
#     plt.tight_layout()
#     plt.show()
# def main():
#     input_file = "pkm.txt."
#     output_file = "data_out.csv"
#
#     x, y = read_data(input_file)
#     filtered_data = filter_data(y)
#
#     assert len(y) == len(filtered_data), "Original data and filtered data arrays have different sizes."
#
#     save_data(output_file, y, filtered_data)
#     plot_data(y, filtered_data)
#     plt.show()
#
#
# if __name__ == "__main__":
#     main()
