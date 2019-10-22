

def oneAway(stringVar1, stringVar2):
    temp1 = list(stringVar1)
    temp2 = list(stringVar2)

    for c in stringVar1:
        if stringVar2.count(c) > 0:
            temp1.remove(c)
            temp2.remove(c)
    
    if (len(temp1) < 2 or len(temp2) < 2):
        return True
    else:
        return False

print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
