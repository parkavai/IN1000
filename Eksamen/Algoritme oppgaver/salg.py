ordbok = {"Heidi": 133, "John":97, "Kari":48}

def maanedenSalgsperson(ordbok):
    for i in ordbok:
        stoerst = ordbok[i]
        if ordbok[i] > stoerst:
            stoerst = ordbok[i]
        return stoerst

print(maanedenSalgsperson(ordbok))
