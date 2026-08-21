N, M = map(int, input().split(' '))
B_original = list(map(int, input().split(' ')))
W_original = list(map(int, input().split(' ')))

B = sorted(B_original, reverse=True)
W = sorted(W_original, reverse=True)

black_count = 0
white_count = 0
black_total = 0
white_total = 0

# print(B)
# print(W)

for b in B:
  if black_count < M:
    if b < 0 and W[black_count] > 0 and abs(W[black_count]) >= abs(b):
      black_total += b
      black_count += 1
      continue
  if b >= 0:
    black_total += b
    black_count += 1
  elif b < 0 and black_count < 2:
    black_total += b
    black_count += 1
  else:
    break
  # print(black_total)
for w in W:
  if white_count >= black_count:
    break
  else:
    if w >= 0:
      white_total += w
      white_count += 1
    elif w < 0:
      break
  # print(white_total)

if black_total + white_total > 0:
  print(black_total + white_total)
else:
  print(0)