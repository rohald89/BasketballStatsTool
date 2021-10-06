import constants


def clean_data():
    '''store players in a new list, 
    store the height as an integer 
    and change the experience to be a boolean
    '''
    players = constants.PLAYERS

    for player in players:
        player['height'] = int(player['height'][:2])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

    return players

def balance_teams(players):
    balanced_teams = {}
    for team in constants.TEAMS:
        balanced_teams[team] = []
    while len(players) > 0:
        for team in balanced_teams:
            player = players.pop()
            balanced_teams[team].append(player)
    print(balanced_teams)


if __name__ == '__main__':
    player_data = clean_data()
    balance_teams(player_data)