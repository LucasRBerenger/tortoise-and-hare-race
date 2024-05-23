import random
import time
import os

def tortoiseMovement():
    value = random.randint(1, 10)

    if value <= 5:
        return 3
    elif value > 5 and value <= 7:
        return -6
    else:
        return 1

def hareMovement():
    value = random.randint(1, 10)

    if value <= 2:
        return 0
    elif value > 2 and value <= 4:
        return 9
    elif value == 5:
        return -12
    elif value > 5 and value <= 8:
        return 1
    else:
        return -2
    
def validationLimits(position):
    if position < 1:
        return 1
    if position > 70:
        return 70
    return position
    
def track(tortoisePosition, harePosition):
    for position in range(1, 71):
        if position == tortoisePosition and position == harePosition:
            print("OUCH!!!", end="")
        elif position == tortoisePosition:
            print("T", end="")
        elif position == harePosition:
            print("L", end="")
        else:
            print("=", end="")

harePosition = 1 
tortoisePosition = 1

print("\n\nBANG!! AND THEY'RE OFF!!!\n\n")
time.sleep(0.8)

while tortoisePosition < 70 and harePosition < 70:
    tortoisePosition += tortoiseMovement()
    tortoisePosition = validationLimits(tortoisePosition)
    harePosition += hareMovement()
    harePosition = validationLimits(harePosition)

    track(tortoisePosition, harePosition)
    print()
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')

        
if tortoisePosition >= 70:
    print("\nTORTOISE WINS!!! YAY!!!\n")
else:
    print("\nHARE WINS!!! YUCH!!!!\n")




    
