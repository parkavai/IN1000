def dempDeg(tekst):
    sisteindeks = len(tekst) - 1
    if(len(tekst) == 0):
        return ""
    elif(tekst[sisteindeks] != "!"):
        return tekst
    for x in range(len(tekst) - 1):
        if(tekst[sisteindeks] == "!"):
            sisteindeks -= 1
    if(sisteindeks == 0):
        return "."
    return tekst[0:sisteindeks+1] + "."
        


    


assert(dempDeg("abcde!!!")) == "abcde."
assert(dempDeg("!!")) == "."
assert(dempDeg("!abscde f!")) =="!abscde f."
assert(dempDeg("!abscde f")) =="!abscde f"
assert(dempDeg("abcd")) == "abcd"
assert(dempDeg("")) == ""
