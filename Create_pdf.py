from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size =12)
pdf.cell(200,10,txt="Welcome", ln=1, align = "C")
pdf.image("1.jpg",10,20,100)
pdf.add_page()
pdf.output("simple_demo.pdf")