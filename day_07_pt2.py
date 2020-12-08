list = open("input_07.txt", "r").read().splitlines()

def checkBags(bag):
    for line in list:
        outsideBag = line.split(" contain ")[0]
        innerBags = line.split(" contain ")[1].replace(".", "")
        if bag in outsideBag:
            if "no other" in line:
                return 1
            innerBags = innerBags.split(", ")
            sum = 0
            for item in innerBags:
                sum += int(item[0]) * checkBags(item[2:].rstrip())
            return sum + 1

print(checkBags("shiny gold") - 1)
