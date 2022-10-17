                    #   1
                    #   B B 
                    #   3 3 3
                    #   D D D D
                    #   5 5 5 5 5




n=int(input())
i=1
k=ord("A")
while i<=n:
    j=1
    while j<=i:
        if(i%2==0):
            print(chr(k),end=" ")
        else:
            print(i,end=" ")
        j=j+1
    i=i+1
    k=k+1
    print()