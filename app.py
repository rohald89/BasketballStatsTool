import constants


def clean_data():
    '''store players in a new list, 
    store the height as an integer 
    and change the experience to be a boolean
    '''
    players = constants.PLAYERS
    for player in players:
        player['height'] = int(player['height'][0:2])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return players


if __name__ == '__main__':
    clean_data()