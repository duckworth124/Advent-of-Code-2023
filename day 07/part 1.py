with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def get_card_value(card):
    return card_values.index(card)


def get_hand_type(hand):
    hand_summary = {}
    for card in hand:
        if card not in hand_summary:
            hand_summary[card] = 1
            continue
        hand_summary[card] += 1

    num_unique_cards = len(hand_summary.keys())
    max_matching_cards = max(hand_summary.values())
    if num_unique_cards == 1:
        return 6
    if num_unique_cards == 2:
        if max_matching_cards == 4:
            return 5
        return 4
    if max_matching_cards == 3:
        return 3
    if list(hand_summary.values()).count(2) == 2:
        return 2
    if max_matching_cards == 2:
        return 1
    return 0


def get_hand_value(hand):
    return get_hand_type(hand), [get_card_value(card) for card in hand]


puzzle_input_parsed = [i.split(' ') for i in puzzle_input]
puzzle_input_parsed.sort(key=lambda x: get_hand_value(x[0]))

total_winnings = 0
for rank, (hand, bid) in enumerate(puzzle_input_parsed):
    rank += 1
    total_winnings += rank * int(bid)
print(total_winnings)
