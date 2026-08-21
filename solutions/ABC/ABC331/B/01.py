N, S, M, L = map(int, input().split(' '))
A = []

for s in range(100):
  for m in range(100):
    for l in range(100):
      n = 6*s + 8*m + 12*l
      amount = S*s + M*m + L*l
      if n >= N:
        A.append(amount)

      
print(min(A))