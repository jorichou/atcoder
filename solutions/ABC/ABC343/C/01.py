import numpy as np

N = int(input())
N_root = N ** (1/3)
x = int(np.round(N_root))
if x**3 > N:
  x -= 1

while True:
  K = x**3
  tmp1 = str(K)
  tmp2 = str(K)[::-1]
  # print(tmp1, tmp2, sep=" ")
  if tmp1 == tmp2:
    break
  else:
    x -= 1

    
print(K)