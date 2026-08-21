N, D = map(int, input().split(' '))
S = list(input())
number_of_cookie = 0
index = len(S) - 1

while True:
  if S[index] == "@":
    S[index] = "."
    D -= 1
    
  if D == 0 or "@" not in S:
    break
  index -= 1
  
print(*S, sep="")