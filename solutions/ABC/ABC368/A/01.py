N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

A_front = A[:-K]
A_back = A[-K:]

print(*A_back, *A_front, sep=' ')