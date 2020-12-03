with open("input_03.txt", "r") as f:
    list = f.read().splitlines()
    count = 0
    index = 0
    for line in list:
        line = line.strip()
        if line[index] is "#":
            count += 1
        index = (index + 3) % len(line)
    print("There are: " + str(count) + " trees in your path")
