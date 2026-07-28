
def create_files():
    goals = []
    goal = input("Enter goals: ")
    goals.append(goal + "\n")

    with open("notes.txt", "a") as file:
        file.writelines(goals)

create_files()

"""


with open("notes.txt", "w") as file:
    file.write("Learning Python")






with open("notes.txt", "r") as file:
    print(file.read())

"""

def readfiles():
    with open("notes.txt","r") as file:
        print(file.read())
readfiles()
