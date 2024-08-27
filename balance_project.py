class ruhul:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.u_in()
    def u_in(self):
        print("""
            Hi! How can I help you 
            1. press 1 to create pin code
            2. Press 2 to Check your balance
            3. Press 3 to Balane Withdraw
            4. Press 4 change your pin code
            5. Press 5 to  exit
        """)
        ch=input('Enter your choice : ')
        if ch=='1':
            self.create_pin()
        elif ch=='2':
            self.check_bal()
        elif ch=='3':
            self.bal_wi()
        elif ch=='4':
            self.pin_ch()
        else:
            exit()
        

    def create_pin(self):
        p = int(input("Enter new pin code at least 6 digit : "))
        self.pin=p
        if self.pin<6: 
            print("Pin code at least 6 digits")
            self.create_pin()

        bl= int(input("Enter your balance : "))
        self.balance=bl
        print("Pin create successfully") 
        self.u_in()    


    def check_bal(self):
        print('current Balane is : ',self.balance)    
        self.u_in()


    def bal_wi(self):
        amount=int(input("Enter the amount : "))
        if amount>self.balance:
            print("You have insuficient balance")
            self.bal_wi()
        else:
            self.balance=self.balance - amount
            print("Balance withdrawed successfully")
        self.u_in()


    def pin_ch(self):
        old_p=int(input("Enter your old pin code : ")) 
        if old_p ==  self.pin:
            new_p = int(input("Enter your new pin : "))
            self.pin=new_p
            print("Pin changed success")
        else:
            print("Please give your old pin correctly")
            self.pin_ch()
        self.u_in()



ob=ruhul()