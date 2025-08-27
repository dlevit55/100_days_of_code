#!/usr/bin/env python3

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print("your password is: ")
random_list = []
for letter in range(nr_letters):
    list_random_letter = random.randint(0, 51)
    #print(letters[list_random_letter], end = '')
    random_list.append(letters[list_random_letter])
for symbol in range(nr_symbols):
    list_random_symbol = random.randint(0, 8)
    #print(symbols[list_random_symbol], end = '')
    random_list.append(symbols[list_random_symbol])
for number in range(nr_numbers):
    list_random_number = random.randint(0, 9)
    #print(numbers[list_random_number], end = '')
    random_list.append(numbers[list_random_number])

#print(random_list)
random.shuffle(random_list)
print("".join(random_list))


