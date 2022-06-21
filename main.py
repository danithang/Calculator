from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2
    
#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

#making a dictionary for operators, keys are the operations and values are the functions name
operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}
def calculator():
    #print logo in function so when user chooses to start over the calculator logo will appear
    print(logo)
    first_number = float(input("What's the first number?: "))

    #printing the keys in the dictionary which are the symbols representing operators
    for key in operations:
        print(key)
#adding while loop to see if should_contine will equal true or false depending on user answer, will repeat as long as user answers yes
    should_continue = True
    while should_continue:
        operator_choice = input("Choose an operator: ")
        next_number = float(input("What's the next number?: "))
        #tap into operations dictionary and pass in operator_choice 
        calculation_function = operations[operator_choice]
        #adding the num1 and num2 inputs to calculation_function variable to    input whatever operator user chooses from operator_choice variable
        answer = calculation_function(first_number, next_number)
        print(f"{first_number} {operator_choice} {next_number} = {answer}")
        #adding if statement to answer whether user wants to continue or not
        if input(f"Would you like to continue with the calculation of {answer}? Type 'yes' or to start over type 'no': \n").lower() == "yes":
        #answer will have to replace the first number in order to get a different answer each time to use with next_number
            first_number = answer
        else:
            should_continue = False
            calculator()

calculator()

        
    

    


