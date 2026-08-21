K, G, M = map(int, input().split(' '))
glass = 0
cup = 0

for k in range(K):
  if glass == G:
    glass = 0
    
  elif cup == 0:
    cup = M

  else:
    # グラスの残り容量がマグカップに入っている量より小さいとき
    if (G - glass) <= cup:
      cup -= (G - glass)
      glass = G

    else:
      glass += cup
      cup = 0

print(glass, cup, sep=' ')
  
