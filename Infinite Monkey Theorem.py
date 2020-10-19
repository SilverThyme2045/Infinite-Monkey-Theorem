import random
import sys
import string
while True:
    number = input("Enter a number: ")
    try:
        val = int(number)
        if val <=0:
            print("Sorry, input must be a positive integer, try again")
            continue
        break
    except ValueError:
        print("That's not an int!")    
number=int(number)
print("Starting Monkey Now:")
x=0
while (True):
    x=x+1
    if x>number:
        break
    sys.stdout.write((string.ascii_letters+" ")[random.randint(0, 52)])
