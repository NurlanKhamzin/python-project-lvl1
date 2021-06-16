from random import randint, randrange

game_rule = "What number is missing in the progression?"


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
    is_correct = str(correct[random])
    return num, is_correct


if __name__ == '__main__':
    game_logic()
