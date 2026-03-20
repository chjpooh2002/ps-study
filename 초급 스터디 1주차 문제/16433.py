N,R,C = map(int,input().split())
for i in range(N):
    for j in range(N):
        if (i%2)==(R%2):
            if (j%2)==(C%2):
                print("v",end="")
            else:
                print(".",end="")
        else:
            if (j%2)!=(C%2):
                print("v",end="")
            else:
                print(".",end="")
    print()
