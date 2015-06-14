# whole game should loop

# load data
    # question responses stored here. 0 means no, 1 means yes, -1 means unknown (question is new)

# display welcome message

# prompt the user to think of an animal

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