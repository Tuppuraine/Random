import random
import secrets
from collections import Counter
import matplotlib.pyplot as plt

def begin(start: int, end: int, times: int, generator):

    numbers = []

    for i in range (0, times-1):
        numbers.append(generator(start, end+1)) #appends randomized numbers to list

    counted = Counter(numbers) #counts how many times a number appears in list and makes a dictionary 

    arranged = dict(sorted(counted.items())) #arranges the dictionary

    numbers = list(arranged.keys())
    arranged_times = list(arranged.values())

    printout(numbers, arranged_times)

def pseudogenerator(start: int, end: int):

    return random.randint(start, end)

def secretgenerator(start: int, end: int):
    
    return secrets.choice(range(start, end))

def printout(numbers: list, arranged_times: list):

    plt.bar(numbers, arranged_times, color ='pink')

    plt.xlabel(f"Randomized numbers, randomized {len(arranged_times)-1} times")
    plt.ylabel("Times appeared")
    plt.title(f"Randomized numbers")
    plt.show()
 
    #for number in arranged:
    #    print (f"Number {number}, was generated {arranged[number]} times")


def main():
    while True:
        try:
            print("This program randomizes numbers between given range")
            start = int(input("Input beginning of range: "))
            end = int(input("Input the end of range: "))
            if end <= start:
                print("End of range needs to be bigger than start")
                continue
            times = int(input("How many times do you want to randomize a number in range: ")) + 1
            break
        except ValueError:
            print("Please input integer only")
    while True:
        try:
            generator = int(input("Would you like to use pseudo random[1] or secret library[2]? Input 1 or 2: "))
            if generator == 1:
                begin(start, end, times, pseudogenerator)
                break
            elif generator == 2:
                begin(start, end, times, secretgenerator)
                break
        except ValueError:
            print("Please input 1 or 2")

    while True:        
        again = input("Again? [Y/N]: ")
        if again == "Y" or again == "y":
            main()
        else:
            break

main()