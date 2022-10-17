                #    A B C D E 
                #    F G H I 
                #    J K L 
                #    M N 
                #    O



i=65
a=65
while i<=69:
    j=69
    while j>=i:
        print(chr(a),end=" ")
        j=j-1
        a=a+1
    i=i+1
    print()
        