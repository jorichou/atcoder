x, y = input().split(' ')
os_list = ["Ocelot", "Serval", "Lynx"]

x_index = os_list.index(x)
y_index = os_list.index(y)

if x_index >= y_index:
  print("Yes")
else:
  print("No")