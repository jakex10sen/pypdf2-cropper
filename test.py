'''
found at http://stackoverflow.com/questions/457207/cropping-pages-of-a-pdf-file
'''
from PyPDF2 import PdfFileReader, PdfFileWriter

input1 = PdfFileReader(file("in/ch01.pdf", "rb"))
output = PdfFileWriter()

numPages = input1.getNumPages()
print "document has %s pages." % numPages

for i in range(numPages):
    page = input1.getPage(i)
    print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
    page.trimBox.lowerLeft = (0, 10)
    page.trimBox.upperRight = (612, 700)
    page.cropBox.lowerLeft = (0, 9)
    page.cropBox.upperRight = (612, 710)
    output.addPage(page)

outputStream = file("out/out.pdf", "wb")
output.write(outputStream)
outputStream.close()
