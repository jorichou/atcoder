N = int(input())

A = []

for i in range(N):
  temp = []
  for j in range(i+1):
    if j == 0 or j == i:
      temp.append(1)
    else:
      a = A[i-1][j-1] + A[i-1][j]
      temp.append(a)
  A.append(temp)
  
for a in A:
  print(*a, sep=" ")