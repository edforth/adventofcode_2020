with open('day2input.txt',"r") as f:
    lines = f.read().splitlines()

#Part 1
count = 0
for line in lines:
    split = line.split(":")
    split2 = split[0].split()
    split3 = split2[0].split("-")
    lower = int(split3[0])
    upper = int(split3[1])
    key = split2[1]
    password = split[1]
    if password.count(key) >= lower and password.count(key) <= upper:
        count = count+1
print("Part 1 Answer = ",count)


#Part 2
count = 0
isvalid = "not valid"
for line in lines:
    split = line.split(":")
    split2 = split[0].split()
    split3 = split2[0].split("-")
    lower = int(split3[0])
    upper = int(split3[1])
    key = split2[1]
    password = split[1].strip()
    if (password[lower-1] == key and password[upper-1] != key) or (password[lower-1] != key and password[upper-1] == key):
        #isvalid = "valid"
        count = count+1
    #print(line, isvalid)
    #print("key=",key,"lower=",lower,password[lower-1],"upper=",upper,password[upper-1],"  ",isvalid)
    #isvalid = "not valid"
print("Part 2 Answer = ",count)
#First attempt was 435 - Answer is too low
#Second attempt correct (699) - I needed to strip the whitespace from the password variable, as there was leading whitespace