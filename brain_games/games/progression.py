from random import randint, randrange

GAME_RULE = "What number is missing in the progression?"


def generate_question_answer():
    task = []
    correct = []
    a1 = randint(1, 10)
    d = randint(1, 10)
    for i in range(10):
        formula = a1 + (i - 1) * d
        task.append(formula)
        correct.append(formula)
    random = randrange(len(task))
    task[random] = '..'
    task = ' '.join([str(n) for n in task])
    correct_answer = str(correct[random])
    return task, correct_answer


if __name__ == '__main__':
    generate_question_answer()
