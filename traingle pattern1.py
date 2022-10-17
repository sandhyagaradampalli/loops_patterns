                    #               1
                    #            1  2 
                    #         1  2  3
                    #      1  2  3  4
                    #   1  2  3  4  5 

# i=0
# while i<5:
#     print("  "*(4-i),end=" ")
#     j=0
#     while j-1<i:
#         print(1*(j+1),end=" ")
#         j=j+1
#     print()
#     i=i+1



i=0
while i<=4:
    print("  "*(4-i),end=" ")
    j=1
    while j-1<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1