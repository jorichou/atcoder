N, D = map(int, input().split(' '))
S = input()
number_of_cookie = 0

for box in S:
  if (box == "@"):
    number_of_cookie += 1
    
if D > number_of_cookie:
  print(len(S))
else:
  print(len(S) - (number_of_cookie - D))