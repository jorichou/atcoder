n = int(input())

def function(i):
    i = list(str(i))
    return sum(map(int, i))

a = 1
for i in range(n):
    if i == 0:
        a = function(a)
    else:
        a += function(a)

print(a)