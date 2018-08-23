

def TempCov5():
    myfile='D://Users/703183779/Desktop/West Penn Allegheney.txt'
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
        if "dated effective as" in line:
            print(line)
            myline = line
            WrdList=myline.split()
            print(WrdList)
            for i in range(len(WrdList)):
                print(i, WrdList[i])
                
    for i in range(len(WrdList)):
        Str1 = str(WrdList[i])
        TempList=Str1.split(',')
        
        
    Str1 = WrdList[50]
            
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

def  TempCov1():
        myfile='D:\\Users\\703183779\\Desktop\\West Penn Allegheney.txt'
        fhand=open(myfile,'r')
        WrdList=list()
        TempList=list()
        AgrStartDate=''
        AgrStrtDate=''
	
        for line in fhand:
                line.rstrip()
                if "dated effective as" in line:
                        myline = line
                        WrdList=myline.split()
                for i in range(len(WrdList)):
                        Str1=str(WrdList[i])
                        TempList=Str1.split(',')
        Str1= WrdList[11]
        for i in range(len(WrdList)):
                j = i+1
                if WrdList[i]==Str1:
                        StartPos=i
                if WrdList[i]=='(d/b/a' and WrdList[j]=='Covidien),':
                        EndPos=i+1
        for i in range(len(WrdList)):
                if i>=StartPos and i<=EndPos:
                        Str2=WrdList[i]
                        Str2=str(Str2)
                        AgrStartDate=AgrStartDate +' '+Str2
        print(AgrStartDate)
        Str3=','
        Str3=str(Str3)
        for i in range(len(WrdList)):
                if WrdList[i] == Str1:
                        StartPos=i
                if WrdList[i]=="between":
                        EndPos=i-1
        for i in range(len(WrdList)):
                if i>=StartPos and i<=EndPos:
                        Str3=WrdList[i]
                        Str3=str(Str3)
                        AgrStrtDate = AgrStrtDate+''+Str3
        print(AgrStrtDate)
        print("\n")

TempCov1()
                       
                       


def TempCov3():
    myfile='D:\\Users\\703183779\\Desktop\\West Penn Allegheney.txt'
    fhand=open(myfile,'r')
    WrdList=list()
    AgrEndDt=''
    AgrEndDate=''
    

    for line in fhand:
        line.rstrip()
        if "\"Contt act Year\"" in line:
            print(line)
            myline=line
            WrdList=myline.split()
            print(WrdList)
            for i in range(len(WrdList)):
              #  print(i,WrdList[i])
    for i in range(len(WrdList)):
        Str1=str(WrdList[i])
        TempList=Str1.split(',')
    Str1=WrdList[4]

    for i in range(len(WrdList)):
        j=i+1
        k=j+1
        if WrdList[i]==Str1:
            StartPos=i+1
        if WrdList[i]=='during' and WrdList[j]=='the' and WrdList[k]=='term':
            EndPos=i-1
            print(EndPos)
    for i in range(len(WrdList)):
        if i>=StartPos and i<=EndPos:
            Str2=WrdList[i]
            Str2=str(Str2)
            AgrEndDt=AgrEndDt+' '+Str2
    print(AgrEndDt)

TempCov3()


def TempCov6():
    myfile='D://Users/703183779/Desktop/West Penn Allegheney.txt'
    fhand=open(myfile,'r')
    WrdList=list()
    TempList=list()
    PerOfRebate=''

    for line in fhand:
        if "Categories shall be" in line:
            print(line)
            myline = line
            WrdList=myline.split()
            print(WrdList)
            for i in range(len(WrdList)):
                         #print(i,WrdList[i])
    for i in range(len(WrdList)):
        Str1 = str(WrdList[i])
        TempList=Str1.split(',')

    Str1 = WrdList[58]
    for i in range(len(WrdList)):
        j=i+1
        k=j+1
        if WrdList[i]==Str1:
            StartPos=i+2
            print(StartPos)
        if WrdList[i]=="Purchases" and WrdList[j]=="of" and WrdList[k]=="Products":
            EndPos=i+2
    for i in range(len(WrdList)):
        if i>=StartPos and i<=EndPos:
            Str2=WrdList[i]
            Str2=str(Str2)
            PerOfRebate=PerOfRebate +' '+Str2
    print(PerOfRebate)
                            
            
TempCov6()

def TempCov4():
    myfile ='D://Users/703183779/Desktop/West Penn Allegheney.txt'
    fhand=open(myfile,'r')
    WrdList=()
    TempList=()
    TypeOfRebate=''

    for line in fhand:
        line.rstrip()
        if "Payment Terms" in line:
            print(line)
            myline = line
            WrdList=myline.split()
            print(WrdList)
            for i in range(len(WrdList)):
               # print(i,WrdList[i])
    for i in range(len(WrdList)):
        Str1=str(WrdList[i])
        TempList=Str1.split(',')

    Str1=WrdList[2]

    for i in range(len(WrdList)):
        j=i+1
        if WrdList[i]==Str1:
            StartPos=i+1
        if WrdList[i]=="Authorized" and WrdList[j]=="Distributor.,":
            Endpos=i+1
    for i in range(len(WrdList)):
        if i>=StartPos and i<=Endpos:
            Str2=WrdList[i]
            Str2=str(Str2)
            TypeOfRebate=TypeOfRebate+' '+Str2
    print(TypeOfRebate.rstrip(","))
            
TempCov4()



