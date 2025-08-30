from random import shuffle

ages = list(range(16, 30))
shuffle(ages)
ages = 
def main():
    print("Hello! I'm the all knowing BITLORD, and I'll try to guess your age!")
    name = input("What's your name yo? ")
    for i in ages:
        answer = input("Are you " + str(i) + " years old (y/n)? ")
        if answer == 'y':
            print(name + " is " + str(i) + " years old.")
            break
        print("Rats.\n")
    if answer != 'y':
        print("Not your average college student huh?")

main()
