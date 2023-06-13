import math

phi = math.pi

class Count:
    def __init__(self,radian,degree,result):
        self.radian = radian
        self.degree = degree
        self.result = result

    def changeDegree():
        degree = float(input("Enter Degree: "))
        result = degree * (phi/180)
        print(f"Result: {result} Radian\n")

    def changeRadian():
        radian = float(input("Enter Radian: "))
        result = radian * (180/phi)
        print(f"Result: {result} Degree\n")

while True:
    print("Angle Converter\n1. Degree to Radian\n2. Radian to Degree\n3. Exit")
    userInput = int(input("Enter Number: "))
    if userInput == 1:
        Count.changeDegree()
    elif userInput == 2:
        Count.changeRadian()
    elif userInput == 3:
        exit()