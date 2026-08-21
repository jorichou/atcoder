N, M = map(int, input().split(' '))
V = {}
counter = 0
for m in range(M):
  hen = sorted(list(map(int, input().split(' '))))
  if hen[0] == hen[1]:
    counter += 1
  else:
    if hen[0] not in V.keys():
      V[hen[0]] = [hen[1]]
    elif hen[1] in V[hen[0]]:
      counter += 1
    else:
      V[hen[0]].append(hen[1])

# print(V)
print(counter)
    