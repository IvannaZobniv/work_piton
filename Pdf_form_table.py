from fpdf import FPDF
import openpyxl

pdf = FPDF()
# pdf.add_page()
pdf.add_form('DejaVu','','DejaVuSansCondensed.ttf', uni=True)
pdf.add_form('DejaVul','','DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.set_form('DejaVul','',14)
# pdf.cell(200,10,txt="Welcome", ln=1, align = "C")
# pdf.image("1.jpg",10,20,100)

h=0
book = openpyxl.open("Learn.xlsx", read_only =True)
# sheet = book.active
sheet = book.worksheets[0]
# print(sheet["D7853"].value)
# print(sheet[6][2].value)
g=0
lefti =50
lefti2 =150

pdf.add_page()
pdf.line(5,5,5,290)
pdf.line(5,290,205,290)
pdf.line(205,290,205,5)
pdf.line(205,5,5,5)
for row in range(1,5):
    pdf.line(5,row*58,205,row*58)
pdf.line(105,5,105,290)
cou =0
for row in range(1,1001):

# for row in range(1,sheet.max_row):
#     print(row)
    g = g + 1
    cou=cou+1
    # numb = sheet[row][0].value
    word = sheet[row][1].value
    transcr = str(sheet[row][2].value)
    translate = str(sheet[row][3].value)

    leni = len(transcr)
    if g<6:
        ggg=g*58+5-15
        pdf.text(lefti-leni, int(ggg), txt=transcr)
    else:
        ggg = (g-5 )* 58 + 5 - 15
        pdf.text(lefti2 - leni, int(ggg), txt=transcr)

    leni = len(translate)
    if g<6:
        ggg = g * 58 + 5 - 10
        pdf.text(lefti - leni-3, int(ggg), txt=translate.title())
        pdf.set_text_color(139,69,19);
        pdf.text(10,int(ggg),txt=str(cou))
        pdf.set_text_color(0,0,0);
    else:
        ggg = (g - 5) * 58 + 5 - 10
        pdf.text(lefti2 - leni - 3, int(ggg), txt=translate.title())
        pdf.set_text_color(139, 69, 19);
        pdf.text(110, int(ggg), txt=str(cou))
        pdf.set_text_color(0, 0, 0);
    if g==10:
        g = 0
        h=h+1
        pdf.add_page()
        pdf.line(5, 5, 5, 290)
        pdf.line(5, 290, 205, 290)
        pdf.line(205, 290, 205, 5)
        pdf.line(205, 5, 5, 5)
        for row in range(1, 5):
            pdf.line(5, row * 58, 205, row * 58)
        pdf.line(105, 5, 105, 290)
        print(h)

pdf.output("simple_demo.pdf")




