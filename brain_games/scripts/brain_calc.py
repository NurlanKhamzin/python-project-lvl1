import prompt
import operator
import random
from random import randrange


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("What is the result of the expression?")
    for num_input in range(3):
        num1 = randrange(99)
        num2 = randrange(99)
        ops = {'+': operator.add,
               '-': operator.sub,
               '*': operator.mul}
        op = random.choice(list(ops.keys()))
        answer = ops.get(op)(num1, num2)
        print("Question: " + str(num1) + " " + str(op) + " " + str(num2))
        num_input = prompt.string("Your answer: ")
        if str(answer) == (num_input):
            print('Correct!')
        else:
            print(str(num_input) + " is wrong answer ;(. Correct answer was " + str(answer) + ".")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
