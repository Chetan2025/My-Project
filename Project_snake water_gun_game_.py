#snake water gun game ............................................
'''snake = s = 0 
   water = w = 1 
   gun = g = 2'''
import random
dis = { "s" : 0 , "w" : 1 ,"g" : 2 }
reverse_dis = { 0 : "s" , 1 : "w" , 2 : "g"}
i = 1
for i in range (1 , 5):
   computer = random.choice ([0,1,2])
   you = input("Enter S for snake \nEnter W for water\nEnter G for gun \t ") 
   you = dis[you]
   print("\n")
   print(f"You chose     : {reverse_dis[you]}")
   print(f"Computer chose: {reverse_dis[computer]}")
   print("\n")

   # else:
   #  if (computer == -1 and u == 0):
   #      print("you lose ")
   #  elif (computer == -1 and u == 1):  ----------- 01 
   #      print(" you win ")
   #  elif (computer == 1 and u == 0):----------------- 02   this are winnig logic of win 
   #      print(" you win ")
   #  elif (computer == 0 and u == -1 ):-------------  03
   #      print(" you win ")
   #  elif (computer == 0 and u == 1):
   #      print(" you lose ")
   #  elif (computer == 1 and u == -1):
   #      print("you lose ")
   # if (computer == you):
   #    print("itz DRAW")
   if (computer == you):
      print("itz   D R A W")
   elif ( computer == 0 and you == 2 ) or ( computer == 1 and you == 0 ) or  (computer == 2 and you == 1 ):
      print("you   W I N !")
   
   else:
      print("you   L O S E ! ")
   print(" "," ")


      



















      
