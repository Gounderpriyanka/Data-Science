class bank :
    balance =25000 
    pin  = 1234
    def deposit(self):
        
        num = int(input("Enter the pin: "))
        if self.pin == num:
            amt = int(input("Enter the deposit amount: "))
            self.balance  +=amt
            print("deposited successfully")
        else :
            print("The pin is incorrect!")

        
    
    def withdraw(self):
        num = int(input("Enter the pin: "))
        if self.pin == num:
            amt = int(input("Enter the withdraw amount: "))
            if self.balance -amt >=10000 :  
                self.balance -=amt
                print("withdrawed successfully")
            else :
                print("min balance required 10000")
        else:
            print("Pin is incorrect!")


    def display(self):
        print("balance : ",self.balance)

b = bank()
b.deposit()
b.withdraw()
b.display()