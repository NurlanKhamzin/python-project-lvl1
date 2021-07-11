import operator
import random
from random import randrange

GAME_RULE = "What is the result of the expression?"


def generate_question_answer():
    num1 = randrange(99)
    num2 = randrange(99)
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    op = random.choice(list(ops.keys()))
    task = str(num1) + " " + str(op) + " " + str(num2)
    correct_answer = str(ops.get(op)(num1, num2))
    return task, correct_answer


if __name__ == '__main__':
    generate_question_answer()
