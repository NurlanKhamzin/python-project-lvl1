import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.GAME_RULE)

    for _ in range(3):
        task, correct_answer = game.generate_question_answer()
        print("Question: " + str(task))
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
