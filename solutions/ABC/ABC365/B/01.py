N = int(input())
A = list(map(int, input().split(' ')))

A_sorted = sorted(A, reverse=True)
second_large = A_sorted[1]

print(A.index(second_large) + 1)