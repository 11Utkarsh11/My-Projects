class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def attack(self):
        print(f"{self.name} is attacking")

class Warrior(Character):
    def attack(self):
        print(f"Warrior named {self.name} attacks with sword\n")


class Mage(Character):
    def attack(self):
        print(f"Mage named {self.name} attacks with magic\n")


class Archer(Character):
    def attack(self):
        print(f"Archer named {self.name} attacks with bow\n")


class Game:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def show_characters(self):
        print("\n========== ALL CHARACTERS ==========")
        for character in self.characters:
            print(f"""
====================================
              {character.name}
====================================

Name: {character.name}
Health: {character.health}
Level: {character.level}""")

    def all_attack(self):
        print("\n========== ALL ATTACK ==========\n")
        for character in self.characters:
            character.attack()

# =========================
# TEST CODE
# =========================

# Create characters
warrior1 = Warrior("Thor", 150, 10)
warrior2 = Warrior("Kratos", 200, 15)

mage1 = Mage("Gandalf", 100, 12)
mage2 = Mage("Merlin", 120, 14)

archer1 = Archer("Legolas", 110, 11)


# Create game
game = Game()


# Add characters
game.add_character(warrior1)
game.add_character(warrior2)
game.add_character(mage1)
game.add_character(mage2)
game.add_character(archer1)


# Show all characters
game.show_characters()


# Make everyone attack
game.all_attack()


# Remove one character
game.remove_character(warrior2)


# Show characters again
game.show_characters()


# Make everyone attack again
game.all_attack()