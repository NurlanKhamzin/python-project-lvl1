import prompt
from random import randint, randrange


def game4():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("What number is missing in the progression?")
    for num_input in range(3):
        array = []
        list = []
        a1 = randint(1, 10)
        d = randint(1, 10)
        for i in range(10):
            formula = a1 + (i - 1) * d
            array.append(formula)
            list.append(formula)
        random = randrange(len(array))
        array[random] = '..'
        print("Question: " + str(array))
        num_input = prompt.string("Your answer: ")
        if str(list[random]) == num_input:
            print('Correct!')
        else:
            message = " is wrong answer ;(. Correct answer was "
            print(str(num_input) + message + str(list[random]) + ".")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    game4()
