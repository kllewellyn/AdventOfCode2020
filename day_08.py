with open("input_08_test.txt", "r") as f:
    instructions = f.read().splitlines()

    lineNumbers = list(range(0,len(instructions)))
    index = 0
    accelerator = 0
    while index in lineNumbers:
        line = instructions[index].rstrip()
        lineNumbers.remove(index)
        instruction = line.split(" ")[0]
        number = int(line.split(" ")[1])
        if instruction == "nop":
            index += 1
            continue
        elif instruction == "acc":
            accelerator += number
            index += 1
        elif instruction == "jmp":
            index += number
    print("The accelerator is: " + str(accelerator))
