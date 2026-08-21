s = list(input())

length = len(s)

s.pop(length // 2)

result = ""
for string in s:
    result += string
print(result)