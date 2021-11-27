with open('day07input.txt',"r") as f:
    lines = f.read().splitlines()
"""
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
"""

#Part 2
def get_inner_bags(outerbag,bagrules):
    foundbags = next(item for item in bagrules if item["outerbag"] == outerbag)
    returnedinnerbags = foundbags["innerbags"]
    return returnedinnerbags


bagrules = []
for line in lines:
    s = line.split(' contain')
    outer = s[0].strip().rstrip("s")
    innerbags = s[1].split(',')
    for i in range(0,len(innerbags)):
        cleaninput = innerbags[i].strip().rstrip('s.')
        
        bag = cleaninput.lstrip('0123456789').strip()
        if cleaninput[0:2] == "no":
            qty=0
        else:
            qty = int(cleaninput[:len(cleaninput)-len(bag)])
        innerbags[i] = dict(qty=qty,bag=bag)
        #print("Cleaninput="+cleaninput+"#","qty="+str(qty)+"#","bag="+bag+"#")

    #print(line)
    #print("outer="+outer+"#","length=",len(outer),"#")
    #print(innerbags)
    bagrules.append(dict(outerbag=outer, innerbags=innerbags))
#print(bagrules)
targetbag = 'shiny gold bag'
#print(next(item for item in bagrules if item["outerbag"] == targetbag))
returnedbags = get_inner_bags(targetbag,bagrules)
totalbags = 0 
for rb in returnedbags:
    morebags = get_inner_bags(rb['bag'],bagrules)
    print("morebags=",morebags)
    print(rb['qty'],rb['bag'])
print(returnedbags)



