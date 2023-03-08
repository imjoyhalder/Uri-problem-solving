n = int(input())
for i in range(n):
    a = 0
    b = 1
    j = int(input())
    if j == 0:
        print(f"Fib({j}) = {j}")
    else:
        for k in range(1,j+1):
            c = a+b
            b = a
            a = c
        print(f"Fib({j}) = {c}")