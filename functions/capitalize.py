s = 'happy birthday'
size = len(s)
count = 0
news = ""
test = ""
for i in s:
    if count == 0:
        if i == " ":
            news = news + i
        elif i.isalpha() == True:
            news = news + i.upper()
    else:
        if i == " ":
            news = news + i
        elif i.isalpha() == True and test == " ":
            news = news + i.upper()
        else:
            news = news + i
    count += 1
    test = i
print(len(s))
print(s)
print(news)
