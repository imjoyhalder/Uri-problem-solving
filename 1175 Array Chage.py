l = []
for i in range(20):
    n = int(input())
    l.append(n)
k = 0
for j in l[::-1]:
    print(f"N[{k}] = {j}")
    k = k+1
    