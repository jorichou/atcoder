N = int(input())
K = []
dice_length = []
probability = []

for _ in range(N):
  tmp = list(map(int, input().split(' ')))
  dic = {}
  for n in tmp[1:]:
    if n in dic.keys():
      dic[n] += 1
    else:
      dic[n] = 1
  dice_length.append(tmp[0])
  K.append(dic)
  
for i in range(0, N-1):
  for j in range(i+1, N):
    dice1 = K[i]
    dice2 = K[j]
    dice1_length = dice_length[i]
    dice2_length = dice_length[j]
    
    denominator = dice1_length * dice2_length
    
    total = 0
    for m, n in dice1.items():
      if m in dice2.keys():
        total += n * dice2[m]
    
    probability.append(total/denominator)
    
print(max(probability))
    