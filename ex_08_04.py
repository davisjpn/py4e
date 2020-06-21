fhand = open('romeo.txt')
first_list = list()
second_list = list()
for line in fhand:
    line = line.rstrip()
    wlist= list(line.split(" "))
    for item in wlist:
        first_list.append(item)
first_list.sort()
for x in first_list:
    if x not in second_list:
        second_list.append(x)
print(second_list)
print(len(first_list))
print(len(second_list))
print('done')
