from tabnanny import check


class Cust:
    formType = "Bank Account Details ."
    
    def inputData(self):
        self.name = str(input("Enter the name : "))
        self.age = int(input("Enter the age : "))
        self.account = int(input("Enter Account Number : "))
        self.balance = int(input("Enter the Balance : "))
        
    def checkavail(self):
        check = int(input("Enter Acoount Number to check : "))
        if self.account != check:    
            print("Customer not found in record.")
        else:
            print("Customer found in record.")    
    
    def creditscore(self):
        if self.balance <= 100:
            print("The customer has low credit score.")
        else:
            print("The Credit Score of the customer is good.")
                
        
print("-:Enter Data of Customers:-")        
        
data = Cust()
i = 5
for i in range(0 , 5):
    i = i + 1
    print(str(i))
    data.inputData()
    
data.checkavail()
data.creditscore()