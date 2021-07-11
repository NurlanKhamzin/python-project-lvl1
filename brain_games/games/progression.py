from random import randint, randrange

GAME_RULE = "What number is missing in the progression?"


def generate_progression():
    progression = []
    checker = []
    a1 = randint(1, 10)
    d = randint(1, 10)
    for i in range(10):
        formula = a1 + (i - 1) * d
        progression.append(formula)
        checker.append(formula)
    random = randrange(len(progression))
    progression[random] = '..'
    progression = ' '.join([str(n) for n in progression])
    return progression, str(checker[random])


def generate_question_answer():
    task, correct_answer = generate_progression()
    return task, correct_answer
