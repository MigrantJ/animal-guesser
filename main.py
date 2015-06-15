#!/usr/bin/env python

import json
import random
import copy


def load_json():
    """load data. question responses stored here.
    false means no, true means yes, null/None means unknown (question is new)
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


def prompt_yes_or_no(prompt):
    response = safe_input(prompt)
    return response in (u"Yes", u"yes", u"Y", u"y")


def play_again():
    return prompt_yes_or_no(u"Do you want to play again?")


def get_question(questions, animals):
    """Select a question based on what will narrow the animal list the most."""
    # TODO: don't make selection random
    i = random.choice(questions.keys())
    # don't ask question again
    q = questions.pop(i)
    return i, q


def guess_animal(animals):
    return random.choice(animals.keys())


def narrow_animals(animals, qindex, response):
    """Take entries out of the animals list based on the response to a
    question.
    """
    return {a: rs for a, rs in animals.iteritems()
            if animals[a][qindex] == response
            or animals[a][qindex] is None}


if __name__ == "__main__":
    jsondata = load_json()
    while True:
        # create safe-to-modify lists
        qs = jsondata["questions"]
        questions = {i: q for i, q in zip(range(len(qs)), qs)}
        animals = copy.deepcopy(jsondata["animals"])
        responses = [-1 for i in range(len(questions))]
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
                responses[qindex] = response_yes
                animals = narrow_animals(animals, qindex, response_yes)

        if not response_yes:
            newanimal = safe_input(u"Dang! What was your animal?")
            if newanimal in jsondata["animals"]:
                print(u"That's weird, I know that animal.")
            else:
                newi = len(questions)
                newquestion = safe_input(u"Okay, what's a question that is true for " + newanimal + u" but false for " + guess)
                # store new animal along with user responses
                jsondata["animals"][newanimal] = responses
                # store new question, put in yes for new animal, no for guessed animal, -1 for all others
                jsondata["questions"].append(newquestion)
                for animal, answers in jsondata["animals"].iteritems():
                    answers.append(-1)
                jsondata["animals"][newanimal][-1] = 1
                jsondata["animals"][guess][-1] = 0
        else:
            # TODO: add responses to data of animal if answer is unknown (-1)
            print(u"YES! I RULE!")

        if not play_again():
            break