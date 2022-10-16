from dataclasses import dataclass

@dataclass
class Chance:
    chance_id: int = None
    chance_text: str = None
    chance_prize: str = None

    def __str__(self):
        return f"Chance {self.chance_id}: {self.chance_text}, and the prize is {self.chance_prize}."
