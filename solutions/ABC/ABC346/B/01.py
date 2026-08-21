import sys

W, B = map(int, input().split(' '))
s = "wbwbwwbwbwbw"
w = 0
b = 0
start = 0
end = 0

s += s
if W + B > 12:
  repeat = (W + B) // 12
  for _ in range(repeat):
    s += s
  
end = W + B - 1
length_s = len(s)

for i in range(start, end+1):
  if s[i] == "w":
    w += 1
  elif s[i] == "b":
    b += 1

while end < length_s:
  if w == W and b == B:
    print("Yes")
    sys.exit()
  else:
    end += 1
    if end < length_s:
      if s[end] == "w":
        w += 1
      elif s[end] == "b":
        b += 1
      if s[start] == "w":
        w -= 1
      elif s[start] == "b":
        b -= 1
      start += 1
    else:
      break
    
print("No")