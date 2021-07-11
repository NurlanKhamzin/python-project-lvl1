from random import randrange
import math

GAME_RULE = "Find the greatest common divisor of given numbers."


def generate_question_answer():
    num1 = randrange(99)
    num2 = randrange(99)
    task = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return task, correct_answer
