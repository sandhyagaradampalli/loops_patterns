                        #  A 
                        #  B C 
                        #  C D E 
                        #  D E F G 
                        #  E F G H I 




x=65
i=1
while i<6:
    j=1
    c=x
    while j<=i:
        print(chr(c),end=" ")
        j=j+1
        c=c+1
    i=i+1
    x=x+1
    print()