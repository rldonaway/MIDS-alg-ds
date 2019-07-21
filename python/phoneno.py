# Write a script that prompts the user for their phone number, x. Then carry out the following steps:
#
# 1. Compute x minus the sum of the digits of x. Call this result y.
#       (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)
# 2. Compute the sum of the digits of y, and store the result back in y.
# 3. Repeat step 2 until y has just one digit, then display it.
#
# What answer do you get?


def sum_of_digits(integer: int) -> int:
    result = 0
    while integer > 0:
        digit = integer % 10
        result += digit
        integer = integer // 10
    return result


print(sum_of_digits(123))
print(sum_of_digits(0))
print(sum_of_digits(1))
print(sum_of_digits(10))

x = int(input("what is your phone number?"))
y = x - sum_of_digits(x)
print("starting y", y)
while y // 10 > 0:
    y = sum_of_digits(y)
    print("current y", y)
print("answer y", y)