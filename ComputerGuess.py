import random
import time
number = random.randint(0, 10)
goal = int(input("Think a number, my pal: "))
choices = 1
print(number)
while number != goal:
    if goal > number:
        print("sorry, too low")
    if goal < number:
        print("sorry, too high")
    number = random.randint(0, 10)
    print(number)
    choices += 1
    time.sleep(2)
if number == goal:
    print(f'The computer lasted {choices} tries to achieve the number')