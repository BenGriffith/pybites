import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = {}

    with open(BATTLE_DATA) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for line in csv_reader:
            if line_count == 0:
                attacker = line[1:]
            else:
                defeat_mapping[line[0]] = dict(zip(attacker, line[1:]))
            line_count += 1
    
    return defeat_mapping    


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    
    if player1 not in defeat_mapping or player2 not in defeat_mapping:
        raise ValueError

    for attacker, outcomes in defeat_mapping.items():
        if attacker == player1:
            for opponent, outcome in outcomes.items():
                if opponent == player2:
                    if outcome == "draw":
                        return "Tie"
                    elif outcome == "win":
                        return attacker
                    else:
                        return opponent


if __name__ == "__main__":
    print(get_winner("Rock", "Fire"))