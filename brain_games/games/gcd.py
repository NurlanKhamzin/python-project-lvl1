from random import randrange
import math

GAME_RULE = "Find the greatest common divisor of given numbers."


def game_logic():
    num1 = randrange(99)
    num2 = randrange(99)
    num = '{0} {1}'.format(num1, num2)
    correct_answer = str(math.gcd(num1, num2))
    return num, correct_answer


if __name__ == '__main__':
    game_logic()
