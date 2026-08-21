import sys

N = int(input())
S = input()

if N == 1 and S[0] == "/":
  print("Yes")
elif N % 2 == 0:
  print("No")
else:
  for i in range((N + 1) // 2 - 1):
    if S[i] != '1':
      print("No")
      sys.exit()
      
  if S[(N + 1) // 2 - 1] != "/":
    print("No")
    sys.exit()
    
  for i in range((N + 1) // 2, N):
    if S[i] != '2':
      print("No")
      sys.exit()
    
  print("Yes")
