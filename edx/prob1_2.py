s = 'azcbobobegghakl'
size = len(s)
count = 0
start = 0
end = 3
if size < 3:
    count += 0
elif size == 3:
    if s == 'bob':
        count += 1
else:
    while size >=3:
        if s[start:end]== 'bob':
            count +=1
        size -=1
        start +=1
        end +=1
print(count)
