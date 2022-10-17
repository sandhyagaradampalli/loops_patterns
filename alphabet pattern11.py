                    #  E D C B A 
                    #  D C B A 
                    #  C B A 
                    #  B A 
                    #  A




x=69
i=1
while i<6:
    j=5
    c=x
    while j>=i:
        print(chr(c),end=" ")
        j=j-1
        c=c-1
    i=i+1
    x=x-1
    print()