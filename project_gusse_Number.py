import random

a = random.randint(1,100)

i = -1

while(i!=a):
    n = int(input("Enter the > G u s s i n g ! < Number : "))

    if (n == a ):
        print("    > P e r f e c t___G u s s ! < ")
        print(f"the random number is {a}")
        break
    
    elif (n > a):
        print("Give the > L o w e r ! < Number ..")
        print("keep trying \n")
            
    elif (n < a):
        print(" Give the > L a r g e r ! < Number ..\n")
        print("Keep trying \n")
        

        