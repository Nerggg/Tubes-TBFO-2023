import readpda

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','/']

with open("pda.txt", "r") as r:
    pdatxt = r.read()

with open("input.html", "r") as r:
    html = r.read()

(start, pda) = readpda.readpda(pdatxt)

for i in range (len(pda)):
    print(f"pda ke {i + 1}")
    print(pda[i].currState)
    print(pda[i].inp)
    print(pda[i].pop)
    print(pda[i].moveState)
    print(pda[i].push)
