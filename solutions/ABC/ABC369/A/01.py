A, B = map(int, input().split(' '))

if abs(A - B) == 0:
  print('1')
else:
  if abs(A - B) % 2 == 0:
    print('3')
  elif abs(A - B) % 2 == 1:
    print('2')