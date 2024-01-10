# # Write a program to print whether a number is even or odd, also take input from the user.
# value = int(input())

# if (value % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

# # Take name as input and print a greeting message for that particular name.
# string_value = input("Enter the string as input")
# print(f"Hi! {string_value}")

# # Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.
# p_value = int(input())
# t_value = int(input())
# r_value = int(input())

# SI = (p_value * t_value * r_value)/100
# print(SI)

# # Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
# value_1 = int(input())
# value_2 = int(input())
# string_input = input("Enter ADD to 'add 2 numbers' \
#     'Enter SUB to 'subtract 2 numbers' \
#     'Enter SUB to 'subtract 2 numbers' \
#     'Enter MUL to 'multiplication 2 numbers' \
#     'Enter DIV to divide 2 numbers'")
# if (string_input == 'ADD'):
#     print(value_1 + value_2)
# elif (string_input == 'SUB'):
#     print(value_1 - value_2)
# elif (string_input == 'MUL'):
#     print(value_1 * value_2)
# elif (string_input == 'DIV'):
#     if (value_1 > value_2):
#         print(value_1/value_2)
#     else:
#         print(value_2/value_1)

# # Take 2 numbers as input and print the largest number.
# value_1 = int(input())
# value_2 = int(input())

# if (value_1 > value_2):
#     print(f"{value_1} is larger")
# else:
#     print(f"{value_2} is larger")

# # Input currency in rupees and output in USD.
# value = int(input())
# CURRENT_CURRENCY_RATE = 80
# print(value * CURRENT_CURRENCY_RATE)
# To calculate Fibonacci Series up to n numbers.
# 0,1,1,2,3,5,8,13,21,34

# a = 0
# b = 1
# n = int(input())

# print(str(a) + " " + str(b) + " ", end=" ")
# # c <- a+b, a <- b, b <- c

# for i in range(2, n):
#     c = a + b
#     print(str(c), end=" ")
#     a = b
#     b = c

# print()
# # To find out whether the given String is Palindrome or not.
# # MADAM = MADAM -> Palindrome

# string_input = input("Enter the string to find palindrome or not: ")
# if (string_input == string_input[::-1]):
#     print(f"{string_input} String is Palindrome")
# else:
#     print(f"{string_input} String is not a Palindrome")

# To find Armstrong Number between two given number.


def is_armstrong(number):
    power = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp //= 10
    return number == sum


def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for number in range(start, end + 1):
        if is_armstrong(number):
            armstrong_numbers.append(number)
    return armstrong_numbers


start_number = int(input("First Value"))
end_number = int(input("Second value"))
print(find_armstrong_numbers(start_number, end_number))
