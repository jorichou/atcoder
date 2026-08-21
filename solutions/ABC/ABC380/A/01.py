N = input()
counter = [0, 0, 0]

for i in range(len(N)):
  if N[i] == '1':
    counter[0] += 1
  elif N[i] == "2":
    counter[1] += 1
  elif N[i] == "3":
    counter[2] += 1
    
if counter[0] == 1 and counter[1] == 2 and counter[2] == 3:
  print("Yes")
else:
  print("No")
