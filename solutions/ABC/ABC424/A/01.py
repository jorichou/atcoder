V = list(map(int, input().split(' ')))

V = list(sorted(V))
if V[0] == V[1] or V[1] == V[2]:
  print('Yes')
else:
  print('No')