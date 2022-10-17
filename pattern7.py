
i=1
while i<=5: 
    j=1
    k=5
    while j<=5:
        if i==2:
            print(k-1,end=" ")
        elif i==3:
            print(k-2,end=" ")
        elif i==4:
            print(k-3,end=" ")
        elif i==5:
            print(k-4,end=" ")
        else:
            print(k,end=" ")
        k=k+5
        j=j+1
    i=i+1
    print()




# i=5
# while i-1>=0:
#     j=0
#     while j<i+20:
#         print(i+j,end=" ")
#         j=j+5
#     i=i-1
#     print()