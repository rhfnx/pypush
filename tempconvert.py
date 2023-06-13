print(
    "_"*22,"\nTEMPERATURE CONVERSION\n"+"_"*22
)
t = {
    1:"==> 1.Celcius",
    2:"==> 2.Rankine",
    3:"==> 3.Fahrenheit",
    4:"==> 4.Kelvin",
    5:"==> 5.Exit"
}
print("PLEASE-SELECT:")
print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
print("_"*22)

while True:
    a = int(input("Enter Number: "))

    def celcius(temp):
        if temp == 1:
            print("_"*22)
            print("Convert to:\n"+t[2]+"\n"+t[3]+"\n"+t[4])
            print("_"*22)
            c1 = int(input("Enter Number: "))
            if c1 == 2:
                c12 = int(input("Enter Num to Convert: "))
                print(c12*(4/5),"R")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif c1 == 3:
                c13 = int(input("Enter Num to Convert: "))
                print((9/5*c13)+32,"F")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif c1 == 4:
                c14 = int(input("Enter Num to Convert: "))
                print(c14+273.15,"K")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
    celcius(a)

    def rankine(temp1):
        if temp1 == 2:
            print("_"*22)
            print("Convert to:\n",t[1]+"\n"+t[3]+"\n"+t[4])
            print("_"*22)
            r1 = int(input("Enter Number:"))
            if r1 == 1:
                r12 = int(input("Enter Num to Convert: "))
                print((5/4)*r12,"C")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif r1 == 3:
                r13 = int(input("Enter Num to Convert: "))
                print(((9/4)*r13)+32,"F")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif r1 == 4:
                r14 = int(input("Enter Num to Convert: "))
                print((r14*(5/4))+273.15,"K")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
    rankine(a)

    def fahrenheit(temp2):
        if temp2 == 3:
            print("_"*22)
            print("Convert to:\n"+t[1]+"\n"+t[2]+"\n"+t[4])
            print("_"*22)
            f1 = int(input("Enter Number: "))
            if f1 == 1:
                f12 = int(input("Enter Num to Convert: "))
                print((f12-32)*(5/9),"C")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif f1 == 2:
                f13 = int(input("Enter Number to Convert: "))
                print((f13-32)*(4/9),"R")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif f1 == 4:
                f14 = int(input("Enter Number to Convert:" ))
                print((f14-32)*(5/9)+273.15,"K")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
    fahrenheit(a)

    def kelvin(temp3):
        if temp3 == 4:
            print("_"*22)
            print("Convert to:\n"+t[1]+"\n"+t[2]+"\n"+t[3])
            print("_"*22)
            k1 = int(input("Enter Number: "))
            if k1 == 1:
                k12 = int(input("Enter Num to Convert: "))
                print((k12-273.15)*(5/9),"C")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif k1 == 2:
                k13 = int(input("Enter Num to Convert: "))
                print((k13-273.15)*(4/9),"R")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
            elif k1 ==3:
                k14 = int(input("Enter Num to Convert: "))
                print(((k14-273.15)*(5/9))*(9/5)+32,"F")
                print("_"*22)
                print("PLEASE-SELECT:")
                print(t[1]+"\n"+t[2]+"\n"+t[3]+"\n"+t[4]+"\n"+t[5])
                print("_"*22)
    kelvin(a)

    def endprog(temp4):
        if temp4 == 5:
            print("_"*22)
            print("THANKS FOR TRYING\n AND THANKS FOR USING")
            print("_"*22)
            print("Programmed by Naufal Rahfi")
            print("_"*22)
            exit()
    endprog(a)
