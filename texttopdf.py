from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial',size = 15)


pdf.cell(200,10, txt = 'python lover', ln= 1, align= 'C')

pdf.cell(200,10, txt = 'welcome to the python world', ln =2, align = 'C')

pdf.output(r'c:\users\dell\desktop\first.pdf')
