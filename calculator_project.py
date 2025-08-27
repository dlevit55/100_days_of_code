#!/usr/bin/env python3

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+" : add, "-" : subtract, "*" : multiply,"/" : divide}

def one_try():
    print("+\n-\n*\n/")
    math_operator = input("Pick an operation from above: ")
    second_num = int(input("What's the second number?: "))

    calculated_sum = operations[math_operator](first_num,second_num)
    print(f"{float(first_num)} {math_operator} {float(second_num)} = {float(calculated_sum)} ")
    print("the sum is: ", calculated_sum)
    return calculated_sum

first_num = int(input("What's the first number?: "))
one_try_result= one_try()
keep_going = True
while keep_going:

    user_choice = input(f"Type 'y' to continue calculating with {one_try_result}, or type 'n' to start a new calculation ")

    if user_choice == "n":
        first_num = int(input("What's the first number?: "))
        one_try()
    elif user_choice == "y":
        first_num = one_try_result
        one_try()
    else:
        print("Wrong input")
        keep_going = False



