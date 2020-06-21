def readAndTotal():
    line = (input('Please enter integer(blank to quit):'))
    if line == " ":
        return 0
    else:
        return float(line) + readAndTotal()
def main():
    total = readAndTotal()
    print('The total of all those values is ', total)

main()
