import json


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

# ask user if they want to play again
    #if no:
        # terminate program


def play_again():
    response = safe_input(u"Do you want to play again?")
    return True if response in (u"Yes", u"yes", u"Y", u"y") else False

if __name__ == "__main__":
    while True:
        jsondata = load_json()
        welcome()
        if not play_again():
            break