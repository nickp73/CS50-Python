students = ["Harry", "Ron", "Hermione", "Draco"]
houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1,
          students[i])

for i in range(len(students)):
    print(i + 1,
          students[i].upper())
    print(i + 1,
          students[i].lower())
    print(i + 1,
          students[i].capitalize())
    print(i + 1,
          students[i].title())
    print(i + 1,
          students[i].swapcase())

