my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = []
index = 0
while index < len(my_list):
    if my_list[index] < 0:
         break
    a.append(my_list[index])
    index += 1
for i in a:
    print(i)
