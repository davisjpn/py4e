fname=input("Enter file name:")
if len(fname)< 1:
    fname= "mbox-short.txt"
fh = open(fname)
count = 0
largest = None
counts=dict()
namelist=list()
for line in fh:
    line = line.rstrip()
    if line.startswith('From:'):
        countlist=list(line.split(" "))
        namelist.append(countlist[1])
        count = count + 1
for names in namelist:
    if names not in counts:
        counts[names] = 1
    else:
        counts[names] = counts[names] + 1
#keymax = max(counts,key=counts.get)
#print(max(counts.keys()),max(counts.values()))
for k,v in counts.items():
    if largest is None:
        email = k
        largest = v
    elif v > largest:
        email = k
        largest = v
print(email,largest)
    #print(k,v)
    #largest = counts[key]
#for names in namelist:
#    if names not in counts:
#        counts[names] = 1
#    else:
#        counts[names] = counts[names] + 1
#keymax = max(counts,key=counts.get)
#print(keymax,max(counts.values()))
