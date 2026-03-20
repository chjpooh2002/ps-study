while True:
    a = list(map(int,input().split()))
    if a[0]==0:
        break
    print(a[1],end = " ")
    for i in range(2,len(a)):
        if a[i] != a[i-1]:
            print(a[i],end = " ")
    print("$")