Q = int(input())
cards = [0 for _ in range(100)]
for _ in range(Q):
  query = list(map(int, input().split(' ')))
  if query[0] == 1:
    cards.insert(0, query[1])
  else:
    output = cards.pop(0)
    print(output)
