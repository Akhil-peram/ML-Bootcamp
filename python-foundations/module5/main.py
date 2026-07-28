# Loops only two
# for loop
# while loop
for i in range(10):
    print(i)                    # remember the indentations , 4 spaces

count = 0
while count <5:
    print(count)
    count+=1
# nested for loops


skills = ["Python","ML","Data Science","FastAPI","React"]
for skill in skills:
    for count in skill:
        count=len(skill)
    print("the word counts is ",count,"for",skill)


"""
Be mindful in which loop are you printing , always

"""
