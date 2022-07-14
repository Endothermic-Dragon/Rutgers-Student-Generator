import random

names = []
maps = {}
studentsPerGroup = 5
iterations = 10000

with open("student_list.txt", "r") as f:
    names = f.read().split("\n")

with open("groups.txt", "r") as f:
    for i in f.read().split("\n\n"):
        namesList = tuple(i.split("\n"))
        for i in namesList:
            if i not in maps:
                maps[i] = []
            maps[i].append(namesList)
    for i, j in maps.items():
        temp = list(set(j[0]))
        temp.remove(i)
        maps[i] = temp


del temp, namesList, f, i, j

minScore = float("inf")
minList = []

for i in range(iterations):
    namesCopy = names.copy()

    random.shuffle(namesCopy)

    namesCopy = [namesCopy[i:i + studentsPerGroup] \
        for i in range(0, len(namesCopy), studentsPerGroup)]

    score = 0

    for i in namesCopy:
        for j in i:
            score += sum(el in maps[j] for el in i)
    
    if score/2 < minScore:
        minScore = score/2
        minList = namesCopy

print("")
print(f"Common relations: {minScore}\n")

jointString = []

for i in range(len(minList)):
    print(f"Group {i + 1}:")
    subList = minList[i]
    subList = sorted(subList)
    for j in subList:
        jointString.append(j)
        print(j)
    print("")

jointString = "\n\n".join(["\n".join(jointString[i:i + studentsPerGroup]) \
        for i in range(0, len(jointString), studentsPerGroup)])

with open("output_2.txt", "w") as f:
    f.write(jointString)