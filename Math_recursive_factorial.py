def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
try:
    number = int(input("Please enter a number to calculate factorial: "))
    print("Your factorial from number {} is equal: {}".format(number,factorial(number)))
except ValueError:
    print("You must enter an integer number!")