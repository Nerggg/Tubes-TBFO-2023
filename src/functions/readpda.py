class LOP: # list of production
    def __init__(self, currState, inp, pop, moveState, push): 
        self.currState = currState # currState: state saat itu
        self.inp = inp # inp: input symbol
        self.pop = pop # pop: top stack symbol yg di pop
        self.moveState = moveState # moveState: state tujuan
        self.push = push # push: stack symbol yang di push

def readpda(pdatxt):
    startStack = str()
    startState = str()
    temp = str()
    currStateTemp = str()
    inpTemp = str()
    popTemp = str()
    moveStateTemp = str()
    pushTemp = []
    pda = []
    inputSymbol = []

    i = int(0)

    while (pdatxt[i] != '\n'): # skip baris pertama 
        i += 1
    i += 1
    while (pdatxt[i] != '\n'): # skip baris kedua
        temp += pdatxt[i]
        i += 1
        if (pdatxt[i] == ' '):
            inputSymbol.append(temp)
            temp = str()
            i += 1
    inputSymbol.append(temp)
    temp = str()
    i += 1
    while (pdatxt[i] != '\n'):
        temp += pdatxt[i]
        i += 1
    i += 1
    startStack = temp # mindahin baris ketiga ke starting stack symbol
    temp = str()
    while (pdatxt[i] != '\n'): # skip baris keempat
        i += 1
    i += 1
    while (pdatxt[i] != '\n'):
        temp += pdatxt[i]
        i += 1
    i += 1
    startState = temp # mindahin baris kelima ke starting state

    # mindahin baris keenam hingga akhir ke fungsi transisi
    temp = str()
    while (i < len(pdatxt)):
        while (pdatxt[i] != ' '):
            temp = temp + pdatxt[i]
            i += 1
        currStateTemp = temp
        temp = str()
        i += 1
        while (pdatxt[i] != ' '):
            temp = temp + pdatxt[i]
            i += 1
        inpTemp = temp
        temp = str()
        i += 1
        while (pdatxt[i] != ' '):
            temp = temp + pdatxt[i]
            i += 1
        popTemp = temp
        temp = str()
        i += 1
        while (pdatxt[i] != ' '):
            temp = temp + pdatxt[i]
            i += 1
        moveStateTemp = temp
        temp = str()
        i += 1
        while (pdatxt[i-1] != '\n'):
            while (pdatxt[i] != ',' and pdatxt[i] != '\n'):
                temp = temp + pdatxt[i]
                i += 1
            pushTemp.append(temp)
            temp = str()
            i += 1

        pdatemp = LOP(currStateTemp, inpTemp, popTemp, moveStateTemp, pushTemp)
        pda.append(pdatemp)
        currStateTemp = str()
        inpTemp = str()
        popTemp = str()
        moveStateTemp = str()
        pushTemp = []

    return (inputSymbol, startState, startStack, pda)
