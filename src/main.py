import readpda

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

with open("pda.txt", "r") as r:
    pdatxt = r.read()

with open("input.html", "r") as r:
    html = r.read()

(startState, startStack, pda) = readpda.readpda(pdatxt)

state = startState
stack = [startStack]

i = int(0)
j = int(0)
reject = False
passed = False
alpha = False
temp = str()

# skip newline yang ada
while (html[i] == '\n'):
    i += 1

while (i < len(html) - 1 and reject == False):
    print(f"html nya pas i {i} adalah {html[i]}")
    print(f"dan current statenya adalah {state}")
    print(f"dan stacknya adalah {stack}")
    print()
    if (len(html) - i > 8 and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ') and (stack[len(stack)-1] == 'H' or stack[len(stack)-1] == 'T' or stack[len(stack)-1] == 'B' or stack[len(stack)-1] == 'S')):
#        print("masuk atas")
        i += 1
        continue
    elif (len(html) - i > 8 and stack[len(stack)-1] == '<' and state == 'W' and (html[i] == '\n' or html[i] == '\t' or html[i] == ' ')):
#        print("masuk bawah")
        i += 1
        continue
    elif (html[i] != '<' and stack[len(stack)-1] == 'G'):
#        if (html[i] == '\n'):
#            print(f"pas newline dia masuk sini")
        i += 1
        continue
    elif (html[i] in alphabet):
        while (html[i] in alphabet):
            temp = temp + html[i]
            alpha = True
            i += 1
    else:
        temp = html[i]
    while(j < len(pda) and passed == False):
        if (pda[j].inp == temp and pda[j].pop == stack[len(stack)-1] and state == pda[j].currState):
            state = pda[j].moveState
            stack.pop(len(stack)-1)
            if (pda[j].push[0] != 'e'):
                for k in range(len(pda[j].push)-1,-1,-1):
                    stack.append(pda[j].push[k])
            passed = True
        j += 1
    if not passed:
        reject = True
    passed = False
    j = 0
    print(f"temp nya {temp}")
    temp = str()
    if (not(alpha)):
        i += 1
    else:
        alpha = False

if (reject == False and len(stack) == 1 and stack[0] == 'Z'):
    print("accept")
else:
    print(html[i:])
    print(f"html nya pas {i} adalah {html[i]}")
    print(f"stack nya {stack}")
    print(f"state nya {state}")
    print(f"reject di i {i}")
