n, q = map(int, input().split(' '))
computer = {}
for version in range(1, n+1):
    computer[version] = 1
oldest = 1
for _ in range(q):
    total = 0
    x, y = map(int, input().split(' '))
    if x < oldest:
        print(0)
        continue
    for version in range(oldest, x+1):
        total += computer[version]
        computer.pop(version)
        oldest = x + 1

    computer[y] += total
    print(total)

