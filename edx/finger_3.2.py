s='1.23,2.4,3.123'
s = s.split(',')
sum = 0
for i in s:
    sum = sum + float(i)
print(sum)
