def isMatch(input):
    sum = 0
    for number in input:
        number = int(number.rstrip())
        sum += number
    return 10884537 - sum

with open("input_09.txt", "r") as f:
    textInput = f.read().splitlines()
    startIndex = 0
    endIndex = 25
    while endIndex < len(textInput):
        sublist = textInput[startIndex:endIndex]
        result = isMatch(sublist)
        if result == 0:
            sublist.sort()
            smallest = int(sublist[0].rstrip())
            largest = int(sublist[-1].rstrip())
            sumOfBoth = smallest + largest
            print("Sum of largest and smallest: " + str(sumOfBoth))
            break
        elif result > 0:
            endIndex += 1
        elif result < 0:
            startIndex += 1
