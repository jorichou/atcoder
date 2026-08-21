n, k = map(int, input().split(' '))
s = input()

part_dic = {}
max_counter = 1

# def search_part(part, e, part_len, e_len):
#     for i in range(e_len-part_len):
#         if part == e[i:i+k]:
max_list = []

for i in range(n-k+1):
    part_s = s[i:i+k]
    if part_s not in part_dic.keys():
        part_dic[part_s] = 1
    else:
        part_dic[part_s] += 1

max_counter = max(part_dic.values())

for string in part_dic.keys():
    if part_dic[string] == max_counter:
        max_list.append(string)

print(max_counter)
print(*list(sorted(max_list)))