                #   A
                #   B C 
                #   D E F 
                #   G H I J 



i=65
a=65
while i<=68:
    j=65
    while j<=i:
        print(chr(a),end=" ")
        j=j+1
        a=a+1
    i=i+1
    print()
        