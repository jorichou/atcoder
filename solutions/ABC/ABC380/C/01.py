N, K = map(int, input().split(' '))
S = input()

segments = []
indexes = []
one_index = 0
counter = ["", 0]

counter[0] = S[0]
counter[1] = 1
for i in range(1, N):
  if counter[0] == S[i]:
    counter[1] += 1
  else:
    tmp_list = counter.copy()
    segments.append(tmp_list)
    if counter[0] == '1':
      indexes.append(one_index)
    counter[0] = S[i]
    counter[1] = 1
    one_index += 1
segments.append(counter)
indexes.append(one_index)
# print(segments)
# print(indexes)
tmp = segments.pop(indexes[K-1])
segments.insert(indexes[K-2] + 1, tmp)

for segment in segments:
  print(segment[0]*segment[1], end="")