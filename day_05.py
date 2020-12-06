with open("input_05.txt", "r") as f:
    list = f.read().splitlines()
    maxSeatNumber = 0
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
                maxRow = (maxRow - minRow) // 2 + minRow
                elif current == "B":
                minRow = (maxRow - minRow) // 2 + minRow
        finalRow = maxRow
        minColumn = 0
        maxColumn = 7
        while (maxColumn - minColumn) != 1:
            try:
                current = next(characters)
            except StopIteration:
                continue
            if current == "L":
                maxColumn = (maxColumn - minColumn) // 2 + minColumn
            elif current == "R":
                minColumn = (maxColumn - minColumn) // 2 + minColumn

        finalColumn = maxColumn

        seatId = (finalRow * 8) + finalColumn

        if seatId > maxSeatNumber:
            maxSeatNumber = seatId

    print("The highest seat Id is: " + str(maxSeatNumber))
