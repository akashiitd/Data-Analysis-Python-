"""Function to calculate how much he will earn"""

def theme_park(ride,people,l):
    s=0
    for i in range(ride):
        count=0
        new =[]
        for index,value in enumerate(l):
            if(count+value<=people):
                s = s+value
                count = count+value
            else:
                new = l[index:]+l[:index]               
                l=new
                break
    return s                    

    
    
    
    """Boiler Plate"""        
import sys
#num_list = ['0','1','2','3','4','5','6','7','8','9']    
mylist =[]
#""""D:\Users\703183779\Downloads\C-small-practice.in""""
f = open(r"D:\Users\703183779\Downloads\C-small-practice.in",mode="r")
for line in f:
    mylist.append(line)

mylist=[x.replace("\n","") for x in mylist]
mylist=mylist[1:]
inputlist =mylist[0::2]
group = mylist[1::2]
orig_stdout = sys.stdout
z = open(r'D:\Users\703183779\Documents\Mounika\theme_park_small.txt', 'w')
sys.stdout = z

for index,val in enumerate(group):
    #print("Case #{}: {}".format(index+1,last_name(int(val))))
    rp = inputlist[index].split(" ")
    g_p = [int(g) for g in group[index].split(" ")]
    
    
    print("Case #{}: {}".format(index+1,theme_park(int(rp[0]),int(rp[1]),g_p)))
sys.stdout = orig_stdout
z.close() 
