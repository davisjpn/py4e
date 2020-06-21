s = "I love flowers! Love pizza! and ice cream?"
news = ""
for char in range(0,len(s)):
    if char == 0:
        if s[char].isalpha():
            news = news + s[char].upper()
        else:
            news = news + s[char]
    else:
        if s[char]== "i" and s[char-1]== " " and s[char+1]== " ":
            news = news + s[char].upper()
        else:
            news = news + s[char]
position = 0
while position < len(news):
    if news[position] == "." or news[position] == "!" or news[position] == "?":
        position = position + 1
        while position < len(news) and news[position] == " ":
            position = position + 1
        if position < len(news):
            news = news[0:position]+ news[position].upper()+ news[position+1:len(news)]
    position = position + 1
print(s)
print(news)
