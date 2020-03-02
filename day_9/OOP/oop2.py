class Customer:
    def __init__(self,firstName,lastName,Age):
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        
    def myOutput(self):
        print(self.firstName)
    
brian = Customer('Brian','Kiprotich',20)
peter = Customer('Peter','wafula',25)
brian.myOutput()
    