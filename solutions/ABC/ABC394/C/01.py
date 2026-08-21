S = list(input())
index = 0

while index < len(S)-1:
  s = S[index] + S[index+1]
  if s == "WA":
    S[index] = "A"
    S[index+1] = "C"
    if index > 0:
      index -= 1
  else:
    index += 1
    
print(*S, sep="")