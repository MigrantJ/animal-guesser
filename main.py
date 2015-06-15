#!/usr/bin/env python

import json
import random
import copy


def load_json():
    """load data. question responses stored here.
    0 means no, 1 means yes, -1 means unknown (question is new)
    """
    f = open("data.json", "r")
    return json.loads(f.read())


def safe_input(prompt):
    """Allow canceling input without errors"""
    try:
        user_input = raw_input(prompt)
    except EOFError:
        user_input = None
    except KeyboardInterrupt:
        user_input = None

    return user_input


def welcome():
    """display welcome message"""
    print(u"Welcome to the Animal Guesser!")
    safe_input(u"Please think of an animal, then press a key to begin!")

# main game loop here
    # print a question
        # if there are no more questions
            # make guess at animal
        # else
            # select a question (preferably one that will eliminate a lot of animals
    # prompt user for response
        # if question was an animal guess:
            # terminate loop
        # else:
            # keep track of user's response in case this is a new animal
    # winnow down available questions based on response

# end game
    # if animal guess was correct:
        # print yay message, end game
    # if not:
        # ask user what the animal was
        # if that animal is in data:
            # try to determine what went wrong? or ask user questions that have uncertain responses?
        # if not:
            # prompt user for a question that would separate it from *guessed animal*
            # store new animal along with user responses
            # store new question, put in yes for new animal, no for guessed animal, -1 for all others


def prompt_yes_or_no(prompt):
    response = safe_input(prompt)
    return True if response in (u"Yes", u"yes", u"Y", u"y") else False


def play_again():
    return prompt_yes_or_no(u"Do you want to play again?")


def get_question(questions, animals):
    # select a question (preferably one that will narrow animal list)
    i = random.choice(questions.keys())
    # don't ask question again
    q = questions.pop(i)
    return i, q


def guess_animal(animals):
    return random.choice(animals.keys())


def narrow_animals(animals, qindex, response):
    return {a: rs for a, rs in animals.iteritems()
            if animals[a][qindex] == response}


if __name__ == "__main__":
    jsondata = load_json()
    while True:
        # create safe-to-modify lists
        qs = jsondata["questions"]
        questions = {i: q for i, q in zip(range(len(qs)), qs)}
        animals = copy.deepcopy(jsondata["animals"])
        response_yes = None
        guess = None
        welcome()

        while True:
            # if there are no more questions or animals
            if len(animals) == 1 or not len(questions):
                guess = guess_animal(animals)
                question = u"Is your animal a " + guess + u"?"
            else:
                qindex, question = get_question(questions, animals)
            # prompt user for response
            response_yes = prompt_yes_or_no(question)
            if guess:
                break
            else:
                animals = narrow_animals(animals, qindex, response_yes)

        if not response_yes:
            newanimal = safe_input(u"Dang! What was your animal?")
            if jsondata["animals"][newanimal]:
                print(u"That's weird, I know that animal.")
            else:
                newquestion = safe_input(u"Okay, what's a question that would distinguish that animal from " + guess)
        else:
            print(u"YES! I RULE!")

        if not play_again():
            break