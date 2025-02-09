'''Rock = R    = 0 
   Paper = P   = 1 
   Scissor = S = 2'''
import random
dis = { "r" : 0 , "p" : 1 ,"s" : 2 }
reverse_dis = { 0 : "Rock" , 1 : "Paper" , 2 : "Scissor"}

for i in range (1 , 5):
   computer = random.choice ([0,1,2])
   you = input("Enter R for Rock \nEnter p for paper\nEnter s for Scissos \t ") 


   
   if (computer == you):
      print("itz DRAW")
   you = dis[you]
   print("\n")
   
   print(f"You chose     : {reverse_dis[you]}")
   print(f"Computer chose: {reverse_dis[computer]}")
   print("\n")
   # else:
   #  if (computer == 1 and u == 0):
   #      print("you lose ")
   #  elif (computer == 0 and u == 2):----------- 01 
   #      print(" you win ")
   #  elif (computer == 1 and u == 2):----------------- 02   -- (1,2,3) this are winnig logic of win 
   #      print(" you win ")
   #  elif (computer == 2 and u == 0 ):-----------03
   #      print(" you win ")
   #  elif (computer == 0 and u == 1):
   #      print(" you lose ")
   #  elif (computer == 2 and u == 1):
   #      print("you lose ")
   # if (computer == you):
   #    print("itz DRAW")

   if (computer == you):
      print("itz   D R A W")
   elif (computer == you) or ( computer == 0 and you == 1 ) or ( computer == 1 and you == 2 ) or  (computer == 2 and you == 0 ):
      print("you   W I N")
   
   else:
      print("you   L O S E ")
   print(" ")
   print("----------------------------------------------------- ")
   print(" ")

