H, W = map(int, input().split(' '))

grid_flag = [[0 for _ in range(W)] for _ in range(H)]
grid = []
cross_counter = [0 for _ in range(H if H < W else W)]

for i in range(H):
  grid.append(input())
  
def count_cross(char, h, w):
  if char == "#" and grid_flag[h-1][w-1] == 0:
    size = 0
    while char == "#":
      size += 1
      if (h + 1) >= H or (w + 1) >= W:
        break
      else:
        grid_flag[h][w] = 1
        h += 1
        w += 1
        char = grid[h][w]
    if size // 2 - 1 < 0:
      pass
    else:
      cross_counter[size // 2 - 1] += 1
  else:
    pass
  
for i in range(H):
  for j in range(W):
    count_cross(grid[i][j], i, j)
    
print(*cross_counter)