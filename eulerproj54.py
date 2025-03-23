def flush(card_type):
    if len(set(card_type))==1:
        return True
    else:
        return False

def straight(card_val):
    if len(set(card_val)) == 5:
        if card_val[0]-card_val[4]==4:  # sum(card_val) / len(card_val)==card_val[2] and
            return True
    return False

def four_o_kind(card_val):
    if len(set(card_val))==2:
        if card_val[0]==card_val[3] or card_val[1]==card_val[4]:
            return True
    return False

def three_o_kind(card_val):
    for ii in card_val:
        if card_val.count(ii)==3:
            return True
    return False

def pair_count(card_val):  # full house is 1 pair en 1 three
    pairs_of = []
    for i in card_val:
        if card_val.count(i)==2:
            pairs_of.append(i)
    if not pairs_of:
        return []
    else:
        return pairs_of

def score_result(card_val1, card_typ1):
    hand_1_has = []  # contains: score, with a ... and high card value
    flush_flag1 = flush(card_typ1)
    straight_flag1 = straight(card_val1)
    pairs_of = pair_count(card_val1)
    if flush_flag1 and straight_flag1 and card_val1[5]==10:
        hand_1_has.append(10)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(card_val1[0])
    elif flush_flag1 and straight_flag1: # maak in evalutatie verschil tussen beide soorten en hoogte i guess
        hand_1_has.append(9)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(1) #suits
    elif four_o_kind(card_val1):
        hand_1_has.append(8)
        if card_val1[0] == card_val1[3]:
            hand_1_has.append(card_val1[0])
            hand_1_has.append(card_val1[4])
        else:
            hand_1_has.append(card_val1[1])
            hand_1_has.append(card_val1[0])
    elif three_o_kind(card_val1):
        if not pairs_of:  # geen paren, gewoon three o kind
            hand_1_has.append(4)
            hand_1_has.append(card_val1[2])
            card_val1 = list(filter((card_val1[2]).__ne__, card_val1))
            hand_1_has.append(card_val1[0])
        else:
            hand_1_has.append(7)
            hand_1_has.append(card_val1[2])
            card_val1 = list(filter((card_val1[2]).__ne__, card_val1))
            hand_1_has.append(card_val1[0])
    elif flush_flag1:
        hand_1_has.append(6)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(1) #suits
    elif straight_flag1:
        hand_1_has.append(5)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(1) #suits
    elif len(set(pairs_of))==2:
        hand_1_has.append(3)
        hand_1_has.append(pairs_of[1])
        hand_1_has.append(pairs_of[0])
    elif len(set(pairs_of))==1:
        hand_1_has.append(2)
        hand_1_has.append(pairs_of[0])
        hand_1_has.append(card_val1[0])
    else:
        hand_1_has.append(1)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(card_val1[1])
    return hand_1_has

# open, read and close
file = open('poker.txt', 'r')
f = file.readlines()
file.close()

# vars
wins_for_p1 = 0
test_counter = 0
letter_to_number = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

for line in f:
    cards = line.rstrip().split(' ')
    hand1 = cards[:5]
    hand2 = cards[5:]
    card_value1 = []
    card_type1 = []
    card_value2 = []
    card_type2 = []
    for i in hand1:
        card_value1.append(i[0])
        card_type1.append(i[1])
    for i in hand2:
        card_value2.append(i[0])
        card_type2.append(i[1])
    card_value1 = list(map(int, [letter_to_number.get(letter, letter) for letter in card_value1]))
    card_value2 = list(map(int, [letter_to_number.get(letter, letter) for letter in card_value2]))
    card_value1.sort(reverse=True)
    card_value2.sort(reverse=True)
    print(card_value1, card_value2)
    if score_result(card_value1, card_type1) > score_result(card_value2, card_type2):
        wins_for_p1 = wins_for_p1+1
    test_counter+=1
    print(test_counter)

print(wins_for_p1)
