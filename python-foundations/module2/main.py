skills = ["python","machine-learning","Git"]
skills.append("FastAPI") # add 
skills.append("php") # 

for skill in enumerate(skills):
    print(skill)

skills.remove(skills[4]) # remove , uses index of list to remove

skills.pop() # removes last element

skills.clear() # deletes everything

skills.count(skills) # counts list elements
