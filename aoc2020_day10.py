with open('day10input.txt',"r") as f:
    lines = f.read().splitlines()

adapters = []
for line in lines:
    adapters.append(int(line))
adapters.sort()
print(adapters)
currentvoltage = 0
jump1count = 0
jump2count = 0
jump3count = 0
for i in range(0,len(adapters)):
    voltagejump = adapters[i] - currentvoltage
    if voltagejump == 1:
        jump1count = jump1count+1
    elif voltagejump == 2:
        jump2count = jump2count+1
    elif voltagejump == 3:
        jump3count = jump3count+1
    else:
        print("Voltage jump is ",voltagejump,"BREAK")
        break
    print("iteration =",i,"adapter voltage = ",adapters[i],"voltage jump = ",voltagejump,"jump1count = ",jump1count,"jump2count = ",jump2count,"jump3count = ",jump3count)
    currentvoltage = adapters[i]
#Account for the final jump to the device (+3)
jump3count = jump3count + 1
print("Part 1 answer = ",jump1count*jump3count)
#Incorrect answer:1809 (too low)
#Correct on second try (1876)  I forgot to account for the final 3 volt jump to the device
