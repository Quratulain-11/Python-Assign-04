def main():

   input_temp = float(input("Enter temperature in Fahrenheit: "))

   user_input = (input_temp - 32) * 5.0 / 9.0
   
   print(f'Temperature = {input_temp}F = {user_input}C')


if __name__ == '__main__':
    main()




