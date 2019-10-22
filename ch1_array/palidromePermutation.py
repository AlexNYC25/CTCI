
def palidromePermutation(stringVar):
    temp = []
    tempSizeWithoutSpaces = 0

    for c in stringVar:
        if (c != ' '):
            tempSizeWithoutSpaces = tempSizeWithoutSpaces + 1
            if temp.count(c) > 0 :
                temp.remove(c)
            else:
                temp.append(c)
    
    if tempSizeWithoutSpaces % 2 == 1:
        if len(temp) != 1:
            return False
        else:
            return True

    if tempSizeWithoutSpaces % 2 == 0:
        if len(temp) != 0:
            return False
        else:
            return True

print(palidromePermutation("aba bcc"))
print(palidromePermutation("abbgx cca"))
    
