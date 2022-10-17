#                             1 2 3 4 5 
#                             2 3 4 5 6
#                             3 4 5 6 7 
#                             4 5 6 7 8
#                             5 6 7 8 9
# 
# 
# 
# 
# 
i=1
while i<=5:
    j=1
    k=1
    while j<=5:
        if i==2:
            print(k+1,end=" ")
        elif(i==3):
            print(k+2,end=" ")
        elif(i==4):
            print(k+3,end=" ")
        elif(i==5):
            print(k+4,end=" ")
        else:
            print(k,end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()
    
    
  
i=5
while i>=1:
    j=i
    while j<=25:
        print(j,end=" ")
        j+=5
    i-=1
    print()
    
    
       
i=1
while i<=5:
    j=i
    while j<=5+i-1:
        print(j,end=" ")
        j+=1
    i+=1
    print()
    
    
    