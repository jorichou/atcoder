N = int(input())
P = list(map(int, input().split(' ')))
Q = list(map(int, input().split(' ')))

S = [0 for _ in range(N)]
index = 0

for i in Q:
  seen = P[index]
  S[i - 1] = Q[seen - 1]
  index += 1
  
print(*S)