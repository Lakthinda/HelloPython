def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand1_total = 0
    hand2_total = 0
    # hand_1check wich A value to use
    A_with_11 = check_A_value(hand_1,11)
    A_with_1 = check_A_value(hand_1,1)
    if(A_with_11 < 21):
        hand1_total = A_with_11
    else:
        hand1_total = A_with_1
        
    # hand_2check wich A value to use
    A_with_11 = check_A_value(hand_2,11)
    A_with_1 = check_A_value(hand_2,1)
    
    if(A_with_11 < 21):
        hand2_total = A_with_11
    else:
        hand2_total = A_with_1

    # determining if hand1 win
    if(hand1_total > 21):
        return False
    elif ((hand1_total < 21 and hand1_total > hand2_total) or hand2_total > 21):
        return True
    else:
        return False
        
def check_A_value(hand,A_value):
    hand_total = 0
    for value in hand:
        if(value == 'K' or value == 'J' or value == 'Q'):
            hand_total = hand_total + 10
        elif(value == 'A'):
            hand_total = hand_total + int(A_value)
        else:
            hand_total = hand_total + int(value)
    
    return hand_total


hand_1=['2', '10', '5', 'A', '9', '9']
hand_2=['5', '7', '5', 'Q', '5']


print(blackjack_hand_greater_than(hand_1,hand_2))