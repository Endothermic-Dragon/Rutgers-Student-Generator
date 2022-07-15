# Used to randomize list
import random

# Store all the student names
names = []

# Store the "maps" from student-to-student
maps = {}

# Specify the number of students per group
studentsPerGroup = 5

# Number of shuffle iterations to run
iterations = 1000

# Fetch the list of student names
with open("student_list.txt", "r") as f:
    names = f.read().split("\n")

# Fetch the list of groups, subdivide and store relations in map
# Not exactly optimal algorithm, but serves the purpose
with open("groups.txt", "r") as f:
    for i in f.read().split("\n\n"):
        namesList = tuple(i.split("\n"))
        for j in namesList:
            if j not in maps:
                maps[j] = []
            maps[j].extend(namesList)
    for i, j in maps.items():
        temp = list(set(j))
        temp.remove(i)
        maps[i] = temp

# Set the min score to be inifinity so it's replaced at the first iteration
minScore = float("inf")
# Whenever smaller min is achieved, save to list
minList = []

# Shuffle a bunch of times, calculate "score" (# of people who've sat with each other before)
for i in range(iterations):
    namesCopy = names.copy()

    random.shuffle(namesCopy)

    namesCopy = [namesCopy[i:i + studentsPerGroup] \
        for i in range(0, len(namesCopy), studentsPerGroup)]

    score = 0

    for i in namesCopy:
        for j in i:
            score += sum(el in maps[j] for el in i)
    
    if score < minScore:
        minScore = score
        minList = namesCopy

# Print out output
print("")
print(f"Common relations: {minScore}\n")

# Generate data string to save to file
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

# Save to file
with open("output_1.txt", "w") as f:
    f.write(jointString)