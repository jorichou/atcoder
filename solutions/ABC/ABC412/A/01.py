N = int(input())
# tasks = []
counter = 0
for _ in range(N):
  task = list(map(int, input().split(' ')))
  # tasks.append(task)
  if (task[0] - task[1]) < 0:
    counter += 1
  
print(counter)