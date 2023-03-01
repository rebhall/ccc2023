peppers = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}
N = int(input())
T = 0
Nlist = []
for number in range(N):
    temp = input()
    Nlist.append(temp)
for i in Nlist:
    T += int(peppers[i])
print(T)
