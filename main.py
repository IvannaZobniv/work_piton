from fpdf import FPDF
pdf = FPDF()
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

f = open('data.txt')
List_data = []
List_count = 0

# Читаємо з файла
while True:
    Zn = f.readline()
    if not Zn:
        break
    List_data.append(float(Zn))
    List_count = List_count + 1
f.close
diap = input("Вкажіть кількість діапазонів - ")
mx=max(List_data)
mn=min(List_data)
delta = (mx-mn)/int(diap)
print(List_data)
print(List_count)
print(mx, mn, delta)

pdf.add_page()
#pdf.set_text_color(139, 69, 19);
textl="Максимальне значення = "+str(mx)
pdf.text(10, 10, txt=textl)
textl="Мінімальне значення = "+str(mn)
pdf.text(10, 20, txt=textl)
textl="Delta = "+str(delta)
pdf.text(10, 30, txt=textl)
pdf.line(10, 35, 200, 35)

pdf.output("test.pdf")