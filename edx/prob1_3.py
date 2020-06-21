s = 'azcbobobegghakl'
size = len(s)
string1 = s[0]
largest = ""
for i in range(len(s)-1):
    if s[(i+1)] >= s[i]:
        string1 = string1 + s[(i+1)]
    else:
        if len(string1) > len(largest):
            largest = string1
            string1 = s[i+1]
        else:
            string1 = s[i+1]
if len(string1) > len(largest):
    largest = string1
print('Longest substring in alphabetical order is:', largest)
