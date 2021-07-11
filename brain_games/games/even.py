from random import randrange

GAME_RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\""


def is_even(n):
    return (n % 2) == 0


def generate_question_answer():
    task = randrange(99)
    correct_answer = "yes" if is_even(task) else "no"
    return task, correct_answer
