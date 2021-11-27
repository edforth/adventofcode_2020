with open('day06input.txt',"r") as f:
    lines = f.read().split("\n\n")

#Part 1
fullsum = 0 
for line in lines:
    list = line.splitlines()
    groupanswers = ''.join(list)
    #print("list = ",list, " concat = ",groupanswers)
    questionsanswered = 0
    for question in range(97,123):
        if chr(question) in groupanswers:
            questionsanswered = questionsanswered + 1
    fullsum = fullsum + questionsanswered
print("Part 1 Answer = ",fullsum)
#6259  First try!



#Part 2
fullsum = 0 
for line in lines:
    list = line.splitlines()
    groupanswers = ''.join(list)
    questionsanswered = 0
    for question in range(97,123):
        if groupanswers.count(chr(question)) == len(list):
            questionsanswered = questionsanswered + 1
    #groupanswers = ''.join(list)
    fullsum = fullsum + questionsanswered
    #print("list = ",list)
print("Part 2 Answer = ",fullsum)
#3178! First Try!!