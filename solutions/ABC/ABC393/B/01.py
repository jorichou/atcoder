S = input()
counter = 0
A = []
B = []
C = []

for n in range(len(S)):
  if S[n] == "A":
    A.append(n)
  elif S[n] == "B":
    B.append(n)
  elif S[n] == "C":
    C.append(n)
   
if A and B and C: 
  for j in B:
    minsA = list(map(lambda x : j-x, A))
    minsC = list(map(lambda x : x-j, C))
    for i in minsA:
      for k in minsC:
        if i == k and i > 0 and k > 0:
          counter += 1
  print(counter)
else:
  print(0)