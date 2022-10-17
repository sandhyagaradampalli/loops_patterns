                #    2
                #    4 6
                #    8 10 12
                #    14 16 18 20
                #    22 24 26 28 30


i=2
a=2
while i<=6:
    j=2
    while j<=i:
        print(a,end=" ")
        j=j+1
        a=a+2
    i=i+1
    print()