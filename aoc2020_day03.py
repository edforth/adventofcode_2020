with open('day03input.txt',"r") as f:
    lines = f.read().splitlines()

def newpos(currentposition, currentslope):
    newxpos = currentposition['xpos'] + currentslope['x']
    newypos = currentposition['ypos'] + currentslope['y']
    while newxpos > 30:
        newxpos = newxpos - 31
    newposition = {
        'xpos': newxpos,
        'ypos': newypos
    }
    return newposition


#Part 1
treeshit = 0
position = {
    'xpos': 0,
    'ypos': 0
}
slope = {
    'x': 3,
    'y': 1
}

while position['ypos'] < len(lines)-1:
    position = newpos(position, slope)
    istree = lines[position['ypos']][position['xpos']]
    if istree == '#':
        treeshit = treeshit+1
    #print(position, istree)
    #print(len(lines))
print("Part 1 Answer = ", treeshit)
#87 is not correct :(
#Correct on second try (289) The problem was, when I looped I subtracted 30 from the overage, instead of thirty one.  (Starting a 0 is messing me up)



#Part 2
treeshit = 0
treeshitproduct = 1
slopes = [
    {
    'x': 1,
    'y': 1
    },
    {
    'x': 3,
    'y': 1
    },
    {
    'x': 5,
    'y': 1
    },
    {
    'x': 7,
    'y': 1
    },
    {
    'x': 1,
    'y': 2
    }
]
for slope in slopes:
    position = {
        'xpos': 0,
        'ypos': 0
    }
    while position['ypos'] < len(lines)-1:
        position = newpos(position, slope)
        istree = lines[position['ypos']][position['xpos']]
        if istree == '#':
            treeshit = treeshit+1
        #print(position, istree, "treeshit=",treeshit)
    treeshitproduct = treeshitproduct * treeshit
    treeshit = 0
print("Part 2 Answer = ", treeshitproduct)
#4390051033368 is not the answer (too high)
    #I'm guessing there's something weird about the slope that's moving y by two
    #nope, it was that I forgot to rest treeshit between checking the different slopes
#yup, second try was correct (5522401584)