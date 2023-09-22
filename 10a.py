from PyPDF2 import PdfWriter,PdfReader

num1=int(input("enter the page no of pdf1"))
num2=int(input("enter the page no of pdf2"))
pdf1="C:\\Users\\anubh\\Downloads\\original_1687433780_1._Probability.pdf"
pdf2="C:\\Users\\anubh\\Downloads\\original_1687433780_1._Probability.pdf"

pdf_writer=PdfWriter()
pdf_reader=PdfReader(pdf1)
page=pdf_reader.pages[num1-1]
pdf_writer.add_page(page)

pdf_reader=PdfReader(pdf2)
page=pdf_reader.pages[num2-1]
pdf_writer.add_page(page)

with open('o.pdf','wb') as output:
    pdf_writer.write(output)
print("combine sucesfully")
