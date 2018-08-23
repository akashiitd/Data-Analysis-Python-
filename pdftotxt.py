
def TempCov5():
    myfile='D://Users/703183779/Downloads/Text Mining NLP Projects/Textdocument/MaimonidesMedCtr_PRA_8-2015 to 7-16.txt'
    fhand= open(myfile,'r')
    namelist=list()
    WrdDic=dict()
    WrdList=list()
    TempList=list()
    ClientNames=''
    ClientNamesOnly=''
    
    cnt=1-2

    for line in fhand:
        line.rstrip()
        if "Start Date:" in line:
            print(line)
            myline = line
            WrdList=myline.split()
            print(WrdList)
            for i in range(len(WrdList)):
                print(i, WrdList[i])
                
    for i in range(len(WrdList)):
        Str1 = str(WrdList[i])
        TempList=Str1.split(',')
        
        
    Str1 = WrdList[5]
    print(Str1)        
    for i in range(len(WrdList)):
            j=i+1
            k=j+1
            if WrdList[i]==Str1:
                StartPos=i+2
            if WrdList[i]=='Schedule' and WrdList[j]=='I' and WrdList[k]=='attached':
                EndPos=i+2
    for i in range(len(WrdList)):
        if i>=StartPos and i<=EndPos:
            Str2=WrdList[i]
            Str2=str(Str2)
            ClientNames = ClientNames +' '+Str2
    print ("\n\n\n CAPTURED CLIENT_DETAILS FROM PDF \n\n")
    print (ClientNames)
    print ("\n\n\n \n\n")    

    Str3=','
    Str3=str(Str3)

    for i in range(len(WrdList)):
        if WrdList[i]==Str1:
                StartPos=i+2
        if WrdList[i]=='having':
            EndPos=i-1
    for i in range(len(WrdList)):
        if i>=StartPos and i<=EndPos:
            Str2=WrdList[i]
            Str2=str(Str2)
            ClientNamesOnly = ClientNamesOnly +' '+ Str2
    print ("\n\n\n CAPTURED CLIENT_NAME_ONLY FROM PDF \n\n")
    print (ClientNamesOnly)
    print ("\n\n\n \n\n")   

TempCov5()
