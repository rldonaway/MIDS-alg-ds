# Assignment 2, #1
#
# a. Given two messages, A and B, which have the same length, we can
# create a new message by taking the first character from A, then the first
# character from B, then the second character from A, then the second
# character from B, and so on. We’ll call this the interleave of A and B.
# For example, if A is the text “abcde” and B is the text “12345” the
# interleave of A and B is “a1b2c3d4e5”.
# Write a function, interleave(), that takes two strings of the same length
# and returns the interleave of the two.
# b. To make a message even harder to read, we can perform several
# interleaves in a row. Assume that the length of a message is a power of
# 2. We define the scramble of the message recursively as follows:
# 1. The scramble of a single character is just that character.
# 2. The scramble of a longer message is found by taking the scramble
# of the first half of the message and the scramble of the second half
# of the message, and interleaving them.


def interleave(msg_a, msg_b):
    len_a = len(msg_a)
    len_b = len(msg_b)
    if len_a != len_b:
        raise ValueError("messages are not the same length")

    result = ""
    for i in range(len_a):
        result += msg_a[i]
        result += msg_b[i]

    return result


# print(interleave("abc", "123"))


def length_power_two(message):
    msg_len = len(message)
    power_of_two = 1;
    while power_of_two < msg_len:
        power_of_two = 2 * power_of_two

    for i in range(msg_len, power_of_two):
        message += "."

    return message


# print(length_power_two(""))
# print(length_power_two("a"))
# print(length_power_two("ab"))
# print(length_power_two("abc"))
# print(length_power_two("abcd"))
# print(length_power_two("abcde"))
# print(length_power_two("abcdef"))


def scramble(message):
    if len(message) < 1:
        return message
    return scramble_recur(length_power_two(message))


def scramble_recur(message):
    msg_len = len(message)
    if msg_len < 2:
        return message

    half_msg_len = msg_len // 2
    first_half = message[:half_msg_len]
    second_half = message[half_msg_len:]

    return interleave(scramble_recur(first_half), scramble_recur(second_half))


# print(scramble(""))
# print(scramble("1"))
# print(scramble("12"))
# print(scramble("1234"))
# print(scramble("12345678"))
# print(scramble("hello"))
# print(scramble("Madam I'm Adam"))


def scramble_file():
    file_to_scramble = open("input.txt", "r")
    scrambled_file = open("output.txt", "w")
    for line in file_to_scramble.readlines():
        scrambled = scramble(line[:-1])
        scrambled_file.write(scrambled + "\n")
    scrambled_file.close()
    file_to_scramble.close()


if __name__ == "__main__":
    scramble_file()