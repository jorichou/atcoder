N = int(input())
strings = []

for _ in range(N):
  S = input()
  strings.append(S)
  
length = len(strings)

for i in range(0, length-1):
  for j in range(i+1, length):
    length1 = len(strings[i])
    length2 = len(strings[j])
    if length1 > length2:
      strings[i], strings[j] = strings[j], strings[i]
      
print(*strings, sep='')