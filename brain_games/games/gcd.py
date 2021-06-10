import prompt
from random import randrange
import math


def game3():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Find the greatest common divisor of given numbers.")
    for num_input in range(3):
        num1 = randrange(99)
        num2 = randrange(99)
        print("Question: " + str(num1) + " " + str(num2))
        num_input = prompt.string("Your answer: ")
        if str(math.gcd(num1, num2)) == num_input:
            print('Correct!')
        else:
            message = " is wrong answer ;(. Correct answer was "
            print(str(num_input) + message + str(math.gcd(num1, num2)) + ".")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    game3()
