from random import randrange

GAME_RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\""


def is_even(n):
    if (n % 2) == 0:
        return True


def game_logic():
    num = randrange(99)
    correct_answer = "yes" if is_even(num) else "no"
    return num, correct_answer


if __name__ == '__main__':
    game_logic()
