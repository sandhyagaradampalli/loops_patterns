            #            1
            #         2  1
            #       3 2  1
            #     4 3 2  1
            #   5 4 3 2  1



n=int(input())
i=1
while i<=n:
    k=n-1
    while k>=i:
        print(" ",end=" ")
        k=k-1
    j=i
    while j>=1:
        print(j,end=" ")
        j=j-1
    i=i+1
    print()
        
        
        
    

