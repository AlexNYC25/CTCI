

def isUnique(stringVar):
    characterList = []

    for c in stringVar:
        if characterList.count(str(c)) > 0:
            return False
        else:
            characterList.append(str(c))
    return True


print(isUnique('abcd'))
print(isUnique("aabb"))