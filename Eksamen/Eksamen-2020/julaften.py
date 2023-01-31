def fridager(julaften):
    if (julaften == "sondag") or (julaften == "lordag"):
        return 4
    elif (julaften == "fredag"):
        return 2
    elif (julaften == "torsdag"):
        return 2
    elif (julaften == "onsdag"):
        return 2
    elif (julaften == "tirsdag"):
        return 2
    elif (julaften == "mandag"):
        return 2
    else:
        print("Angi en dag")
    
