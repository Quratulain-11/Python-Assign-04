def main():
    print ('Hey, lets add perimeters ')

    perimeter1 = float(input('What is the length of side 1? '))
    perimeter2 = float(input('What is the length of side 2? '))
    perimeter3 = float(input('What is the length of side 3? '))

    sum = perimeter1 + perimeter2 + perimeter3

    print(f'perimeter of triangle is = {sum}')

if __name__ == '__main__':
     main()