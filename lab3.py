from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, portrait
from reportlab.lib.units import inch
from PyPDF2 import PdfFileMerger, PdfFileReader

from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import matplotlib.pyplot as plt

# Зчитуємо дані з файлу
data = np.loadtxt('data.txt')

# Розраховуємо кількість бінів за формулою Стерджеса
n_bins = int(np.ceil(1 + np.log2(len(data))))

# Обчислюємо інтервали для бінів
bin_edges = np.linspace(min(data), max(data), n_bins+1)

# Рахуємо гістограму
hist_counts, bins = np.histogram(data, bins=bin_edges)

# Відкриваємо файл для запису результатів
with open('histogram.txt', 'w') as f:
    # Записуємо заголовок
    f.write('Histogram results:\n\n')
    f.write(f'Minimum value: {min(data)}\n')
    f.write(f'Maximum value: {max(data)}\n')
    f.write(f'Number of bins: {n_bins}\n')
    f.write(f'Bin size: {bin_edges[1] - bin_edges[0]}\n\n')

    # Записуємо результати для кожного біна
    for i in range(n_bins):
        f.write(f'{bin_edges[i]} - {bin_edges[i+1]}: {hist_counts[i]}\n')

# Створюємо новий PDF файл з горизонтальним орієнтуванням
c = canvas.Canvas('histogram.pdf', pagesize=portrait(letter))

# # Графічне відображення гістограми та збереження у файл PDF
with PdfPages('histogram.pdf') as pdf:
    fig, ax = plt.subplots()
    ax.hist(data, bins=bin_edges, edgecolor='black')
    ax.set_title('Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    pdf.savefig(fig, bbox_inches='tight')
    # plt.show()

# Перетворення фігуру Matplotlib на зображення PNG і додавання її в PDF
png_filename = 'histogram.png'
fig.savefig(png_filename)
c.drawImage(png_filename, 0, 0, width=9*inch, height=6*inch )

# Додаємо результати до PDF файлу
with open('histogram.txt', 'r') as f:
    # text = f.read()
    # text = text.replace("\n", " ")
    # c.drawString(inch, 1*inch, text)

    lines = f.readlines()
    y = 750
    for line in lines:
        c.drawString(2.5*inch, y, line.strip())
        y -= 20

# Закриваємо файл і зберігаємо результати
c.save()


