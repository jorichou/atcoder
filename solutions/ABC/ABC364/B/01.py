H, W = map(int, input().split(' '))
Si, Sj = map(int, input().split(' '))
C = []
for height in range(H):
  c = input()
  C.append(list(c))
X = input()

Si -= 1
Sj -= 1

def left(i, j, c):
  if j - 1 >= 0:
    if c[i][j - 1] == '.':
      j -= 1
      return j
    else:
      return j
      
  else:
    return j
    
def right(i, j, c):
  if j + 1 <= W - 1:
    if c[i][j + 1] == '.':
      j += 1
      return j
    else:
      return j
      
  else:
    return j
    
def up(i, j, c):
  if i - 1 >= 0:
    if c[i - 1][j] == '.':
      i -= 1 
      return i
    else:
      return i
      
  else:
    return i
    
def down(i, j, c):
  if i + 1 <= H - 1:
    if c[i + 1][j] == '.':
      i += 1  
      return i
    else:
      return i
  else:
    return i

   
for s in X:
  if s == "L":
    Sj = left(Si, Sj, C)
  elif s == "R":
    Sj = right(Si, Sj, C)
  elif s == "U":
    Si = up(Si, Sj, C)
  elif s == "D":
    Si = down(Si, Sj, C)
    
Si += 1
Sj += 1

print(Si, Sj, sep=' ')