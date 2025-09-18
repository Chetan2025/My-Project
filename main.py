import datetime
import time
import random

current_time = datetime.datetime.now()

class Fuel:
    def __init__(self,petrol,diesel,cng):
        self.petrol = petrol
        self.diesel = diesel
        self.cng =   cng
        self.amount = [104.16,90.72,77.00]
        

    def petrol_add(self,quintity):
        if quintity > self.petrol:
            print("|-----------------------------------------------------------|")
            print("|                The Quantity is Not Available              |")
            print("|-----------------------------------------------------------|")
            return 

        self.petrol-= quintity
        total = quintity * self.amount[0]
        return total

    def diesel_add(self,quintity):
        if quintity > self.diesel:
            print("|-----------------------------------------------------------|")
            print("|                The Quantity is Not Available              |")
            print("|-----------------------------------------------------------|")
            return 

        self.diesel -= quintity
        total = quintity * self.amount[1]
        return total 

    def cng_add(self,quintity):
        if quintity > self.cng:
            print("|-----------------------------------------------------------|")
            print("|                The Quantity is Not Available              |")
            print("|-----------------------------------------------------------|")
            return 

        self.cng -= quintity
        total = quintity * self.amount[2]
        return total
    
    def show(self): #inventry of fuel  
        print("\n-----------------------------------------------------------")
        print(f"Now the petrol in the tank is : {self.petrol} litre")
        print(f"Now the diesel in the tank is : {self.diesel} litre")
        print(f"Now the cng in the tank is    : {self.cng}    kg")
        print("\n-----------------------------------------------------------")

    def Bill(self,total): #print bill details 

        print("-----------------------------------------------------------")
        
        print("|-----------------------------------------------------------|")
        print("|                GENRATING BILL PLEASE WAIT.....            |")
        print("|-----------------------------------------------------------|")

        time.sleep(2)
        print(f"""
        |------------------------------------------------------------------|
        |--------------------------- BILL ---------------------------------|
        |----------------Indian Oil Corporation Limited--------------------|  
        |                Date     : {current_time.strftime("%Y-%m-%d")}    
        |                Time     : {current_time.strftime("%H:%M:%S")}    
        |                Bill No. : {random.randint(1000,9999)}            
        |------------------------------------------------------------------|
        |  type of fuel            price per litre/kg           density    |
        |------------------------------------------------------------------|
        | 1. Petrol                         {total[0]}          733.3 kg/m3   
        | 2. Diesel                         {total[1]}          825.00 kg/m3  
        | 3. CNG                            {total[2]}          193.2 kg/m3      
        |      
        |------------------------------------------------------------------|\n
        | Total amount to be paid :        {sum(total)} Rs.                   
        |------------------------------------------------------------------|
        |                "Thank you for using our service"                 |
        |------------------------------------------------------------------|\n
        """)

        


#----------------------------------------------------------------------------------------
print("|-----------------------------------------------------------|")
print("|                FUEL MANAGMENT SYSTEM                      |")
print("|-----------------------------------------------------------|\n")

print("""   
      |---------------------------------------------------------------|
      |          There are three types of Fuel available :            |          
      |---------------------------------------------------------------|
      |type of fuel         price per litre/kg       density          |
      |---------------------------------------------------------------|
      | 1. Petrol             104.16 /liter           733.3 kg/m3     |
      | 2. Diesel             90.72 /liter            825.00 kg/m3    |
      | 3. CNG                77.00 /kg               193.2 kg/m3     |
      | 4. Show fuel inventry                                         |
      | 5. Exit                                                       |
      |---------------------------------------------------------------|
      |---------------------------------------------------------------|
      \n""")

obj = Fuel(10000.00,7000.00,200.00)


while True : 

    print("|-----------------------------------------------------------|")
    print("|Enter the number of fuel type you want to Add :            | ")
    print("|-----------------------------------------------------------|")
    n = int(input("...........\t "))
        
    if n in [1,2,3]:

        print("-----------------------------------------------------------")
        quintity = float(input("Enter the quantity you want to Add :\t  "))
        print("-----------------------------------------------------------")

        if n == 1:
            total = obj.petrol_add(quintity)
            if total is not None:
                obj.Bill([total,0.00,0.00])
            

        elif n == 2:
            total = obj.diesel_add(quintity)
            if total is not None:
                obj.Bill([0.00,total,0.00])
            
        elif n == 3:
            total = obj.cng_add(quintity)
            if total is not None:
                obj.Bill([0.00,0.00,total])

    elif n == 4:
        obj.show()

    elif n == 5:
        print("|-----------------------------------------------------------|")
        print("|           Thank you for using our Service                 |")
        print("|-----------------------------------------------------------|")
        break

    else:
        print("|-----------------------------------------------------------|")
        print("|                    Invalid, select another option  !      |")
        print("|-----------------------------------------------------------|")