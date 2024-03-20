import json
import random

def flashcards_quiz():
    president_questions = []
    with open("flashcards (copy).json", "r") as f:
        flashcards = json.load(f)
    president_questions = list(flashcards.keys())
    for _ in range(1):  
        random.shuffle(president_questions)
        for i in president_questions:
            user_response = input(f"Who was the {i}th president of the United States? ")
            if user_response == flashcards[i]:
              print('correct')


flashcards_quiz()