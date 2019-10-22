
def urlify(stringVar):
    stringToBeReturned = ""

    for c in stringVar:
        if c == ' ':
            stringToBeReturned += '%20'
        else: 
            stringToBeReturned += c
    return stringToBeReturned


print(urlify("time up"))