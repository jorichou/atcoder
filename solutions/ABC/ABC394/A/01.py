S = input()
twos = []

for s in S:
  if s == "2":
    twos.append(s)
    
print(*twos, sep='')