                    # 1
                    # 1 2
                    # 3 5 8
                    # 13 21 34 55
                    # 89 144 233 377 610




n=int(input())
n1=0
n2=1
r=n1+n2
i=0
while i<n:
    j=0
    while j<=i:
        print(str(r)+" ",end="")
        r=n1+n2
        n1=n2
        n2=r
        j=j+1
    i=i+1
    print()

