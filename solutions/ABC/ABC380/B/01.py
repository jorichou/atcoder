S = input()

counter = 0
original = []

for i in range(1, len(S)):
  if S[i] == "-":
    counter += 1
  elif S[i]  == "|":
    original.append(counter)
    counter = 0
  
print(*original)