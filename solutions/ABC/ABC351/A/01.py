A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A_total = sum(A)
B_total = sum(B)

print(A_total - B_total + 1)