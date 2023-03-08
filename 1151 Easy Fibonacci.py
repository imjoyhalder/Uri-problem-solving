n = int(input())
count = 0
n1,n2 = 0,1
l = []
while count < n:
    l.append(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
print(*l)