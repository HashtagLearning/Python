num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which would you like to perform?")
ab = input("Enter any of these specific operation +,-,*,/: ")

result = 0
if ab == '+':
    result = num1 + num2
elif ab == '-':
    result = num1 - num2
elif ab == '*':
    result = num1 * num2
elif ab == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ab , num2, ":", result)
