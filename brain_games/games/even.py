from random import randrange

game_rule = "Answer \"yes\" if the number is even, otherwise answer \"no\""


def is_even(n):
    if (n % 2) == 0:
        return True


def game_logic():
    num = randrange(99)
    is_correct = "yes" if is_even(num) else "no"
    return num, is_correct


if __name__ == '__main__':
    game_logic()
