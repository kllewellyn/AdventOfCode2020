

with open("input_01.txt", "r") as f:
    list = f.read().splitlines()
    for e in list:
        e.strip()

    for element in list:
        difference = 2020 - int(element)
        string = str(difference)
        if string in list:
            answer = difference * int(element)
            print("The Solution is: " + str(answer))
        else:
            continue
