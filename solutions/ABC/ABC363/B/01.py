N, T, P = map(int, input().split(' '))
L = list(map(int, input().split(' ')))
day = 0


while True:
  counter = 0
  for i in L:
    if (i >= T):
      counter += 1
    
  if counter < P:
    L = [i + 1 for i in L]
    day += 1
    
  else:
    break
    
print(day)