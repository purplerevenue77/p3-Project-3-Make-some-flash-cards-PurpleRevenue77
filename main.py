import json
import random

def flashcards_quiz():
    president_questions = []
    correct = 0
    with open("flashcards (copy).json", "r") as f:
        flashcards = json.load(f)
    president_questions = list(flashcards.keys())
    for key in random.choices(president_questions, k=20):
      value = flashcards[key]
      for i in president_questions:
        user_response = input(f"Who was the {i}th president of the United States? ")
        if user_response == value:
          correct += 1
        elif user_response != value:
          correct += 0
      score = f"{correct}/20"
      print(score)

flashcards_quiz()