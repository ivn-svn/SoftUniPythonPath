#
# Create a class called Hero. Upon initialization, it should receive a name (string) 
# and health (number). Create two additional methods:
# •	defend(damage) - reduce the given damage from the hero's health:
# o	if the health become 0 or less, set it to 0 and return "{name} was defeated"
# •	heal(amount) - increase the health of the hero with the given amount
#
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = int(health)
    def defend(self, damage):
        self.damage = int(damage)
        self.health -= self.damage
        if self.health < 0:
            self.health = 0
            return(f"{self.name} was defeated")
        elif self.health == 0:
            return(f"{self.name} was defeated")
    def heal(self, amount):
        self.amount = int(amount)
        self.health += self.amount
        return self.health