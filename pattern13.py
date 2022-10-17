                    #   1
                    #   3 5
                    #   5 7 9
                    #   7 9 11 13
                    #   9 11 13 15 17





i=0
a=1
while i<=8:
    j=0
    while j<=i:
        print(a+j,end=" ")
        j=j+2
    i=i+2
    a=a+2
    print()
        