import math

def main():

    ab : float = float(input('Enter the number of AB :'))
    ac : float = float(input('Enter the number of AC : '))

    bc : float = math.sqrt(ab**2 + ac**2)

    print(f'The length of BC (the hypotenuse) is: {bc}')

if __name__ == '__main__':
    main() 