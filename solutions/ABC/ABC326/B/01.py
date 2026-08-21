N = int(input())

while True:
  hundred = N // 100
  teen = (N - 100 * hundred) // 10 
  one = N - 100 * hundred - 10 * teen
  if hundred * teen == one:
    break
  else:
    N += 1
    
print(N)