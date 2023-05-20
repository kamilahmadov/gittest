# Building a Multiple Choise Quiz

from Question import Question

question_promts = [
    "What colors are apples?\n(a) Red/Green(b) Purple\n(c) Orange \n\n",
    "What colors are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
    "What colors are strawberies\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)