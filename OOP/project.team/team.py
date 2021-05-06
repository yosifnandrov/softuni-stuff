class Team:

    def __init__(self,name,rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self,new_value):
        self.__rating = new_value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self,new_players):
        self.__players = new_players

    def add_player(self,player:"Player"):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self,player_name):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player.__str__()
        return f"Player {player_name} not found"






