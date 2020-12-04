req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("input_04.txt", "r") as f:
    list = f.read().split("\n\n")
    valid_passports = 0
    for passport in list:
        valid_fields = 0
        for field in req_fields:
            if field in passport:
                valid_fields += 1
            else:
                break
            if valid_fields == len(req_fields):
                valid_passports += 1

    print("The number of valid passports is: " + str(valid_passports))
