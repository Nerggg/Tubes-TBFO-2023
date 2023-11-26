import functions.readpda as readpda
import functions.load as load

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','1','2','3','4','5','6','G','E','T','P','O','S']

(start, filepda, filehtml) = load.load()

if (start):
    with open(filepda, "r") as r:
        pdatxt = r.read()

    with open(filehtml, "r") as r:
        html = r.read()

    (inputSymbol, startState, startStack, pda) = readpda.readpda(pdatxt)

    state = startState
    stack = [startStack]

    i = int(0)
    j = int(0)
    reject = False
    passed = False
    alpha = False
    temp = str()

    # bonus
    line = int(1)
    currLine = str()
    bidx = int()
    lidx = int()

    # skip newline yang ada
    while (html[i] == '\n'):
        i += 1
        line += 1

    while (i < len(html) - 1 and reject == False):
        epsilonIdxTemp = i-1
#        print(f"html nya pas i {i} adalah {html[i]}")
#        print(f"dan current statenya adalah {state}")
#        print(f"dan stacknya adalah {stack}")
#        print()
        if (len(html) - i > 8 and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ') and (stack[len(stack)-1] == 'Z' or stack[len(stack)-1] == 'H' or stack[len(stack)-1] == 'T' or stack[len(stack)-1] == 'B' or stack[len(stack)-1] == 'S' or stack[len(stack)-1] == 'tr' or stack[len(stack)-1] == 'body' or stack[len(stack)-1] == 'input' or stack[len(stack)-1] == 'img' or stack[len(stack)-1] == 'th' or stack[len(stack)-1] == 'td' or stack[len(stack)-1] == 'table')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (len(html) - i > 8 and stack[len(stack)-1] == 'C' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (len(html) - i > 8 and stack[len(stack)-1] == 'html' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (len(html) - i > 8 and stack[len(stack)-1] == 'head' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (len(html) - i > 8 and stack[len(stack)-1] == 'link' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (len(html) - i > 8 and stack[len(stack)-1] == '>' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (len(html) - i > 8 and stack[len(stack)-1] == '<' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif ((html[i] != '<') and stack[len(stack)-1] == 'G'):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif ((html[i] != '-') and stack[len(stack)-1] == 'C'):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif ((html[i] != '>') and stack[len(stack)-1] == 'CC'):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (html[i] != '\"' and html[i] != '=' and stack[len(stack)-1] == 'A'):
            if (html[i] == '\n'):
                bidx = i
                line += 1
            i += 1
            continue
        elif (html[i] in alphabet):
            while (html[i] in alphabet):
                temp = temp + html[i]
                alpha = True
                i += 1
        else:
            temp = html[i]
        epsilon = False
        while(j < len(pda) and passed == False):
            if (pda[j].inp == 'e' and pda[j].pop == stack[len(stack)-1] and state == pda[j].currState):
                state = pda[j].moveState
                stack.pop(len(stack)-1)
                if (pda[j].push[0] != 'e'):
                    for k in range(len(pda[j].push)-1,-1,-1):
                        stack.append(pda[j].push[k])
                epsilon = True
                passed = True
            elif (pda[j].inp == temp and pda[j].pop == stack[len(stack)-1] and state == pda[j].currState):
                state = pda[j].moveState
                stack.pop(len(stack)-1)
                if (pda[j].push[0] != 'e'):
                    for k in range(len(pda[j].push)-1,-1,-1):
                        stack.append(pda[j].push[k])
                passed = True
            j += 1
            if (epsilon):
                i = epsilonIdxTemp
        if not passed:
            reject = True
        passed = False
        j = 0
    #    print(f"temp nya {temp}")
        temp = str()
        if (not(alpha)):
            i += 1
        else:
            alpha = False

    if (reject == False and len(stack) == 1 and stack[0] == 'Z'):
        print("Accepted")
    else:
#        print("DEBUG")
#        print(html[i:])
#        print(f"html nya pas {i} adalah {html[i]}")
#        print(f"stack nya {stack}")
#        print(f"state nya {state}")
        while (html[i] != '\n'):
            i += 1
        lidx = i

        print("Syntax Error")
        print(f"Terdapat kesalahan sintaks pada line {line}:")
        print(html[bidx+1:lidx])
