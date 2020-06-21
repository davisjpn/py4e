text = "X-DSPAM-Confidence:     0.8475"
n = text.find('0')
newtext = text[n:]
newtext = float(newtext)
print(newtext)
