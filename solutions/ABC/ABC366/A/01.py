N, T, A = map(int, input().split(' '))

if (N - T - A) < abs(A - T):
  print("Yes")
  
else:
  print("No")