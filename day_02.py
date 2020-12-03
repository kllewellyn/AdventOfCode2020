with open("input_02.txt", "r") as f:
    list = f.read().splitlines()
    count = 0
    for line in list:
        beforeColon = line.split(":")[0]
        password = line.split(":")[1].strip()

        numbers = beforeColon.split()[0]

        lowerBound = numbers.split("-")[0].strip()
        upperBound = numbers.split("-")[1].strip()

        character = beforeColon.split()[1].strip()

        characterCount = password.count(character)

        if characterCount >= int(lowerBound) and characterCount <= int(upperBound):
            count += 1
    print("The number of valid passwords is: " + str(count))
