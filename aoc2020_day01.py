with open('day1input.txt',"r") as f:
    lines = f.read().splitlines()

#Part 1
breakloops = 0
for line1 in lines:
    value1 = int(line1)
    for line2 in lines:
        value2 = int(line2)
        if value1 == value2:
            continue
        if value1 + value2 == 2020:
            print("Part 1 Answer = ", value1 * value2)
            breakloops = 1
            break

    if breakloops == 1:
        break

#Part 2
breakloops = 0
for line1 in lines:
    value1 = int(line1)
    for line2 in lines:
        value2 = int(line2)
        if value1 == value2:
            continue
        for line3 in lines:
            value3 = int(line3)
            if value3 == value1:
                continue
            if value3 == value2:
                continue
            if value1 + value2 + value3 == 2020:
                print("Part 2 Answer = ", value1 * value2 * value3)
                breakloops = 1
                break
        if breakloops == 1:
            break
    if breakloops == 1:
        break   
