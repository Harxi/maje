import random

from engine import events

entityTypes = {
    "Player": "Игрок",
    "Zombie": "Зомби"
}

class Entity:
    def __init__(self, **kwargs):
        self.xp: float = kwargs["xp"]
        self.lvl: int = kwargs["lvl"]
        self.type: str = kwargs["type"]
        self.name: str = kwargs["name"]
        self.coins: int = kwargs["coins"]
        self.reqxp: int = kwargs["reqxp"]
        self.items: list = kwargs["items"]
        self.health: float = kwargs["health"]
        self.damage: float = kwargs["damage"]
        self.armor: "Armor" = kwargs["armor"]
        self.weapon: "Sword" = kwargs["weapon"]
        self.events: "Events" = kwargs["events"]
        self.maxHealth: float = kwargs["maxHealth"]
    
    def deathEvent(self, entity):
        items = [self.weapon, self.armor] + self.items
        entity.items += items
        entity.coins += self.coins
        xp = (entity.reqxp+self.xp)/100*random.randint(1, 5)
        entity.xp += xp
        return {"items": items, "coins": entity.coins, "xp": xp}
        # print(f"{entity.name} убил(а) {entityTypes[entites[0].type]} и получил(а) {round(xp)} XP, {entity.coins} C и следующие предметы: {', '.join(map(lambda item: str(item), items))}")
        
    def getDamage(self, damage: float, fromEntity: "Entity"):
        self.health -= damage
    
    def hit(self, entity: "Entity"):
        damage = random.choices([self.damage+self.weapon.damage, (self.damage+self.weapon.damage)*2], weights=[1-entity.weapon.chance, entity.weapon.chance])[0]-entity.armor.armor
        if damage <= 0:
            return -1
        else:
            entity.getDamage(damage, self)
            return damage
      
