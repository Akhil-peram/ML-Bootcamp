# functions


def hello():
    print("hello welcome to ML boot camp")


def yourbio(*args):
    name = input("Enter your name:")
    age = input("Enter age: ")
    res = input("why bootcamp")
    print(name,age,res,sep="\n")

def circle(r:int):
    r= int(input("Enter radius for circumference: "))
    return 2* 3.14 * r


#hello()
#yourbio()
print(circle(0))

"""
*args and **kwargs

args can take multiple inputs  as a tuple

kwargs are keyword arhuments that can take multiple inputs as a dictionary

"""
