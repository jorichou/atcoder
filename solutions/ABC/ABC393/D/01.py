N = int(input())
S = input()
ones = []

for i in range(N):
  if S[i] == "1":
    ones.append(i)

one = len(ones)
center = ones[one // 2]
length = list(map(lambda x : abs(x-center), ones))

for i in range(one//2+1, one):
  length[i] -= abs(i-(one//2))
for j in range(one//2):
  length[j] -= abs(one//2-j)

print(sum(length))