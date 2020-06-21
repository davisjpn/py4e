fname=input("Enter file name:")
if len(fname)< 1:
    fname= "mbox-short.txt"
fh = open(fname)
count = 0
hours=dict()
hourlist=list()
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        colonpos=line.find(':')
        hr_pos=line[colonpos-2:colonpos]
        hourlist.append(hr_pos)
for item in hourlist:
    hours[item] = hours.get(item,0) + 1
for k,v in sorted (hours.items()):
    print(k,v)
        
