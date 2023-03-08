a = int(input())
for i in range(a):
    n = int(input())
    f = False
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                f = True
                break
    if f: 
        print(n," nao eh primo")
    else: 
        print(n," eh primo")
