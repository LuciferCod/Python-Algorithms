#python 3
#Lucifer Coder FizzBuzz Code

#input

number = int(input("Enter Number: "))

#Check for divisibility

if number%3 == 0:
    output = str("Fizz")

if number%5 == 0:
    output = str("Buzz")

if number%5 == 0 and number%3 == 0:
    output = str("FizzBuzz")

if number%5 != 0 and number%3 != 0:
    output = str("Neither")


#output

print(output)
