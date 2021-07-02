from random import randrange

GAME_RULE = "Answer \"yes\" if the number is prime, otherwise answer \"no\""


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def game_logic():
    num = randrange(99)
    correct_answer = "yes" if is_prime(num) else "no"
    return num, correct_answer


if __name__ == '__main__':
    game_logic()
