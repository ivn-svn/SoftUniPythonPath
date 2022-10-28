# 6.	Steam User
# Create a class called SteamUser. Upon initialization, it should receive a username (string) and games (list). It should also have an attribute called played_hours (0 by default). Add three methods to the class:
# -	play(game, hours)
# o	If the game is in the game list, increase the played_hours by the given hours and return "{username} is playing {game}"
# o	Otherwise, return "{game} is not in library"
# -	buy_game(game)
# o	If the game is not in the game list, add it and return "{username} bought {game}"
# o	Otherwise, return "{game} is already in your library"
# -	status() - returns the following:
#     "{username} has {games_count} games. Total play time: {played_hours}"
# Submit only the class in the judge system.
# Examples
class SteamUser:
    def __init__(self, username:str, games:list, played_hours = 3):
        self.username = str(username)
        self.games = list(games)
        self.played_hours = int(played_hours)
    def play(self, game, hours):
        self.game = game
        self.hours = hours
        if self.game in self.games:
            self.played_hours += self.hours
            return f"{self.username} is playing {self.game}"
        else:            
            return f"{self.game} is not in library"
    def buy_game(self, game):
        if self.game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {self.game}"
        elif self.game in self.games:
            return f"{self.game} is already in your library"
    def status(self):        
            games_count = len(self.games)
            return f"{self.username} has {games_count} games. Total play time: {self.played_hours}"

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
