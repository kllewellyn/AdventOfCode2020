def doesItExit(instructions):
    lineNumbers = []
    index = 0
    accelerator = 0
    while index not in lineNumbers and index < len(instructions):
        line = instructions[index].rstrip()
        lineNumbers.append(index)
        instruction = line.split(" ")[0]
        number = int(line.split(" ")[1])
        if instruction == "nop":
            index += 1
        elif instruction == "acc":
            accelerator += number
            index += 1
        elif instruction == "jmp":
            index += number
        if index in lineNumbers:
            return 0
    return accelerator

with open("input_08.txt", "r") as f:
    input = f.read().splitlines()
    lineNumbers = list(range(0,len(input)))
    index = 0
    for line in input:
        if "nop" in line:
            replace = line.replace("nop", "jmp")
            input[index] = replace
            if(doesItExit(input) == 0):
                input[index] = line
            else:
                print("The accelerator is: " + str(doesItExit(input)))
                break
            index += 1
        elif "acc" in line:
            index += 1
            continue
        elif "jmp" in line:
            replace = line.replace("jmp", "nop")
            input[index] = replace
            if(doesItExit(input) == 0):
                input[index] = line
            else:
                print("The accelerator is: " + str(doesItExit(input)))
                break
            index += 1
