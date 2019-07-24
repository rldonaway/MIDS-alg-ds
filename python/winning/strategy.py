def is_hot(N):
    if N < 2:
        return False
    one_less_hot = is_hot(N-1)
    half_hot = is_hot(N/2)
    return not (one_less_hot and half_hot)


# print(is_hot(1))
# print(is_hot(2))
# print(is_hot(3))
# print(is_hot(4))


def bool_to_word(bool):
    if bool:
        return "hot"
    return "cold"


def strategy_file():
    file_of_states = open("input.txt", "r")
    file_of_outcomes = open("output.txt", "w")
    for line in file_of_states.readlines():
        outcome = is_hot(int(line[:-1]))
        file_of_outcomes.write(bool_to_word(outcome) + "\n")
    file_of_outcomes.close()
    file_of_states.close()


if __name__ == "__main__":
    strategy_file()