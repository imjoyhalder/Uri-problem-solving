n = int(input())
count = 0
for i in range(1000):
    for j in range(n):
        count += 1
        print(f"N[{count}] = {j}")
    