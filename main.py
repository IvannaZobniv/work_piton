# import numpy as np
# # вказуємо довжигу профіля
# len_prof = 50
# # вказуємо детальність по профілю
# det = 500
# #  Вказуємо відстань між профілями
# del_prof = 0.5
# # обхід змійкою: 0 - ні, 1-так
# zmeya =1
# # снять тренд: 0 - ні, 1-так
# trend =1
#
# f = open("pkm.txt")
# f1 = open("pkm_out.csv", "w")
# a1 = []
# b1 =[]
# c1 = []
# Count =-1
# Mag = []
# X=[]
# Y =[]
# Zi=[]
# Z=[]
# v = 0
# D = 349057 # долгота
# S = 5570360 # широта
# mimi = 10000000
# mama = 0
# # Читаємо значення магнітного поля
# while True:
#     Zn = f.readline()
#     if not Zn:
#         break
#     if not (Zn.find("Поле")==-1):
#         Mag = []
#         X = []
#         Xi =[]
#         Z = []
#         Y =[]
#         Yi = []
#         Zi = []
#         Points =0
#         Count = Count +1
#         dolgota = D+ Count* del_prof
#         while True:
#             Zn = f.readline()
#             Zn = Zn.strip()
#             if len (Zn)==0:
#                 break
#             magi = float(Zn)
#             if magi > mama: mama=magi
#             if magi <mimi: mimi=magi
#             Mag.append(magi)
#             Points = Points+1
#         v =0
#         for i in range(Points-1):
#             v =v+1
#             Y.append(v)
#             if zmeya == 0:
#                 Z.append(Mag[i])
#             if zmeya == 1:
#                 if Count % 2:
#                     Z.append(Mag[Points-2-i])
#                 else:
#                     Z.append(Mag[i])
#         delta = (Points-1)/det
#         for i in range(det):
#             xi = (i-1)*delta
#             Xi.append(dolgota)
#             yi =S +i*len_prof/det
#             Yi.append(yi)
#             eri = np.interp(xi,Y,Z)
#             Zi.append(eri)
#             f1.write(str(dolgota)+";"+ str(yi)+";"+str(eri)+"/n")
#         if trend == 1:
#             summa = 0
#             for i in Zi:
#                 summa = summa+i
#             sred = summa/det
#             for i in range(det):
#                 Zi[i-1] = Zi[i-1]-sred
#             a1.append(Yi)
#             b1.append(Xi)
#             c1.append(Zi)
# f.close()
# f1.close()
#
# import  matplotlib.pyplot as plt
# import numpy as np
# plt.style.use('_mpl-gallery-nogrid')
#
# # levels = np.linspace(50730,50770,40)
# levels = np.linspace(-20, 20, 40)
# print(mimi, mama)
# fig, ax = plt.subplots()
# ax.contourf(b1,a1,c1, levels=levels)
# plt.show()
# ----------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Input parameters
# len_prof = 50
# det = 500
# del_prof = 0.5
# zmeya = 1
# trend = 1
#
# D = 349057  # Longitude
# S = 5570360  # Latitude
#
# # Function to process and return magnetic field data
# def process_magnetic_data(file_path):
#     min_val = 10000000
#     max_val = 0
#     count = -1
#     a1, b1, c1 = [], [], []
#
#     with open(file_path, 'r') as f:
#         while True:
#             line = f.readline()
#             if not line:
#                 break
#             if "Поле" in line:
#                 count += 1
#                 longitude = D + count * del_prof
#                 mag_data, y, z = [], [], []
#
#                 # Read magnetic field data points
#                 while True:
#                     line = f.readline().strip()
#                     if not line:
#                         break
#                     mag_val = float(line)
#                     min_val = min(min_val, mag_val)
#                     max_val = max(max_val, mag_val)
#                     mag_data.append(mag_val)
#
#                 # Process magnetic field data
#                 for i, mag_val in enumerate(mag_data[:-1]):
#                     y.append(i)
#                     z.append(mag_data[-2 - i] if count % 2 and zmeya else mag_val)
#
#                 delta = (len(mag_data) - 1) / det
#                 xi, yi, zi = [], [], []
#
#                 for i in range(det):
#                     xi.append(longitude)
#                     yi.append(S + i * len_prof / det)
#                     zi.append(np.interp((i - 1) * delta, y, z))
#
#                 if trend:
#                     mean = np.mean(zi)
#                     zi = [val - mean for val in zi]
#
#                 a1.append(yi)
#                 b1.append(xi)
#                 c1.append(zi)
#
#     return a1, b1, c1, min_val, max_val
#
#
# # Process the magnetic field data and write the output to a CSV file
# a1, b1, c1, min_val, max_val = process_magnetic_data("pkm.txt")
#
# with open("pkm_out.csv", "w") as f_out:
#     for xi, yi, zi in zip(b1, a1, c1):
#         for x, y, z in zip(xi, yi, zi):
#             f_out.write(f"{x};{y};{z}\n")
#
# # Plot the magnetic field data using a filled contour plot
# plt.style.use('_mpl-gallery-nogrid')
# levels = np.linspace(-20, 20, 40)
# print(min_val, max_val)
#
# fig, ax = plt.subplots()
# ax.contourf(b1, a1, c1, levels=levels)
# plt.show()


