def readpda(pda):
    i = int(0)
    j = int(0)
    k = int(0)
    n = int(0) # total list of productions (lop)
    temp = str()
    start = str()
    inputword = []

    # masukin baris pertama ke dalam inputword
    while(pda[i] != '\n'):
        if(pda[i] != ' '):
            temp = temp + pda[i]
        else:
            inputword.append(temp)
            temp = str()
        i += 1

    inputword.append(temp)
    temp = str()
    i += 1

    # masukin starting stack symbol
    while(pda[i] != '\n'):
        if(pda[i] != ' '):
            temp = temp + pda[i]
        i += 1

    start = temp
    temp = str()
    i += 1

    idxtemp = int(i)
    
    for i in range(idxtemp, len(pda)):
        if(pda[i] == '\n'):
            n += 1

    lop = [["" for k in range(3)] for j in range(n)]

    for i in range(idxtemp, len(pda)):
        if(pda[i] != ' ' and pda[i] != '\n'):
            temp = temp + pda[i]
        elif(pda[i] == ' ' or pda[i] == '\n'):
            lop[j][k] = temp
            k += 1
            temp = str()
        if (k == 3):
            j += 1
            k = 0

    return (inputword, start, lop)
