import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.GAME_RULE)

    for _ in range(3):
        num, correct_answer = game.game_logic()
        print("Question: " + str(num))
        num_input = prompt.string("Your answer: ")
        message = " is wrong answer ;(. Correct answer was "
        if num_input == correct_answer:
            print("Correct!")
        else:
            print(f"{num_input}{message}{correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
