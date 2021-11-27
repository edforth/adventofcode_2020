with open('day08input.txt',"r") as f:
    lines = f.read().splitlines()

"""
#Part 1
instructions = []
for line in lines:
    s = line.split()
    instructions.append(dict(cmd = s[0],value=int(s[1])))
#print(instructions)
rowindex = 0 
accumulator = 0
executedcommands = []
while 1:
    if rowindex in executedcommands:
        print("Part 1 Answer = ", accumulator)
        break
    else:
        executedcommands.append(rowindex)
    if instructions[rowindex]['cmd'] == 'nop':
        rowindex = rowindex+1
    elif instructions[rowindex]['cmd'] == 'acc':
        accumulator = accumulator + instructions[rowindex]['value']
        rowindex = rowindex+1
    elif instructions[rowindex]['cmd'] == 'jmp':
        rowindex = rowindex + instructions[rowindex]['value']
#Correct first try! (1584)
"""
"""
#Part 2 - First attempt, the changes are perpetuating throughout all of the attempts and I don't understand why.  Probably some weird python thing
Part2answer = []
startinginstructions = []
for line in lines:
    s = line.split()
    startinginstructions.append(dict(cmd = s[0],value=int(s[1])))

#for i in range(0,len(startinginstructions)):
for i in range(0,5):
    loopdebug = []
    loopdebug.append('Iteration #'+str(i))
    accumulator = 0
    rowindex = 0 
    executedcommands = []
    newinstructions = startinginstructions
    #iterate through the list trying each jmp as nop or each nop as jmp
    if newinstructions[i]['cmd'] == 'nop':
        loopdebug.append('Changed command from '+newinstructions[i]['cmd'])
        newinstructions[i]['cmd'] = 'jmp'
        loopdebug.append('to '+newinstructions[i]['cmd'])
        loopdebug.append('Value stayed at '+str(newinstructions[i]['value']))
    elif newinstructions[i]['cmd'] == 'jmp':
        loopdebug.append('Changed command from '+newinstructions[i]['cmd'])
        newinstructions[i]['cmd'] = 'nop'
        loopdebug.append('to '+newinstructions[i]['cmd'])
        loopdebug.append('Value stayed at '+str(newinstructions[i]['value']))
    else:
        #if we're not changing the command, then don't run the instructions
        loopdebug.append("No cmd change - Skipped iteration")
        print(loopdebug)
        continue
    #print("continued")
    commandlog = []
    while 1:
        if rowindex >= len(startinginstructions)-1:
            Part2answer.append(accumulator)
            #print(loopdebug)
            break
        if rowindex in executedcommands:
            #If executing a row for a second time, then the loop is infinite, so break
            #loopdebug.append("Repeated instruction on row #"+str(rowindex))
            break
        else:
            executedcommands.append(rowindex)
        oldrowindex = rowindex 
        if newinstructions[rowindex]['cmd'] == 'nop':
            rowindex = rowindex+1
            commandlog.append("Executed command #"+str(oldrowindex+1)+": "+newinstructions[oldrowindex]['cmd']+" value #"+str(newinstructions[oldrowindex]['value'])+" accumulator ="+str(accumulator)+" Next Row="+str(rowindex))
        elif newinstructions[rowindex]['cmd'] == 'acc':
            accumulator = accumulator + newinstructions[rowindex]['value']
            rowindex = rowindex+1
            commandlog.append("Executed command #"+str(oldrowindex+1)+": "+newinstructions[oldrowindex]['cmd']+" value #"+str(newinstructions[oldrowindex]['value'])+" accumulator ="+str(accumulator)+" Next Row="+str(rowindex))
        elif newinstructions[rowindex]['cmd'] == 'jmp':
            rowindex = rowindex + newinstructions[rowindex]['value']
            commandlog.append("Executed command #"+str(oldrowindex+1)+": "+newinstructions[oldrowindex]['cmd']+" value #"+str(newinstructions[oldrowindex]['value'])+" accumulator ="+str(accumulator)+" Next Row="+str(rowindex))
        #Check if the program terminates
    print(loopdebug)
    for commandl in commandlog:
        print(commandl)
print("Part 2 Answer = ", Part2answer)
#Wrong Answer = 731 (too low)
"""



#Part 2
Part2answer = []
startinginstructions = []
for line in lines:
    s = line.split()
    startinginstructions.append(dict(cmd = s[0],value=int(s[1])))

for i in range(0,len(startinginstructions)):
#for i in range(0,5):
    loopdebug = []
    loopdebug.append('Iteration #'+str(i))
    accumulator = 0
    rowindex = 0 
    executedcommands = []
    newinstructions = startinginstructions
    #iterate through the list trying each jmp as nop or each nop as jmp
    if newinstructions[i]['cmd'] == 'nop':
        loopdebug.append('Changed command from '+newinstructions[i]['cmd'])
        oldcmd = 'nop'
        newinstructions[i]['cmd'] = 'jmp'
        loopdebug.append('to '+newinstructions[i]['cmd'])
        loopdebug.append('Value stayed at '+str(newinstructions[i]['value']))
    elif newinstructions[i]['cmd'] == 'jmp':
        loopdebug.append('Changed command from '+newinstructions[i]['cmd'])
        oldcmd = 'jmp'
        newinstructions[i]['cmd'] = 'nop'
        loopdebug.append('to '+newinstructions[i]['cmd'])
        loopdebug.append('Value stayed at '+str(newinstructions[i]['value']))
    else:
        #if we're not changing the command, then don't run the instructions
        loopdebug.append("No cmd change - Skipped iteration")
        print(loopdebug)
        continue
    #print("continued")
    commandlog = []
    while 1:
        if rowindex >= len(startinginstructions)-1:
            Part2answer.append(accumulator)
            newinstructions[i]['cmd'] = oldcmd
            #print(loopdebug)
            break
        if rowindex in executedcommands:
            #If executing a row for a second time, then the loop is infinite, so break
            #loopdebug.append("Repeated instruction on row #"+str(rowindex))
            newinstructions[i]['cmd'] = oldcmd
            break
        else:
            executedcommands.append(rowindex)
        oldrowindex = rowindex 
        if newinstructions[rowindex]['cmd'] == 'nop':
            rowindex = rowindex+1
            commandlog.append("Executed command #"+str(oldrowindex+1)+": "+newinstructions[oldrowindex]['cmd']+" value #"+str(newinstructions[oldrowindex]['value'])+" accumulator ="+str(accumulator)+" Next Row="+str(rowindex))
        elif newinstructions[rowindex]['cmd'] == 'acc':
            accumulator = accumulator + newinstructions[rowindex]['value']
            rowindex = rowindex+1
            commandlog.append("Executed command #"+str(oldrowindex+1)+": "+newinstructions[oldrowindex]['cmd']+" value #"+str(newinstructions[oldrowindex]['value'])+" accumulator ="+str(accumulator)+" Next Row="+str(rowindex))
        elif newinstructions[rowindex]['cmd'] == 'jmp':
            rowindex = rowindex + newinstructions[rowindex]['value']
            commandlog.append("Executed command #"+str(oldrowindex+1)+": "+newinstructions[oldrowindex]['cmd']+" value #"+str(newinstructions[oldrowindex]['value'])+" accumulator ="+str(accumulator)+" Next Row="+str(rowindex))
        #Check if the program terminates
    newinstructions[i]['cmd'] = oldcmd
    print(loopdebug)
    for commandl in commandlog:
        print(commandl)
print("Part 2 Answer = ", Part2answer)
#Wrong Answer = 731 (too low)
#Correct second time (920)  Still not sure why the old one didn't work  need to learn more about how python handles lists/dictionaries I guess
