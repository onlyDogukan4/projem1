class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
class Player:
    def __init__(self,name,age,birthdate):
        self.name=name
        self.age=age
        self.birthdate=birthdate
    @staticmethod
    def CreatePlayer():
        name=input("enter a name: ")
        age=int(input("enter a age: "))
        birthdate=Date(int(input("Enter the day of birth: ")), int(input("Enter the month of birth: ")), int(input("Enter the year of birth: ")))
        return Player(name,age,birthdate)
class Team():
    def __init__(self,team_name,players):
        self.team_name=team_name
        self.players=players
        self.counter=0
        self.number_of_player=int(input("How many players do you want in your team: "))

    @classmethod
    def Create_empty_team(cls):
        team_name=input("enter a team name: ")
        return cls(team_name,[])

    def AddPlayer(self,player):
        self.players.append(player)
        self.counter+=1

    def StoreTeam(self, file):
        file.write(f"{self.team_name}; this team has {team.number_of_player} players  \n")
        for player in self.players:
            file.write(player.name+';'+str(player.age)+';'+str(player.birthdate.day)+';'+str(player.birthdate.month)+';'+str(player.birthdate.year)+  "  ,  ")

team=Team.Create_empty_team()
for i in range(team.number_of_player):
    player=Player.CreatePlayer()
    team.AddPlayer(player)
    # print(f"Team: "+{team.team_name} + +"\n",player.name+';'+str(player.age)+';'+str(player.birthdate.day)+';'+str(player.birthdate.month)+';'+str(player.birthdate.year))
    print(f"Team: {team.team_name}; {team.number_of_player} players exist \n{player.name} ;{int(player.age)};{int(player.birthdate.day)};{int(player.birthdate.month)};{int(player.birthdate.year)}")
with open("team_data.txt","w") as file:
    team.StoreTeam(file)
