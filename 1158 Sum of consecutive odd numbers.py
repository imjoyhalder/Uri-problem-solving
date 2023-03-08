n = int(input())
for i in range (n):
    x,y = list(map(int,input().split()))
    s = 0
    while s<y:
        for i in range(x):
            if n%2!=0:
                print(i)
        s +=1