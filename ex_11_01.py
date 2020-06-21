import re
fname=input("Enter file name:")
if len(fname)< 1:
    fname= "regex_sum_411209.txt"
fh = open(fname)
numlist=list()
for line in fh:
        line = line.rstrip()
        stuff=re.findall('([0-9]+)',line)
        if len(stuff) ==0 : continue
        for item in stuff:
            value = int(item)
            numlist.append(value)
print(sum(numlist))
print('done')
