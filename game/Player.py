class Player:

    def __init__(self, player_id, name):
        self.player_id = player_id
        self.typeOfPlayer = name
        self.money = 200
        self.cities = []
        print(f'Created a player {self.player_id},  {self.typeOfPlayer}')

    def __str__(self):
        return f"""Player {self.player_id}: {self.typeOfPlayer}, {self.money} $. The cities are {self.cities}.
               \n"""
