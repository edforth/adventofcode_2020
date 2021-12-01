with open('day09input.txt',"r") as f:
    lines = f.read().splitlines()

"""
#Part 1 Try 1
preamblelength = 5 
preamble = []
possiblepreamblesums = []
part1answer = 0
for i in range(0,preamblelength):
    preamble.append(lines[i])
#print(preamble)
for i in preamble:
    for j in preamble: 
        appendsum = int(i)+int(j)
        print("i=",i,"j=",j,"sum=",appendsum)
        if i != j: 

            possiblepreamblesums.append(appendsum)
print(possiblepreamblesums)
for i in range(preamblelength,len(lines)):
    if int(lines[i]) not in possiblepreamblesums:
        part1answer = lines[i]
        break 
print("Part 1 answer =",part1answer)
#The test example doesn't seem to be correct?   Am I misreading the puzzle?
#Tried the script on the full input without getting the test input to work.  Incorrect answer (102: too low)
#yes, I misread.  Each line must be a sum of two of the X preceding numbers, not a sum of two of the original X numbers.
"""



#Part 1 Try 2
preamblelength = 25
part1answerfound = False 
part1answer = 0  
for i in range(preamblelength,len(lines)):
    if part1answerfound == True:
        break
    preamble = [] 
    possiblepreamblesums = []
    for j in range(i-preamblelength,i):
        preamble.append(int(lines[j]))
    #print("activenumber-",lines[i],"preamble=",preamble)
    for k in preamble:
        for l in preamble: 
            appendsum = k + l
            if k != l: 
                possiblepreamblesums.append(appendsum)
    if int(lines[i]) not in possiblepreamblesums:
        part1answer = lines[i]
        part1answerfound = True 
print("Part 1 answer = ",part1answer,"part1answerfound=",part1answerfound)
#Got there! (31161678)  - Lots of casting and type issue grossness.  
#I think I should have cast the active number and some other variables at the 
#beginning of the for loop and then used them instead of repeatedly recasting
    

#Part 2

#This requires part one
invalidentry = int(part1answer)
contiguousrangefound = False 
for i in range(0,len(lines)):
    if contiguousrangefound == True:
        break
    loopcounter = 1
    contiguousrangesum = int(lines[i])
    rangeentries = []
    rangeentries.append(contiguousrangesum)
    while contiguousrangesum < invalidentry:
        nextentry = int(lines[i+loopcounter])
        contiguousrangesum = contiguousrangesum + nextentry
        rangeentries.append(nextentry)
        loopcounter = loopcounter + 1
    print(contiguousrangesum,rangeentries)
    if contiguousrangesum == invalidentry:
        contiguousrangefound = True
        #print(contiguousrangesum,rangeentries)
        rangeentries.sort()
        part2answer = rangeentries[0] + rangeentries[len(rangeentries)-1]
print("Part 2 answer =",part2answer)
#Incorrect answer 62323356 (too high)   The test case validated :( 
#Correct answer: 5453868   My while loop was messed up. 




