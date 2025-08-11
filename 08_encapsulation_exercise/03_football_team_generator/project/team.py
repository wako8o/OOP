class Team:

    def __init__(self, name:str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):

        info = [player for player in self.__players if player.name == player_name]
        if info:
            self.__players.remove(info[0])
            return info[0]
        return f"Player {player_name} not found"
