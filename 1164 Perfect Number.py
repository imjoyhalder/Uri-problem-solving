"""s = 0
for i in range(int(input())):
    a = int(input())
    c = int(a/2)
    for j in range(1,c+1):
        if a%j==0:
            s += j
    if s==a:
        print(a," eh perfeito")  
    else:
        print(a," nao eh perfeito")
"""
                 
n=int(input())
for i in range(n):
    a=int(input())
    c=int(a/2)
    d=0
    for b in range(1,c+1):
        if(a%b==0):
            d+=b
    if(d==a):
        print("{} eh perfeito".format(a))
    else:
        print("{} nao eh perfeito".format(a))

             