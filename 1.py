import math
import numpy as np
from scipy.interpolate import griddata

# 1. Читаємо координати початку і кінця X1, Y1, X2, Y2
with open('Data1.txt') as f:
    x1, y1, x2, y2 = [float(next(f).strip()) for _ in range(4)]

# 2. Читаємо значення магнітного поля в список
with open('Data1.txt', 'r') as file:
    lines = file.readlines()[5:]
    T = np.array([float(line.strip()) for line in lines])
    T_1d = T.flatten()  # перетворення матриці T розмірності (13, 14) в одновимірний масив розмірності (169,)

# 3. Визначаємо кількість рядків та стовпців для інтерполювання
n_points = len(T_1d)
# n_rows = int(np.sqrt(n_points))
# n_columns = n_points // n_rows
n_rows = 13  # Fixed number of rows
n_columns = n_points // n_rows
# Розраховуємо матрицю інтерпольованих значень X та Y
# xint = np.linspace(x1, x2, n_rows)
# yint = np.linspace(y1, y2, n_columns)
# Xint, Yint = np.meshgrid(xint, yint)
xint = np.linspace(x1, x2, n_rows)
yint = np.linspace(y1, y2, n_columns)
Xint, Yint = np.meshgrid(xint, yint)
# 4. Шукаємо максимальне та мінімальне значення магнітного поля
Tmax, Tmin = np.max(T), np.min(T)

# 5. Отримуємо новий список Ts = T nT-((max-min)/2)
Ts = T - (Tmax - Tmin) / 2

# 6. Маштабуємо значення магнітного поля Tsk = Ts*koef
koef = 1000.0
Tsk = Ts * koef

# Create a 2D array from the 1D array T
T_grid = np.reshape(Tsk, (n_rows, n_columns))

# 7. Здійснюємо поворот системи координат на кут Fi
# a) розраховуємо кут через Xint, Yint
Fi = math.atan2(Yint[-1, -1] - Yint[-1, 0], Xint[-1, -1] - Xint[0, -1])

# б) робимо поворот отримуючи нові значення Tskpov по Xint та Yint+T_grid
Tskpov = np.zeros_like(T_grid)
for i in range(n_rows):
    for j in range(n_columns):
        x, y, t = Xint[i, j], Yint[i, j], T_grid[i, j]
        xp = x * math.cos(Fi) + y * math.sin(Fi)
        yp = -x * math.sin(Fi) + y * math.cos(Fi)
        Tskpov[i, j] = t

# 8. Генеруємо файл kml по Xint та Tskpov
with open('Data1.kml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
    f.write('<kml xmlns="http://earth.google.com/kml/2.2">' + '\n')
    f.write('  <Document>' + '\n')
    f.write('    <name>MagField</name>' + '\n')
    f.write('    <open>1</open>' + '\n')
    for i in range(n_rows):
        for j in range(n_columns):
            f.write(f'    <Placemark>\n')
            f.write(f'      <name>Point ({i},{j})</name>\n')
            f.write(f'      <Point>\n')
            f.write(f'        <coordinates>{Xint[i, j]},{Yint[i, j] + Tskpov[i, j]},0</coordinates>\n')
            f.write(f'      </Point>\n')
            f.write(f'    </Placemark>\n')
    f.write('  </Document>' + '\n')
    f.write('</kml>' + '\n')
