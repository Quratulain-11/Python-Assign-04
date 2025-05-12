
inches_in_foot : int = 12

def main():
    feet : int = int(input('Enter number of feet:'))
    inches : int = feet * inches_in_foot
    print(f'That is {inches} inches !')

if __name__ == '__main__':
    main()    