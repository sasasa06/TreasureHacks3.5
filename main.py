import random
from termcolor import colored

recyclable_items = ["glass bottle", "plastic bottle", "aluminum can", "paper", "cardboard", "metal", "plastic bag"]
non_recyclable_items = ["styrofoam", "food waste", "used tissue", "broken glass", "plastic wrap"]

score = 0
question_limit = 5
used_questions = []

print(colored("Welcome to Saachi's Recycling Fun & Interactive Game! Identify which items are recyclable and which are not.", "green"))
print(colored("Type 'quit' to exit the game.\n", "green"))

while score < question_limit:
    remaining_choices = list(set(recyclable_items + non_recyclable_items) - set(used_questions))
    item = random.choice(remaining_choices)
    print(f"What should you do with a {colored(item, 'yellow')}?")

    answer = input("Enter 'recycle', 'trash', or 'donate': ")

    if answer == "recycle" and item in recyclable_items:
        print(colored("Correct!", "green"))
        score = score + 1
    elif answer == "trash" and item in non_recyclable_items:
        print(colored("Correct!", "green"))
        score = score + 1
    elif answer == "donate":
        print(colored("Donating is a great way to help the environment too!", "green"))
    elif answer == "quit":
        break
    else:
        print(colored("Sorry, that's incorrect.", "red"))

    used_questions.append(item)
    print(f"Your score is {colored(score, 'magenta')}\n")

print(colored("Now, let's create a recycling-themed story!", "green"))
print(colored("Enter a word related to recycling or the environment:", "green"))

recycling_word = input()

story_prompts = [f"Once upon a time, there was a {recycling_word} who lived in a __ADJECTIVE__ __PLACE__.",
                 f"In a far-off land, there was a {recycling_word} who dreamed of __VERB__ing the __NOUN__.",
                 f"Long ago, there was a {recycling_word} who discovered a __ADJECTIVE__ __NOUN__ in the __PLACE__."]

adjectives = ["red", "happy", "funny", "silly", "brave", "wise"]
nouns = ["cat", "dog", "princess", "wizard", "king", "queen"]
verbs = ["fly", "sing", "dance", "swim", "run", "jump"]
places = ["castle", "forest", "beach", "mountain", "river", "ocean"]

story_prompt = random.choice(story_prompts)
words = []

for word_type in ["ADJECTIVE", "NOUN", "VERB", "PLACE"]:
    word = input(f"Enter an {colored(word_type.lower(), 'yellow')}: ")
    words.append(word)

story = story_prompt.replace("__ADJECTIVE__", words[0])
story = story.replace("__NOUN__", words[1])
story = story.replace("__VERB__", words[2])
story = story.replace("__PLACE__", words[3])

print(colored(story, "cyan"))
