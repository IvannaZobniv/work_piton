import math
import numpy as np

# Читаємо координати початку та кінця
with open('Data1.txt') as f:
    X1, Y1, X2, Y2 = [float(next(f).strip()) for _ in range(4)]

# Читаємо значення магнітного поля в список
Mag = []
with open('Data1.txt') as f:
    for _ in range(5):  # пропускаємо перші 5 рядків
        next(f)
    for line in f:
        Mag.append(float(line.strip()))

# Розмірність сітки
n_rows, n_columns = 13, 14
n_points = len(Mag)

# Перевірка на кількість точок
if n_points != n_rows * n_columns:
    print("Кількість точок на сітці та кількість точок магнітного поля відрізняються")
else:
    # Створюємо інтерпольовану сітку
    Xint = np.linspace(X1, X2, n_columns)
    Yint = np.linspace(Y1, Y2, n_rows)
    Xint, Yint = np.meshgrid(Xint, Yint)

    # Розраховуємо матрицю інтерпольованих значень T
    from scipy.interpolate import griddata

    coords = np.column_stack((Xint.flatten(), Yint.flatten()))
    Tsk = griddata(coords, Mag, (Xint, Yint), method='linear')

    # Знаходимо максимальне та мінімальне значення T
    Tmax, Tmin = np.max(Tsk), np.min(Tsk)

    # Створюємо новий список значень T
    Ts = Tsk - (Tmax - Tmin) / 2

    # Маштабуємо значення T за коєфіцієнтом масштабування koef
    koef = 1000.0
    Tskpov = Ts * koef

    # Розраховуємо кут повороту Fi
    Fi = math.atan2(Yint[-1, -1] - Yint[-1, 0], Xint[-1, -1] - Xint[0, -1])

    # Обчислюємо нові координати
    Xint_new = Xint * np.cos(Fi) + Yint * np.sin(Fi)
    Yint_new = -Xint * np.sin(Fi) + Yint * np.cos(Fi)

    # Створюємо список координат точок та їх відповідних значень T для створення файлу KML
    coordinates = []
    for i in range(n_rows):
        for j in range(n_columns):
            coordinates.append((Xint_new[i, j], Yint_new[i, j], Tskpov[i, j]))

# Генеруємо файл kml
filename = 'Data1.kml'
with open(filename, 'w') as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
    f.write('<kml xmlns="http://earth.google.com/kml/2.2">' + '\n')
    f.write(' <Document>' + '\n')
    f.write(' <name>MagField</name>' + '\n')
    f.write(' <open>1</open>' + '\n')
    f.write(' <Style id="magfield">' + '\n')
    f.write(' <LineStyle>' + '\n')
    f.write(' <color>7f00ffff</color>' + '\n')
    f.write(' <width>2</width>' + '\n')
    f.write(' </LineStyle>' + '\n')
    f.write(' <PolyStyle>' + '\n')
    f.write(' <color>7f00ffff</color>' + '\n')
    f.write(' </PolyStyle>' + '\n')

    # Записуємо координати точок та їх значення T у файл kml
    if n_points == n_rows * n_columns:
        coordinates = []
        for i in range(n_rows):
            for j in range(n_columns):
                coordinates.append((Xint_new[i, j], Yint_new[i, j], Tskpov[i, j]))

        f.write(' <Placemark>' + '\n')
        f.write(' <name>MagField</name>' + '\n')
        f.write(' <styleUrl>#magfield</styleUrl>' + '\n')
        f.write(' <Polygon>' + '\n')
        f.write(' <outerBoundaryIs>' + '\n')
        f.write(' <LinearRing>' + '\n')
        f.write(' <coordinates>' + '\n')
        for coord in coordinates:
            f.write('{},{},{}\n'.format(coord[0], coord[1], coord[2]))
        f.write(' </coordinates>' + '\n')
        f.write(' </LinearRing>' + '\n')
        f.write(' </outerBoundaryIs>' + '\n')
        f.write(' </Polygon>' + '\n')
        f.write(' </Placemark>' + '\n')
        f.write(' </Document>' + '\n')
        f.write('</kml>')
    else:
        print("Кількість точок на сітці та кількість точок магнітного поля відрізняються")
