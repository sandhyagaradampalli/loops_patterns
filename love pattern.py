r=6
c=7
i=1
while i<=r:
    j=1
    while j<=c:
        if i==1 and j==2 or i==1 and j==3 or i==1 and j==5 or i==1 and j==6 or i==2 and j==1 or i==2 and j==4 or i==2 and j==7 or i==3 and j==1 or i==3 and j==7 or i==4 and j==2 or i==4 and j==6 or i==5 and j==3 or i==5 and j==5 or i==6 and j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()