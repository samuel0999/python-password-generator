# Random password generator
import random

user_input = input("Enter 'yes' to generate password or 'q' to quit:")

if user_input.lower() != "yes":
    quit()

print("Let's generate :)")

chars = "qwertzuioasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890{}[]@.?-_()!''/|"

password = ""

# Password digits
digits = int(input("Enter how many digits for password:"))

for i in range(digits):
    password += random.choice(chars)

print("You'r generated password is:")
print(password)