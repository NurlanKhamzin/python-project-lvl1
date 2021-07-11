import operator
import random
from random import randrange

GAME_RULE = "What is the result of the expression?"


def generate_question_answer():
    num1 = randrange(99)
    num2 = randrange(99)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    chosen_operator = random.choice(list(operators.keys()))
    task = f"{num1} {chosen_operator} {num2}"
    correct_answer = str(operators.get(chosen_operator)(num1, num2))
    return task, correct_answer
