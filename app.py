import constants
import copy


def clean_data():
    '''store players in a new list, 
    store the height as an integer 
    and change the experience to be a boolean
    '''
    players = copy.deepcopy(constants.PLAYERS)

    for player in players:
        player['height'] = int(player['height'][:2])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['guardians'] = player['guardians'].split(' and ')
    return players


def balance_teams(players):
    balanced_teams = []
    # sort players based on their experience so they get shared amongst the teams equally
    sorted_players = sorted(players, key=lambda x: x['experience'], reverse=True)
    for team in constants.TEAMS:
        balanced_teams.append({
            'team_name': team,
            'players': []
        })
    while len(sorted_players) > 0:
        for team in balanced_teams:
            player = sorted_players.pop()
            team['players'].append(player)
    return balanced_teams

def print_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU----\n")
    print("Here are your choices:\n 1) Display Team Stats\n 2) Quit\n")

def show_menu(teams):
    while True:
        print_menu()
        try: 
            option = int(input('Enter an option: '))
            if option < 1 or option > 2:
                print("please enter a valid number. 1 or 2")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        else: 
            if option == 1:
                display_team_stats(teams)
                continue
            elif option == 2:
                print("Thanks for visiting, hope to see you again soon!")
                break


def display_team_stats(teams):
    print("\nWhich team would you like to learn more about?")
    for i, team in enumerate(teams):
        print(f"{i + 1}) {team['team_name']}")

    while True:
        try: 
            option = int(input('\nEnter an option: '))
            if option < 1 or option > len(teams):
                print(f"please enter a valid number. 1 - {len(teams)}")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        else: 
            display_team(teams[option - 1])
            break


def display_team(team):
    name, players = team.values()
    player_names = []
    print(f"\nTeam: {name} Stats")
    print("--------------------")
    print(f"Total players: {len(players)}")

    experienced = 0
    inexperienced = 0
    for player in players:
        if player['experience']:
            experienced += 1
        else: 
            inexperienced += 1
    print(f"Total experienced: {experienced}")
    print(f"Total inexperienced: {inexperienced}")

    heights = [i['height'] for i in players]
    average_height = round(sum(heights) / len(heights), 2)
    print(f"Average height: {average_height}")

    print("\nPlayers on Team:")
    for player in players:
        player_names.append(player['name'])
    print(', '.join(player_names))

    print("\nGuardians: ")
    guardians = [i['guardians'] for i in players]
    print(', '.join(sum(guardians, [])))

    input('\nPress ENTER to continue...')
    


if __name__ == '__main__':
    player_data = clean_data()
    show_menu(balance_teams(player_data))