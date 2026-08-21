N, M = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

output = []

for i in range(1, N+1, 1):
  if i not in A:
    output.append(i)
    
print(len(output))
print(*output)