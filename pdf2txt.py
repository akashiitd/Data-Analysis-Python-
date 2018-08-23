def Try11():
    import PyPDF2
    content = ""
    POC=''
    SEC=''
    PO=''
    path = 'D://Users/703183779/Downloads/Text Mining NLP Projects/healthaid.pdf'
    pdf_file = open(path, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for i in range(0, read_pdf.getNumPages()):
            # Extract text from page and add to content
            content += read_pdf.getPage(i).extractText() + "\n"
            # Collapse whitespace
            content = " ".join(content.replace(u"\xa0", " ").strip().split())

    LowContent = content.lower()
    print(LowContent)
    
    print ("\n\n\n WORDS SPLITTED HERE BELOW\n\n")
    WrdList = LowContent.split()
    print (WrdList)
    
    for i in range(len(WrdList)):
        print (i,WrdList[i])

    CodeStr ="code"
    POCStr = "orderpoc"
    SECStr = "ordersec"
    POStr = "invoice"

    print ("\n\n\n CAPTURED VALUES FROM PDF BELOW\n\n")

    for i in range(len(WrdList)):
        if not WrdList[i].startswith(POCStr):
            continue
        else:
            #i=i+1
            POClong=WrdList[i]
            POC=POClong[5:]
    print ("POC is: ",POC)
    #print (POClong)

    for i in range(len(WrdList)):
        if not WrdList[i].startswith(SECStr):
            continue
        else:
            #i=i+1
            SEClong=WrdList[i]
            SEC=SEClong[5:15]
    print ("SEC is: ",SEC)
    #print (SEClong)

    for i in range(len(WrdList)):
        if not WrdList[i].startswith(POStr):
            continue
        else:
            #i=i+1
            POlong=WrdList[i]
            POSub=POlong.split('project')
            POlong2=POSub[0]
            PO=POlong2[7:]
    print ("PO is: ",PO)
    #print (POlong)

    for i in range(len(WrdList)):
        if not WrdList[i].startswith(CodeStr):
            continue
        else:
            i=i+1
            CODElong=WrdList[i]
            CODE=CODElong[0]
    print ("CODE is: ",CODE)
    #print (CODElong)

    f = open('example.csv','w')
    f.write(POC)
    f.write('\n ')
    f.write(SEC)
    f.write(' \n')
    f.write(PO)
    f.write(' \n')
    f.write(CODE)
    f.write(' \n')
    f.close()
    
Try11()
