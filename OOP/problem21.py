class Attack:
    def attack(self):
        print("Attacking")

class Defense:
    def defend(self):
        print("Defending")

class Magic:
    def cast_spell(self):
        print("Casting spell")

class Character(Attack, Defense, Magic):
    pass

c = Character()
c.attack()
c.defend()
c.cast_spell()
