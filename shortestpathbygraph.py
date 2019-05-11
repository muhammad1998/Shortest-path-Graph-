from numpy import*
import math
import random
vertex=9
def mindistance(value,check):
    min = 99
    index = -1
    for i in range(0,vertex):
        if(check[i]==False and value[i]<=min):
            min=value[i]
            index=i
    return index
def shortestpath(arr2,num):
    value=[]
    check=[]
    for i in range(0,vertex):
        value.append([i])
        check.append([i])
    for i in range(0,vertex):
        value[i]=999
        check[i] = False
    value[num]=0
    for i in range(0,vertex-1):
        check1 = mindistance(value,check)
        check[check1] = True
        for j in range(0,vertex):
            if(arr2[check1,j]!=0 and value[check1]!=99 and value[check1]+arr2[check1,j]< value[j]):
                value[j]=value[check1]+arr2[check1,j]
    
    print("Vertex Distance "+ "From Source")
    for i in range(0,vertex):
        print("%-17s %-17s"%(i,value[i]))
    
  
num5 = int(input("Enter Maximun matrix size"))
val=num5*num5
sqq=math.sqrt(val)
p=int(sqq)
print(sqq)
t=val-p
print(val-p)
print(val-p)
abc=int(sqq)-1
arr1=[]

for a in range(0,val):
        arr1.append([])
        
for j in range(0,val):
        for k in range(0,val):
                arr1[j].append(k)
                arr1[j][k]=0
print(arr1)
wa=0
xyz=0
for i in range(0,val):
    if(i==abc):
        if(i!=val):
            print(abc)
            abc=abc+p
            if(abc<=val):
                
                arr1[i][abc]=1
            
        else:
            arr[i][val]=0
            for w in range(1,p):
            
                arr1[i-w][i-wa]=1
                wa=wa+1;
            
    elif(i!=abc and i<val-(p)):
        arr1[i][i+1]=1
        arr1[i][i+p]=1
        arr1[i][i+p+1]=1
    for h in range(0,val):
        if(h==val-1):
            arr1[val-1][h]=0
        elif(h==t):
            arr1[t][t+1]=1
            t=t+1
        
        
       

    
        
    
                    

print(arr1[2][0])
print(arr1)
        
arr2 = array([[0,1,0,0,0,0,0,1,0],[1,0,1,0,0,0,0,1,0],[0,1,0,1,0,1,0,0,1],[0,0,1,0,1,1,0,0,0],[0,0,0,1,0,1,0,0,0],[0,0,1,1,1,0,1,0,0],[0,0,0,0,0,1,0,1,1],[1,1,0,0,0,0,1,0,1],[0,0,1,0,0,0,1,1,0]])

for i in range(0,vertex):
    for j in range(0,vertex):
        if(arr2[i,j]==1):
            value=random.randint(1,15)
            arr2[i,j]=value
shortestpath(arr1,2)
print(arr2)


