data = ['1','2','3','2','1']
summary = dict()
for item in data:
    summary[item] = summary.get(item,0) + 1
print(summary)
