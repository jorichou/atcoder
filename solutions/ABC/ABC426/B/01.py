s = list(input())
s_dic = {}

for string in s:
    if string not in s_dic.keys():
        s_dic[string] = 1
    else:
        s_dic[string] += 1

for string in s_dic.keys():
    if s_dic[string] == 1:
        print(string)