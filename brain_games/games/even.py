from random import randrange
import prompt


def game1():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    for num_input in range(3):
        num = randrange(99)
        print("Question: " + str(num))
        num_input = prompt.string("Your answer: ")
        if (num % 2) == 0:
            num_opp = "yes"
        if (num % 2) == 1:
            num_opp = "no"
        if ((num % 2) == 0 and num_input == "yes"):
            print('Correct!')
        elif ((num % 2) == 1 and num_input == "no"):
            print('Correct!')
        else:
            message = " is wrong answer ;(. Correct answer was "
            print(num_input + message + num_opp + ".")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    game1()
