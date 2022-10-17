                    # 1
                    # 2 3
                    # 3 4 5
                    # 4 5 6 7
                    # 5 6 7 8 9



i=0
a=1
while i<=4:
    j=0
    while j<=i:
        print(a+j,end=" ")
        j=j+1
    i=i+1
    a=a+1
    print()
        