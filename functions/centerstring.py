import os
def align(s,w):
    if len(s) > w:
        return s
    else:
        spaces = (w - len(s))//2
        result = " " * spaces + s
        return result


w = os.get_terminal_size().columns
s = input('Please input a string:')
print(len(s))
print (align(s,w))

#print('hello world'.center(width))
#print("{:>12}".format('hello world'))
#align(s,w)
