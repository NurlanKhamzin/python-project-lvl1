from random import randrange
import prompt


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


def game5():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Answer \"yes\" if the number is prime, otherwise answer \"no\"")
    for num_input in range(3):
        num = randrange(99)
        print("Question: " + str(num))
        num_input = prompt.string("Your answer: ")
        message = " is wrong answer ;(. Correct answer was "
        if is_prime(num) is True and num_input == "yes":
            print("Correct!")
        elif is_prime(num) is False and num_input == "no":
            print("Correct!")
        else:
            if is_prime(num) is True:
                num_opp = "yes"
            else:
                num_opp = "no"
            print(num_input + message + num_opp + ".")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    game5()
