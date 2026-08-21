N, X, Y = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
a_total = 0
b_total = 0

A.sort(reverse=True)
B.sort(reverse=True)

for i in range(N):
  a_total += A[i]
  b_total += B[i]
  if a_total > X or b_total > Y:
    print(i + 1)
    break
  
if a_total <= X and b_total <= Y:
  print(N)