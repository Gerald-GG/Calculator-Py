def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # check if divisor is zero to avoid division by zero error
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
# Display menu to user
print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# ask user for inputs until they choose to exit
while True:
    # get user's choice of operation
    choice = input("Enter choice (1/2/3/4): ")

    # Perform selected operation based on user input
    if choice in ('1', '2', '3', '4'):
        #get numbers from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # perform selected operation and display the result
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")


    # ask user if they want to perform  another calculation
    next_calculation = input("Do you want to perform  another calculation? (yes/no): ")
    if next_calculation.lower() != "yes":
        break #exit loop if user does not want to continue