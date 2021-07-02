from random import randint, randrange

GAME_RULE = "What number is missing in the progression?"


def game_logic():
    num = []
    correct = []
    a1 = randint(1, 10)
    d = randint(1, 10)
    for i in range(10):
        formula = a1 + (i - 1) * d
        num.append(formula)
        correct.append(formula)
    random = randrange(len(num))
    num[random] = '..'
    num = ' '.join([str(n) for n in num])
    correct_answer = str(correct[random])
    return num, correct_answer


if __name__ == '__main__':
    game_logic()
