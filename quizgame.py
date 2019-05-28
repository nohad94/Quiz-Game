import random


class Question:
    def __init__(self, question_list):
        self.question = random.choice(question_list)
        self.question_prompt = self.question[0]
        self.answer = dic_answers[self.question_prompt]

    def get_prompt(self):
        return self.question_prompt

    def get_answer(self):
        return self.answer


list_of_questions = [

    ["What is the largest mammal in the world?",
        "Blue Whale",
        "Lion",
        "Elephant",
        "Giraffe"],

    ["What is the most popular sport in the world?",
        "Football",
        "Basketball",
        "Tennis",
        "American Football"],

    ["What is the fifth element of the periodic table",
        "Hydrogen",
        "Oxygen",
        "Carbon",
        "Boron"]
]

dic_answers = {

    "What is the largest mammal in the world?": "Blue Whale",
    "What is the most popular sport in the world?": "Football",
    "What is the fifth element of the periodic table": "Boron"
}


