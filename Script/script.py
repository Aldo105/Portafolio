import sys 
import pypdf

primero = sys.argv[1]
segundo = sys.argv[2]

pdf1 = pypdf.PdfFileReader('/' + primero +'.pdf')
pdf2 = pypdf.PdfFileReader('/' +  segundo +'.pdf')
unidos = pypdf.PdfWriter('/' + '.pdf')

for page in pdf1.pages:
    unidos.add_page(page)

for page in pdf2.pages:
    unidos.add_page(page)

with open("unidos.pdf", "wb") as salida:
    unidos.write(salida)
