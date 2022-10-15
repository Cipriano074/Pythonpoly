from game.Player import Player


class AI(Player):
    def __init__(self, player_id):
        super().__init__(player_id, name="AI")