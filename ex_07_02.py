fname = input("Enter file name:")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    llength = len(line)
    conflevel = line[llength-6+1:26]
    conflevel = float(conflevel)
    total = total + conflevel
print('Average spam confidence:', total/count)
