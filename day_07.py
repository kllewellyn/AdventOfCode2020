with open("input_07.txt", "r") as f:
    list = f.readlines()

    goldBag = ["shiny gold"]
    validBags = set(goldBag)
    change = 0
    change = len(validBags)
    i = 0
    while (i < 6):
        iterator = iter(list)
        for line in iterator:
            outsideBag = line.split(" contain ")[0]
            innerBags = line.split(" contain ")[1]
            newBag = ""
            iterateBag = iter(validBags)
            for bag in iterateBag:
                if bag in innerBags:
                    newBag = outsideBag.rstrip()
                    break
            if newBag != "":
                newBag = newBag.replace(" bags", "")
                validBags.add(newBag)
        i += 1
        print("The number of valid bags: " + str(len(validBags) - 1))
