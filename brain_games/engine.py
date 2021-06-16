import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print(game.GAME_RULE)

    for _ in range(3):
        num, is_correct = game.game_logic()
        print("Question: " + str(num))
        num_input = prompt.string("Your answer: ")
        message = " is wrong answer ;(. Correct answer was "
        if num_input == is_correct:
            print("Correct!")
        else:
            print(num_input + message + is_correct + ".")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name + "!")
