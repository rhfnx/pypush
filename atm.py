#import something
from time import sleep

#Layout 1
print("="*30)
sleep(.50)
print("|"*2,"__THE BANK ATM MACHINE__","|"*2)
sleep(.50)
print("="*30)
sleep(.50)
print("|"*2,"___1. ACOUNT-BALANCE____","|"*2)
sleep(.50)
print("|"*2,"___2. CASH-DEPOSIT______","|"*2)
sleep(.50)
print("|"*2,"___3. WITHDRAW-CASH_____","|"*2)
sleep(.50)
print("|"*2,"___4. TRANSFER__________","|"*2)
sleep(.50)
print("|"*2,"___5. EXIT______________","|"*2)
sleep(.50)
print("|"*2,"___CHOOSE-THE-NUMBER____","|"*2)
sleep(.50)

#Layout 2
MenuList={
  1:"||=====ACCOUNT-BALANCE======||",
  2:"||=====CASH-DEPOSIT=========||",
  3:"||=====WITHDRAW-CASH========||",
  4:"||=====TRANSFER=============||",
  5:"||===========EXIT===========||"
}
balance = 0

#Layout 3
while  True:
  
  key_input = int(input("==============================\n||ENTER NUMBER||:"))
  a = MenuList.get(key_input)

#ACCOUNT BALANCE FUNCTION-
  if a == "||=====ACCOUNT-BALANCE======||":
    print(MenuList[1])
    print("||YOUR BALANCE > $",balance)
    
#CASH DEPOSIT FUNCTION-    
  elif a == "||=====CASH-DEPOSIT=========||":
    print(MenuList[2])
    a1 = int(input("||ENTER AMMOUNT||:$ "))
    balance = balance + a1
    print("||YOUR BALANCE NOW|:$",balance)

#WITHDRAW CASH FUNCTION-
  elif a == "||=====WITHDRAW-CASH========||":
    print(MenuList[3])
    a2 = int(input("||ENTER AMMOUNT||:$ "))
    if balance >= a2:
      print("||>>TRANSACTION-SUCCESFULL<<||")
      balance = balance-a2
      print("||YOUR BALANCE NOW|:$",balance)
    else:
      print("||>>>-TRANSACTION-FAILED-<<<||")
      print("||YOUR BALANCE LOW||")
      
#TRANSFER FUNCTION-
  elif a == "||=====TRANSFER=============||":
    print("="*30)
    print("|"*2,"_______BANK LIST________","|"*2)
    sleep(.50)
    print("|"*2,"______1.WOLRD BANK______","|"*2)
    sleep(.50)
    print("|"*2,"______2.BANK OF SOUP____","|"*2)
    sleep(.50)
    print("|"*2,"______3.BANK OF BANK____","|"*2)
    sleep(.50)
    print("|"*2,"______4.BACK____________","|"*2)
    sleep(.50)
    print("|"*2,"_____CHOOSE-THE-BANK____","|"*2)
    
    a3 = int(input("==============================\n||ENTER NUMBER||:"))
    if a3 == 1:
      print("|"*2,"=======WORLD-BANK=======","|"*2)
      x = int(input("||ENTER ACCOUNT NUMBER||:\n||>>> "))
      x1 = int(input("||ENTER AMMOUNT||:"))
#####################################      
      if balance >= x1:
        print("||>>TRANSACTION-SUCCESFULL<<||")
        balance = balance-x1
        print("||YOUR BALANCE NOW|:$",balance)
      else:
        print("||>>>-TRANSACTION-FAILED-<<<||")
        print("||YOUR BALANCE LOW||")
        
####################################        
    elif a3 == 2:
      print("||=======BANK OF SOUP=======||")
      x2 = int(input("||ENTER ACCOUNT NUMBER||:\n||>>> "))
      x3 = int(input("||ENTER AMMOUNT||:"))
      
      if balance >= x3:
        print("||>>TRANSACTION-SUCCESFULL<<||")
        balance = balance-x3
        print("||YOUR BALANCE NOW|:$",balance)
      else:
        print("||>>>-TRANSACTION-FAILED-<<<||")
        print("||YOUR BALANCE LOW||")
        
#######################################    
    elif a3 == 3:
      print("||=======BANK OF BANK=======||")
      x4 = int(input("||ENTER ACCOUNT NUMBER||:\n||>>> "))
      x5 = int(input("||ENTER AMMOUNT||:"))
      
      if balance >= x5:
        print("||>>TRANSACTION-SUCCESFULL<<||")
        balance = balance-x5
        print("||YOUR BALANCE NOW|:$",balance)
      else:
        print("||>>>-TRANSACTION-FAILED-<<<||")
        print("||YOUR BALANCE LOW||")
        
    elif a3 == 4:
      print("||===========BACK===========||")
          

#EXIT FUNCTION
  elif a == "||===========EXIT===========||":
    print(MenuList[5])
    print("||PROGRAMMED BY RAHFI||\n||THANKS FOR TRYING||")
    print("="*30)
    break
    exit()