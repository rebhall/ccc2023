Edict = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, }
N = int(input())
Nlist = []
iterCount = 0
F = ""

for number in range(N):
    temp = input()
    Nlist.append(temp)

for day in Edict:
    for person in Nlist:
        if person[iterCount] == "Y":
            Edict[day] += 1
    iterCount += 1

X = max(Edict.values())
for i in Edict.keys():
    if Edict.get(i) == X:
        F += str(i) + ","

F = F.rstrip(",")
print(F)
