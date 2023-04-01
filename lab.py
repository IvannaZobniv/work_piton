import numpy as np
import matplotlib.pyplot as plt

# Вхідні параметри
len_prof = 50
det = 500
del_prof = 0.5
zmeya = 1
trend = 1

D = 349057  # Довгота
S = 5570360  # Широта

# Функція обробки та повернення даних магнітного поля
def process_magnetic_data(file_path):
    min_val = 10000000
    max_val = 10
    count = -1
    a1, b1, c1 = [], [], []

    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if "Поле" in line:
                count += 1
                longitude = D + count * del_prof
                mag_data, y, z = [], [], []

                # Читаємо точки даних магнітного поля
                while True:
                    line = f.readline().strip()
                    if not line:
                        break
                    mag_val = float(line)
                    min_val = min(min_val, mag_val)
                    max_val = max(max_val, mag_val)
                    mag_data.append(mag_val)

                # Обробка даних магнітного поля
                for i, mag_val in enumerate(mag_data[:-1]):
                    y.append(i)
                    z.append(mag_data[-2 - i] if count % 2 and zmeya else mag_val)

                delta = (len(mag_data) - 1) / det
                xi, yi, zi = [], [], []

                for i in range(det):
                    xi.append(longitude)
                    yi.append(S + i * len_prof / det)
                    zi.append(np.interp((i - 1) * delta, y, z))

                if trend:
                    mean = np.mean(zi)
                    zi = [val - mean for val in zi]

                a1.append(yi)
                b1.append(xi)
                c1.append(zi)

    return a1, b1, c1, min_val, max_val


# Обробка даних магнітного поля та запис вихідних даних у файл CSV
a1, b1, c1, min_val, max_val = process_magnetic_data("pkm.txt")

with open("pkm_out.csv", "w") as f_out:
    for xi, yi, zi in zip(b1, a1, c1):
        for x, y, z in zip(xi, yi, zi):
            f_out.write(f"{x};{y};{z}\n")

# Побудова даних магнітного поля за допомогою контурної діаграми із заливкою
plt.style.use('_mpl-gallery-nogrid')
levels = np.linspace(-10, 10, 50) # min_val, max_val,діапазон між цими значеннями
print(min_val, max_val)

fig, ax = plt.subplots()
contourf = ax.contourf(b1, a1, c1, levels=levels,cmap='RdBu')  #  кольорова гама
cbar = plt.colorbar(contourf, shrink=1, pad=0.02) #розмір та відступ кольорової шкали
cbar.ax.tick_params(labelsize=15, pad=0.02)  # розмір та відступ значень кольорової шкали
fig.suptitle('Magnetic field values', fontsize=20, y=0.98) # підпис графіка, його розмір та розташування по осі y

# Позначки x і y координат
xticks = np.arange(D, D + len_prof * (len(b1) + 1), len_prof)
yticks = np.arange(S, S + len_prof, len_prof / 10)
# ax.set_xticks(xticks)
ax.set_yticks(yticks)
fontsize = 15
ax.set_xticklabels([f"{x:.0f}" for x in xticks], fontsize=fontsize)
ax.set_yticklabels([f"{y:.0f}" for y in yticks], fontsize=fontsize)
fig.set_size_inches(10, 10)  #  ширина та висота листа відображення

plt.subplots_adjust(left=0.10,  bottom=0.05, top=0.95) # відступ графіка на листі зправа,знизу,зверху
plt.show()