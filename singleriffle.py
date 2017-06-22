"""
    wrute a function to tell if a full deck of cards is a single riffle of two other halves ( half1 and half2)
    rules:
        1- cut the deck into halves half1 and half2
        2- grab a random number of cards from the top of half1 (cards > 0 and cards < half1)
        3- grab a random number of cards from the top of half 2 (cards > 0 and cards < half2 )
        4- repeat step 3 and 4 untiol half1 and half2 are empty
"""

def singleriffle(half1, half2, shuffled_deck):
    #keep track of the index of half1 and half2
    half1_index = 0
    half2_index = 0
    half1_max_index = len(half1) - 1
    half2_max_index = len(half2) - 1

    #iterate through the shuffled_deck
    for card in shuffled_deck:
        #if there are cards in half1 and the top of half1 and the shuffled_deck are the same increment the half1_index
        if half1_index <= half1_max_index and card == half1[half1_index]:
            half1_index += 1
        #if there are cards in half1 and the top of half2 and the shuffled_deck are the same increment the half2_index
        elif half2_index <= half2_max_index and card == half2[half2_index]:
            half2_index += 1
        # if the top of the shuffled_deck does not match the top of half1 or half2 there is no single riffle
        else:
            return False

    # there is a single riffle because all the cards have been found
    return True
