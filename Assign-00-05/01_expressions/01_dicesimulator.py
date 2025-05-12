import random 

num_sides = 6

def roll_sides():

    die1 : int = random.randint(1 , num_sides)
    die2 : int = random.randint(1 , num_sides)
    total = die1 + die2 
    print(f'Total of two dice is {total}')


def main():
        die1 : int = 10
        print(f'die1 in main is start as ss{die1}')
        roll_sides()
        roll_sides()
        roll_sides()
        print(f'die1 in main is {die1}')


if __name__ == '__main__':
    main()        