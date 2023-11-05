import readpda as readpda

with open("pda.txt", "r") as rule:
    pda = rule.read()

(inputword, start, lop) = readpda.readpda(pda)

print(inputword)
print()
print(start)
print()
print(lop)
