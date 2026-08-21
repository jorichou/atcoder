import sys

S = input()
strlog = []

if len(S) % 2 == 1:
  print("No")
  sys.exit()
else:
  if S[0] != S[1]:
      print("No")
      sys.exit()
      
  else:
    # 1文字目と２文字目
    strlog.append(S[0])
    
    for i in range(2, len(S) // 2 + 1):
      if S[2 * i -2] != S[2 * i - 1]:
        print("No")
        sys.exit()
      else:
        for string in strlog:
          if S[2 * i -2] == string:
            print("No")
            sys.exit()
        strlog.append(S[2 * i -2])
      
print("Yes")