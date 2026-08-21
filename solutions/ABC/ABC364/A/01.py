n = int(input())
sweet_counter = 0

for i in range(n):
  s = input()
  if s == "sweet":
    sweet_counter += 1
    if sweet_counter == 2 and i != n - 1:
      print("No")
      break
  else:
    sweet_counter = 0
    
if i == n - 1:
  print("Yes")