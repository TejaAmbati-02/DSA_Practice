# find leap year or not
year = int(input("Enter the year : "))
if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print("Leap Year")
else:
    print("Not Leap Year")

# Take two numbers and print the sum of both
num1 = int(input())
num2 = int(input())
print(num1 + num2)


# Take a number as input and print the multiplication table for it.
number = int(input("Enter the number to print the program"))
for i in range(1, 21):
    print(f"{number} * {i} = {number * i}")


# Take 2 numbers as inputs and find their HCF and LCM.
def compute_lcm_and_hcf(x, y):
    if x == 0 or y == 0:
        return float('inf'), max(x, y)
    elif x < 0 or y < 0:
        x, y = abs(x), abs(y)

    def hcf(x, y):
        while y:
            x, y = y, x % y
        return x

    h = hcf(x, y)
    l = (x * y) // h

    print("LCM is ", l)
    print("HCF is ", h)

# Example usage


number1 = int(input())
number2 = int(input())
compute_lcm_and_hcf(number1, number2)


# Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
def sum_of_numbers():
    total_sum = 0
    while True:
        number = input("Enter a number or 'x' to exit: ")
        if number == 'x':
            break
        try:
            total_sum += float(number)
        except ValueError:
            print("Please enter a valid number.")
    return total_sum


print("Total Sum:", sum_of_numbers())
