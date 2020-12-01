

with open("input_01.txt", "r") as f:
    list = f.read().splitlines()
    for e in list:
        e.strip()

    iterator = iter(list)
    for firstNumber in iterator:
        secondIterator = iter(list)
        for secondNumber in secondIterator:
            difference = 2020 - int(firstNumber) - int(secondNumber)
            if int(difference) < 0:
                continue
            else:
                string = str(difference)
                if string in list:
                    print("First number: " + str(firstNumber) + " Second Number: " + str(secondNumber) + " Third number: " + str(difference))
                    answer = difference * int(firstNumber) * int(secondNumber)
                    print("The product of the 3 numbers is: " + str(answer))
                else:
                    continue
