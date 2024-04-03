class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Player:
    def __init__(self, name, age, birth_date):
        self.name = name
        self.age = age
        self.birth_date = birth_date

def CreatePlayer():
    # Get player information from the user
    name = input("Enter player's name: ")
    age = int(input("Enter player's age: "))

    # Get birth date information
    day = int(input("Enter birth day: "))
    month = int(input("Enter birth month: "))
    year = int(input("Enter birth year: "))
    birth_date = Date(day, month, year)

    # Create and return a Player object
    player = Player(name, age, birth_date)
    return player

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

def CreateEmptyTeam():
    # Get team name from the user
    team_name = input("Enter team name: ")

    # Create and return a Team object
    team = Team(team_name)
    return team

def AddPlayer(team, player):
    # Add the player to the team's player array
    team.players.append(player)

def StoreTeam(team, file_pointer):
    # Write team information to the file
    file_pointer.write(f"Team Name: {team.team_name}\n")
    file_pointer.write("Players:\n")
    for player in team.players:
        file_pointer.write(f"{player.name},{player.age},{player.birth_date.day}/{player.birth_date.month}/{player.birth_date.year};\n")

def ReadTeam(file_pointer):
    # Read team information from the file
    team_name_line = file_pointer.readline().strip().split(": ")
    team_name = team_name_line[1]

    team = Team(team_name)

    players_line = file_pointer.readline().strip().split(": ")[1]
    players_info = players_line.split(";")

    for player_info in players_info:
        if player_info:
            player_details = player_info.split(",")
            name = player_details[0]
            age = int(player_details[1])
            date_details = player_details[2].split("/")
            day = int(date_details[0])
            month = int(date_details[1])
            year = int(date_details[2])
            birth_date = Date(day, month, year)

            player = Player(name, age, birth_date)
            AddPlayer(team, player)

    return team

# Example usage
if __name__ == "__main__":
    team = CreateEmptyTeam()

    # Add players to the team
    for _ in range(3):
        player = CreatePlayer()
        AddPlayer(team, player)

    # Store team information to a file
    with open("team_info.txt", "w") as file:
        StoreTeam(team, file)

    # Read team information from the file
    with open("team_info.txt", "r") as file:
        new_team = ReadTeam(file)

    # Display team information
    print("\nTeam Information:")
    print(f"Team Name: {new_team.team_name}")
    print("Players:")
    for player in new_team.players:
        print(f"Name: {player.name}, Age: {player.age}, Birth Date: {player.birth_date.day}/{player.birth_date.month}/{player.birth_date.year}")
