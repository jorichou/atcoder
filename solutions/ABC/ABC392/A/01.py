A = list(map(int, input().split(' ')))

if A[0] * A[1] == A[2] or A[0] * A[2] == A[1] or A[1] * A[2] == A[0]:
  print('Yes')

else:
  print('No')