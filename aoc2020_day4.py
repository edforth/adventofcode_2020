with open('day4input.txt',"r") as f:
    lines = f.read().split("\n\n")


#Part 1
validcount = 0
for line in lines:
    #isvalid = "not valid"
    d = dict(pair.split(":") for pair in line.split())
    reqkeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if all (key in d for key in reqkeys):
        #isvalid = "valid"
        validcount = validcount + 1
    #print(d, isvalid)
print("Part 1 Answer = ",validcount)
#Correct first try (245)

#Part 2
def check_byr(byr):
    if int(byr) >= 1920 and int(byr) <= 2002:
        return True
    else: 
        #print("##################################################",d,"BAD BIRTH YEAR")
        exceptions.append("Bad Birth Year")
        return False 

def check_iyr(iyr):
    if int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    else: 
        #print("##################################################",d,"BAD ISSUE YEAR")
        exceptions.append("Bad Issue Year")
        return False 

def check_eyr(eyr):
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    else: 
        #print("##################################################",d,"BAD EXPIRATION YEAR")
        exceptions.append("Bad Expiration Year")
        return False 




def check_hgt(hgt):
    if hgt[:len(hgt)-2].isnumeric() == False: 
        exceptions.append("Bad Height - Nonnumeric")
        return False 
    else:
        heightvalue = int(hgt[:len(hgt)-2])
    if hgt[len(hgt)-2:] == 'cm':
        if heightvalue >= 150 and heightvalue <= 193:
            return True 
        else:
            exceptions.append("Bad Height invalid cm value")
            return False
    elif hgt[len(hgt)-2:] == 'in':
        if heightvalue >= 59 and heightvalue <= 76:
            return True 
        else:
            exceptions.append("Bad Height invalid in value")
            return False
    else:
        exceptions.append("Bad Height - Neither in or cm")
        return False

    """
    if (hgt[len(hgt)-2:] == 'cm' or hgt[len(hgt)-2:] == 'in') and (hgt[:len(hgt)-2].isnumeric()):
        return True
    else: 
        #print("##################################################",d,"BAD HEIGHT")
        exceptions.append("Bad Height")
        return False 
    """











def check_hcl(hcl):
    if hcl[0] != '#' or len(hcl) != 7 :
        return False
    else: 
        okcharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        for char in hcl[1:]:
            if char not in okcharacters:
                #print("##################################################",d,"BAD HAIR COLOR")
                exceptions.append("Bad Hair Color")
                return False 
        return True 
        
def check_ecl(hcl):
    okeyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if hcl in okeyecolors:
        return True
    else: 
        #print("##################################################",d,"BAD EYE COLOR")
        exceptions.append("Bad Eye Color")
        return False 

def check_pid(pid):
    if len(pid) == 9 and pid.isnumeric():
        return True
    else: 
        exceptions.append("Bad Passport ID")
        return False 

def check_keys():
    reqkeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if all (key in d for key in reqkeys):
        return True
    else: 
        exceptions.append("Missing Keys")
        return False 



validcount = 0
for line in lines:
    exceptions = []
    d = dict(pair.split(":") for pair in line.split())
    #reqkeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #if all (key in d for key in reqkeys) and check_byr(d['byr']) and check_iyr(d['iyr']) and check_eyr(d['eyr']) and check_hgt(d['hgt']) and check_hcl(d['hcl']) and check_ecl(d['ecl']) and check_pid(d['pid']):
    if check_keys() and check_byr(d['byr']) and check_iyr(d['iyr']) and check_eyr(d['eyr']) and check_hgt(d['hgt']) and check_hcl(d['hcl']) and check_ecl(d['ecl']) and check_pid(d['pid']):
        #isvalid = "valid"
        validcount = validcount + 1
    #print(d, exceptions)
print("Part 2 Answer = ",validcount)
#135 is too high
#Correct on second try (133)  Apparently, I hadn't implemented all of the validation rules for height