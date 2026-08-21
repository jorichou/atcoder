K, G, M = map(int, input().split(' '))

g, m = 0, 0 # 入っている水の量

for _ in range(K):
  if G == g and m >= 0 and m <= M:
    g = 0
  elif g >= 0 and g < G and m == 0:
    m = M
  elif g >= 0 and g < G and m >= 0 and m <= M:
    if G-g >= m: # グラスにすべての水が入るとき
      g += m
      m = 0
    else: # グラスにすべての水が入らないとき
      tmp = G - g
      g = G
      m -= tmp
      
print(g, m, sep=' ')
      

