from collections import namedtuple, defaultdict
import random
import string

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

action_count = defaultdict(int)

def _get_action(n):

    action_max = int(n * 0.25)

    action = random.choice(ACTIONS)

    if action_count[action] >= action_max:
        while action_count[action] < action_max:
            action = random.choice(ACTIONS)
            if action_count[action] < action_max:
                action_count[action] += 1
                break
                
    else:
        action_count[action] += 1
    
    return action


def _get_cards(letter_list, n):

    random_card = random.choice(letter_list)
    random_action = _get_action(n)

    for i in range(len(letter_list)):
        if letter_list[i] == random_card:
            letter_list[i] = PawCard(card=letter_list[i], action=random_action)
        else:
            letter_list[i] = PawCard(card=letter_list[i], action=None)

    return letter_list


def create_paw_deck(n=8):
    
    if n > 26:
        raise ValueError

    letters = list(string.ascii_uppercase)[:n]

    for i in range(len(letters)):
        letters[i] = _get_cards([f"{letters[i]}{j}" for j in NUMBERS], n)

    return [card for letter in letters for card in letter]


if __name__ == "__main__":
    print(create_paw_deck())
    #print(_get_cards())