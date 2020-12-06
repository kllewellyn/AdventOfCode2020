with open("input_05.txt", "r") as f:
    list = f.read().splitlines()
    maxSeatNumber = 0

    all = []
    print("elements in list: " + str(len(list)))
    for seat in list:
        minRow = 0
        maxRow = 127
        characters = iter(seat)
        while ((maxRow - minRow) != 1):
            try:
                current = next(characters)
            except StopIteration:
                continue
            if current == "F":
                maxRow = ((maxRow - minRow) // 2) + minRow
            elif current == "B":
                minRow = maxRow - (maxRow - minRow) // 2
        try:
            current = next(characters)
        except StopIteration:
            continue

        finalRow = maxRow if current == "B" else minRow
        minColumn = 0
        maxColumn = 7

        while (maxColumn - minColumn) != 1:
            try:
                current = next(characters)
            except StopIteration:
                continue
            if current == "L":
                maxColumn =  ((maxColumn - minColumn) // 2) + minColumn

            elif current == "R":
                minColumn = maxColumn - (maxColumn - minColumn) // 2

        try:
            current = next(characters)
        except StopIteration:
            continue

        finalColumn = maxColumn if current == "R" else minColumn

        seatId = (finalRow * 8) + finalColumn

        all.append(seatId)

        if seatId > maxSeatNumber:
            maxSeatNumber = seatId

    for i in range(100,800):
        if i not in all and (i + 1) in all and (i - 1) in all:
            print("Your seat is: " + str(i))
