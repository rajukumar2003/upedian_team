# run pip install PyPDF2 before using
import PyPDF2
a=input("enter the number of pdfs you want to merge together(max 7): ")
if a=='1':
    print("INVALID!!!")
elif a=='2':
    b=input("enter the path to the first file with extension: ")
    c=input("enter the path to the second file with extension: ")
    d=input("what do you want to name the merged file: ")
    pdf1File = open(b, 'rb')
    pdf2File = open(c, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open(d+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
elif a=='3':
    b=input("enter the path to the first file with extension: ")
    c=input("enter the path to the second file with extension: ")
    d=input("enter the path to the third file with extension: ")
    e=input("what do you want to name the merged file: ")
    pdf1File = open(b, 'rb')
    pdf2File = open(c, 'rb')
    pdf3File = open(d, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf3Reader.numPages):
        pageObj = pdf3Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open(e+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    pdf3File.close()
elif a=='4':
    b=input("enter the path to the first file with extension: ")
    c=input("enter the path to the second file with extension: ")
    d=input("enter the path to the third file with extension: ")
    e=input("enter the path to the forth file with extension: ")
    f=input("what do you want to name the merged file: ")
    pdf1File = open(b, 'rb')
    pdf2File = open(c, 'rb')
    pdf3File = open(d, 'rb')
    pdf4File = open(e, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
    pdf4Reader = PyPDF2.PdfFileReader(pdf4File)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf3Reader.numPages):
        pageObj = pdf3Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf4Reader.numPages):
        pageObj = pdf4Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open(f+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    pdf3File.close()
    pdf4File.close()
elif a=='5':
    b=input("enter the path to the first file with extension: ")
    c=input("enter the path to the second file with extension: ")
    d=input("enter the path to the third file with extension: ")
    e=input("enter the path to the forth file with extension: ")
    f=input("enter the path to the fifth file with extension: ")
    g=input("what do you want to name the merged file: ")
    pdf1File = open(b, 'rb')
    pdf2File = open(c, 'rb')
    pdf3File = open(d, 'rb')
    pdf4File = open(e, 'rb')
    pdf5File = open(f, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
    pdf4Reader = PyPDF2.PdfFileReader(pdf4File)
    pdf5Reader = PyPDF2.PdfFileReader(pdf5File)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf3Reader.numPages):
        pageObj = pdf3Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf4Reader.numPages):
        pageObj = pdf4Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf5Reader.numPages):
        pageObj = pdf5Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open(g+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    pdf3File.close()
    pdf4File.close()
    pdf5File.close()
elif a=='6':
    b=input("enter the path to the first file with extension: ")
    c=input("enter the path to the second file with extension: ")
    d=input("enter the path to the third file with extension: ")
    e=input("enter the path to the forth file with extension: ")
    f=input("enter the path to the fifth file with extension: ")
    g=input("enter the path to the sixth file with extension: ")
    h=input("what do you want to name the merged file: ")
    pdf1File = open(b, 'rb')
    pdf2File = open(c, 'rb')
    pdf3File = open(d, 'rb')
    pdf4File = open(e, 'rb')
    pdf5File = open(f, 'rb')
    pdf6File = open(g, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
    pdf4Reader = PyPDF2.PdfFileReader(pdf4File)
    pdf5Reader = PyPDF2.PdfFileReader(pdf5File)
    pdf6Reader = PyPDF2.PdfFileReader(pdf6File)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf3Reader.numPages):
        pageObj = pdf3Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf4Reader.numPages):
        pageObj = pdf4Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf5Reader.numPages):
        pageObj = pdf5Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf6Reader.numPages):
        pageObj = pdf6Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open(h+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    pdf3File.close()
    pdf4File.close()
    pdf5File.close()
    pdf6File.close()
elif a=='7':
    b=input("enter the path to the first file with extension: ")
    c=input("enter the path to the second file with extension: ")
    d=input("enter the path to the third file with extension: ")
    e=input("enter the path to the forth file with extension: ")
    f=input("enter the path to the fifth file with extension: ")
    g=input("enter the path to the sixth file with extension: ")
    h=input("enter the path to the seventh file with extension: ")
    i=input("what do you want to name the merged file: ")
    pdf1File = open(b, 'rb')
    pdf2File = open(c, 'rb')
    pdf3File = open(d, 'rb')
    pdf4File = open(e, 'rb')
    pdf5File = open(f, 'rb')
    pdf6File = open(g, 'rb')
    pdf7File = open(h, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
    pdf4Reader = PyPDF2.PdfFileReader(pdf4File)
    pdf5Reader = PyPDF2.PdfFileReader(pdf5File)
    pdf6Reader = PyPDF2.PdfFileReader(pdf6File)
    pdf7Reader = PyPDF2.PdfFileReader(pdf7File)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf3Reader.numPages):
        pageObj = pdf3Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf4Reader.numPages):
        pageObj = pdf4Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf5Reader.numPages):
        pageObj = pdf5Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf6Reader.numPages):
        pageObj = pdf6Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf7Reader.numPages):
        pageObj = pdf7Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open(i+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    pdf3File.close()
    pdf4File.close()
    pdf5File.close()
    pdf6File.close()
    pdf7File.close()
else:
    print("INVALID!!!")