import random 
import time

# Initializing required strings
string = input("Enter the string: ")
found = ""

# Using a while loop to control its flow accordingly
i = 0
while i < len(string):
    char = string[i]

    # Skiping the spaces in the string
    if char == " ":
        found += " "
        i += 1
        continue

    # Get random character in form of ASCII value
    ascii = random.randint(0,25) + 97

    # Compare the random letter with correct letter in the string
    if chr(ascii) == char:
        # Increment i if correct letter was found and add it to found string
        i += 1
        found += char
        print(found)

    # If the random letter is not correct we still print it but don't move to next letter
    else:
        print(found + chr(ascii))

    # Waiting for a small amount of time to get that nice affect
    time.sleep(0.04)
