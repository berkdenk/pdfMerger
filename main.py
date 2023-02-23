from PyPDF2 import PdfWriter

merge=PdfWriter()
firstpdf=open("bos.pdf","rb")
secondpdf=open("bos2.pdf","rb")

merge.append(firstpdf)
merge.append(secondpdf)

merge.write("merged.pdf")