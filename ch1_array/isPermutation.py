
def isPermutation(string1, string2):
    dict1 = {}
    dict2 = {}

    for c in string1:
        if c not in dict1:
            dict1[c] = 1
        else:
            temp = dict1[c]
            dict1[c] = temp+1
    
    for c in string2:
        if c not in dict2:
            dict2[c] = 1
        else: 
            temp = dict2[c]
            dict2[c] = temp + 1
    
    for x in dict1:
        if x not in dict2:
            return False
        if dict1[x] != dict2[x]:
            return False

    return True 


print(isPermutation("aab", "baa"))
print(isPermutation("abd", "xyz"))
    