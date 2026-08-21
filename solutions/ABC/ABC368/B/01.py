N = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
counter = 0


while True:
  positive_counter = 0
  A = sorted(A, reverse=True)
  A[0] -= 1
  A[1] -= 1
  for i in A:
    if i > 0:
      positive_counter += 1
      
  counter += 1
  if positive_counter <= 1:
    break
print(counter)