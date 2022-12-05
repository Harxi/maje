class Sword:
    def __init__(self, name: str, description: str, collection: str, damage: float, chance: float):
        self.name: str = name
        self.damage: float = damage
        self.chance: float = chance
        self.collection: str = collection
        self.description: str = description
    
    def __str__(self):
        return self.name

class Armor:
    def __init__(self, name: str, description: str, collection: str, armor: int):
        self.name: str = name
        self.armor: int = armor
        self.collection: str = collection
        self.description: str = description
    
    def __str__(self):
        return self.name