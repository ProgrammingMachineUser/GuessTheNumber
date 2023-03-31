import random
import time
number = random.randint(0, 1000000)
trying = int(input("Guess the number, my pal: "))
choices = 1
while trying != number:
    if trying < number:
        print("sorry, too low")
    if trying > number:
        print("sorry, too high")
    trying = int(input('wrong, guess again:'))
    choices += 1
    time.sleep(1)
else:
    print(f"Right answer, you've won in {choices} tries")