l = []
while True:
    n = int(input())
    if n<0:
        break
    else:
        l.append(n)

s = sum(l)
print(f"{s/len(l):.2f}")
