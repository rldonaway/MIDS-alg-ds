# Write a script to compute how many unique prime factors an integer has.
# For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3.
# Use your script to compute the number of unique prime factors of 1234567890.


def unique_prime_factors(intVal):
    count = 0
    remainder = intVal
    prime = 2
    while remainder > 1:
        found_prime = False
        while remainder % prime == 0:
            found_prime = True
            remainder = remainder / prime
        if found_prime:
            count += 1
            print(prime, "is a factor")
        prime += 1
    return count


print("there are", unique_prime_factors(1234567890), "factors")
