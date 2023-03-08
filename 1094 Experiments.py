n = int(input())
for i in range(n):
    x,y = (input().split())
    a = int(x)
    if a==True and y == "R":
        global l
        l = []
        l.append(a)
        print(l)
    elif a == True and y == "C":
        global k
        k = []
        k.append(a)
    elif a == True and y == "R":
        global m
        m =[]
        m.append(a)
    