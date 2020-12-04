import re

valid_passports = 0

with open("input_04.txt", "r") as f:
    list = f.read().split("\n\n")
    count = 0
    print("# of passport entries: " + str(len(list)))
    for passport in list:
        passport = passport.rstrip().replace("\n", " ")
        pairs = passport.split(" ")
        count += 1
        valid = 0

        for pair in pairs:
            key = pair.split(":")[0].strip()
            value = pair.split(":")[1].strip(" ")
            if ("byr" == key and int(value) >= 1920 and int(value) <= 2002):
                valid += 1
            elif ("iyr" == key and int(value) >= 2010 and int(value) <= 2020):
                valid += 1
            elif ("eyr" == key and int(value) >= 2020 and int(value) <= 2030):
                valid += 1
            elif "hgt" == key:
                if "cm" in value:
                    if int(value[:len(value) - 2]) >= 150 and int(value[:len(value) - 2]) <= 193:
                        valid += 1
                elif "in" in value:
                    if int(value[:len(value) - 2]) >= 59 and int(value[:len(value) - 2]) <= 76:
                        valid += 1
            elif "hcl" == key:
                if re.match("^[#][0-9a-f]{6}$", value):
                    valid += 1
            elif "ecl" == key:
                validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if value in validEcl:
                    valid += 1
            elif "pid" == key:
                if re.match("^\d{9}$", value):
                    valid += 1
            print("Valid is: " + str(valid))
        if valid == 7:
            valid_passports += 1

    print("The number of valid passports is: " + str(valid_passports))
    print("Count is : " + str(count))
