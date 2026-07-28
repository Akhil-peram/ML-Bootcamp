marks :int = int(input("Enter marks: "))

if marks >= 90:
    print("Distinction")
elif marks>75 and marks<=90:
    print("First Class")
elif marks>65 and marks<=75:
    print("Second Class")
elif marks >55 and marks <=65:
    print("Third class")
elif marks >45 and marks <=55:
    print("Qualified")
else:
    print("Failed")
