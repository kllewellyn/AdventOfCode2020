with open("input_03.txt", "r") as f:
    list = f.read().splitlines()
    count = 0
    index = 0
    iterator = iter(list)
    for line in iterator:
        line = line.strip()
        if line[index] is "#":
            count += 1
        index = (index + 1) % len(line)
        try:
            next(iterator)
        except StopIteration:
            continue
    print("There are: " + str(count) + " trees in your path")
