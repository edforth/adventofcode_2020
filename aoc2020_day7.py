with open('day7input.txt',"r") as f:
    lines = f.read().splitlines()

#Part 1
desiredinnerbag = 'shiny gold bag'
containingbagscount = 0
possibleouterbags = []
for line in lines:
    split = line.split('contain ')
    outerbag = split[0].strip().rstrip('s')
    innerbag = split[1].split(',')
    #print("outer = ",outerbag," inner = ",innerbag)
    if any(desiredinnerbag in str for str in innerbag):
        possibleouterbags.append(outerbag)
        containingbagscount += 1
while containingbagscount > 0:
    containingbagscount = 0
    for desiredinnerbag in possibleouterbags:
        for line in lines:
            split = line.split('contain ')
            outerbag = split[0].strip().rstrip('s')
            innerbag = split[1].split(',')
            #print("outer = ",outerbag," inner = ",innerbag)
            if any(desiredinnerbag in str for str in innerbag):
                if outerbag not in possibleouterbags:
                    possibleouterbags.append(outerbag)
                    containingbagscount += 1
#print(containingbagscount, possibleouterbags)
print("Part 1 Answer = ", len(possibleouterbags))
#121!  First Try!

