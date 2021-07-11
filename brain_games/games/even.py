from random import randrange

GAME_RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\""


def is_even(n):
    if (n % 2) == 0:
        return True


def generate_question_answer():
    task = randrange(99)
    correct_answer = "yes" if is_even(task) else "no"
    return task, correct_answer


if __name__ == '__main__':
    generate_question_answer()
