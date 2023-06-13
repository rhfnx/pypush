#Degree to Radian and Radian to Degree

import math

phi = math.pi

class count:
    def __init__(self,deg,rad,result):
        self.deg = deg
        self.rad = rad
        selt.result = result

    def dtr():
        deg = int(input("Input Degree: "))
        result = (deg*phi/180)
        print(f"Result: {result}")
        
    def rtd():
        rad = int(input("Input Radian: "))
        result = (rad*180/phi)
        print(f"Result: {result}")

while True:

    print("1. Degree to Radian\n2. Radian to Degree\n3. Exit")
    user_input = int(input("Enter Number: "))
    if user_input == 1:
        count.dtr()
        
    elif user_input == 2:
        count.rtd()
        
    elif user_input == 3:
        print("May that help you!, Thank You!")
        exit()


