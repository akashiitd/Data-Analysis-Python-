def Product_Category():
     myfile='D:\\Users\\703183779\\Desktop\\West Penn Allegheney.txt'
     with open("West Penn Allegheney.txt") as openfile:
         for line in openfile:
            for part in line.split():
                if "Schedule="in part:
                    print (part)
Product_Category() 

     
    
