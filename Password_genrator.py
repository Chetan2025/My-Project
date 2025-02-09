#this program help to gernrate random PASSWORD ......................
import random
import string

password = ""
print("welcome to random password genrated")
n = int(input("""Enter how many ALPHABETES you want in your password\t """))
n1 = int(input("""Enter how many SPICEAL CARECTOR you want in your password\t """))
n2 = int(input("Enter how many NUMBERS you want in your password \t"))

random_alphabet = random.choice(string.ascii_uppercase)
password += random_alphabet
for _ in range(n):
    random_alphabet = random.choice(string.ascii_lowercase)
    password += random_alphabet
for _ in range(n1):
    sp = random.choice(["@" , "#" , "$" , "%" , "&" , "*"])
    password += sp
for _ in range(n2):
    num = random.choice([1,9])
    password += str(num)

print(f"Your Password Was genratedn : {password}")


