with open('day05input.txt',"r") as f:
    lines = f.read().splitlines()

#Part 1
maxboardingpass = 0 
for line in lines:
    rowmin = 0
    rowmax = 127
    rowfactor = 64
    colmin = 0
    colmax = 7
    colfactor = 4
    for char in line:
        if char == 'F':
            rowmax = rowmax - rowfactor 
            rowfactor = rowfactor / 2
            continue
        if char == 'B':
            rowmin = rowmin + rowfactor
            rowfactor = rowfactor / 2
            continue
        if char == 'L':
            colmax = colmax - colfactor
            colfactor = colfactor / 2
            continue
        if char == 'R':
            colmin = colmin + colfactor 
            colfactor = colfactor / 2 
            continue
    seatid = rowmin * 8 + colmin 
    #print("rowmin = ",rowmin," rowmax = ",rowmax," rowfactor = ",rowfactor," colmin = ",colmin," colmax = ",colmax," colfactor = ",colfactor," seatid = ", seatid)
    if seatid > maxboardingpass:
        maxboardingpass = seatid 
print("Part 1 Answer = ", maxboardingpass)
#935! First try!


#Part 2
lowestseatid = 99999999999999999999
highestseatid = 0
allseatids = []
for line in lines:
    rowmin = 0
    rowmax = 127
    rowfactor = 64
    colmin = 0
    colmax = 7
    colfactor = 4
    for char in line:
        if char == 'F':
            rowmax = rowmax - rowfactor 
            rowfactor = rowfactor / 2
            continue
        if char == 'B':
            rowmin = rowmin + rowfactor
            rowfactor = rowfactor / 2
            continue
        if char == 'L':
            colmax = colmax - colfactor
            colfactor = colfactor / 2
            continue
        if char == 'R':
            colmin = colmin + colfactor 
            colfactor = colfactor / 2 
            continue
    seatid = rowmin * 8 + colmin 
    #print("rowmin = ",rowmin," rowmax = ",rowmax," rowfactor = ",rowfactor," colmin = ",colmin," colmax = ",colmax," colfactor = ",colfactor," seatid = ", seatid)
    if seatid > highestseatid:
        highestseatid = seatid 
    if seatid < lowestseatid:
        lowestseatid = seatid 
    allseatids.append(seatid)


missingcount = 0 
for id in range(int(lowestseatid), int(highestseatid)):
    if id not in allseatids:
        missingseatid = id
        missingcount = missingcount + 1
print("Part 2 Answer = ", missingseatid, " missingcount = ",missingcount)
#743! First time again!

    