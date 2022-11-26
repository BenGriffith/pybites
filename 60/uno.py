from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()
MULTIPLIERS = [2, 4]
ACTIONS = ["Draw Two", "Skip", "Reverse"]

UnoCard = namedtuple('UnoCard', 'suit name')


def _multiplier(cards, card, multiplier):
   for _ in range(multiplier):
      cards.append(card)
   return cards

def _create_suit(suit):
   cards = []
   
   for number in range(0, 10):
      card = UnoCard(suit, number)
      if number == 0:
         cards.append(card)
         continue
      _multiplier(cards, card, MULTIPLIERS[0])
      
   for action in ACTIONS:
      card = UnoCard(suit, action)
      _multiplier(cards, card, MULTIPLIERS[0])
   return cards


def _wild_cards():
   cards = []

   for wild in ["Wild", "Wild Draw Four"]:
      card = UnoCard(None, wild)
      _multiplier(cards, card, MULTIPLIERS[1])
   return cards


def create_uno_deck():
   """Create a deck of 108 Uno cards.
      Return a list of UnoCard namedtuples
      (for cards w/o suit use None in the namedtuple)"""
   red, green, blue, yellow = [_create_suit(suit) for suit in SUITS] 
   return red + green + blue + yellow + _wild_cards()