# ========================================
# DARK CASTLE
# ========================================


# ========================================
# PLAYER
# ========================================

class Player:

    def __init__(self):
        self.health = 100
        self.inventory = []

    def has_item(self, item):
        return item in self.inventory

    def add_item(self, item):
        if not self.has_item(item):
            self.inventory.append(item)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def is_alive(self):
        return self.health > 0

    def show_status(self):
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")


# ========================================
# CREATURE
# ========================================

class Creature:

    def __init__(self):
        self.health = 50
        self.defeated = False

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

        if self.health == 0:
            self.defeated = True

    def is_alive(self):
        return not self.defeated


# ========================================
# GAME
# ========================================

class Game:

    def __init__(self):

        self.player = Player()
        self.creature = Creature()

        # World state
        self.trap_triggered = False
        self.chest_opened = False
        self.key_found = False

        # Game state
        self.game_over = False
        self.game_won = False

    # ====================================
    # GENERAL HELPERS
    # ====================================

    def get_choice(self, prompt, valid_choices):

        while True:

            choice = input(prompt)

            if choice in valid_choices:
                return choice

            print("Invalid choice!")

    # ====================================
    # RUN GAME
    # ====================================

    def run(self):

        self.main_menu()

        if self.game_won:
            return

        print("\nThanks for playing The Dark Castle!")

    # ====================================
    # MAIN MENU
    # ====================================

    def main_menu(self):

        print("""
================================
        THE DARK CASTLE
================================

1. Start Game
2. Exit
""")

        choice = self.get_choice(
            "Choose an option: ",
            ["1", "2"]
        )

        if choice == "1":
            self.start_game()

        elif choice == "2":
            print("\nGoodbye!")
            self.game_over = True

    # ====================================
    # START GAME
    # ====================================

    def start_game(self):

        print("""
================================
          START GAME
================================

You wake up inside a mysterious castle.
""")

        self.player.health = 100
        self.player.inventory.clear()

        print(f"Health: {self.player.health}")
        print(f"Inventory: {self.player.inventory}")

        while True:

            choice = input(
                "\nEnter code here to proceed: "
            )

            if choice == "2004":

                print("\nAccess Granted!")

                self.castle_entrance()

                return

            print("Incorrect Code. Try again!")

    # ====================================
    # CASTLE ENTRANCE
    # ====================================

    def castle_entrance(self):

        while not self.game_over and not self.game_won:

            print("""
================================
        CASTLE ENTRANCE
================================

You find yourself standing inside
an enormous abandoned castle.
""")

            print("1. Left door")
            print("2. Right door")
            print("3. Check inventory")

            # Locked door becomes available
            # after finding the key.
            if self.player.has_item("mysterious key"):
                print("4. Locked door")

            # Escape becomes available
            # after obtaining the crown.
            if self.player.has_item("ancient crown"):
                print("5. Escape the castle")

            print()

            valid_choices = ["1", "2", "3"]

            if self.player.has_item("mysterious key"):
                valid_choices.append("4")

            if self.player.has_item("ancient crown"):
                valid_choices.append("5")

            choice = self.get_choice(
                "Choose an option: ",
                valid_choices
            )

            if choice == "1":
                self.dungeon_entrance()

            elif choice == "2":
                self.library_entrance()

            elif choice == "3":
                self.inventory()

            elif choice == "4":
                self.locked_door()

            elif choice == "5":
                self.escape_castle()

    # ====================================
    # DUNGEON ENTRANCE
    # ====================================

    def dungeon_entrance(self):

        while not self.game_over and not self.game_won:

            print("""
================================
           DUNGEON
================================

You enter a dark dungeon.

1. Explore the dungeon
2. Return to castle entrance
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2"]
            )

            if choice == "1":
                self.dungeon()

            elif choice == "2":
                return

    # ====================================
    # DUNGEON
    # ====================================

    def dungeon(self):

        if not self.trap_triggered:

            self.player.take_damage(20)
            self.trap_triggered = True

            print("""
================================
           DUNGEON
================================

You step on a hidden trap!

You lost 20 health.
""")

            print(f"Health: {self.player.health}")

            if not self.player.is_alive():
                self.defeat()
                return

        while not self.game_over and not self.game_won:

            print("""
You discover an old chest.

1. Open the chest
2. Leave the chest
3. Return
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2", "3"]
            )

            if choice == "1":

                self.open_chest()
                return

            elif choice == "2":

                print("\nYou decide not to touch the chest.")

            elif choice == "3":

                return

    # ====================================
    # CHEST
    # ====================================

    def open_chest(self):

        if self.chest_opened:

            print("\nThe chest has already been opened.")

        else:

            print("""
You open the chest.

Inside, you find an old sword.

You obtained: Sword
""")

            self.player.add_item("Sword")
            self.chest_opened = True

        self.dungeon_depths()

    # ====================================
    # DUNGEON DEPTHS
    # ====================================

    def dungeon_depths(self):

        while not self.game_over and not self.game_won:

            print("""
================================
         DUNGEON DEPTHS
================================

You hear something moving
in the darkness...

1. Investigate
2. Run back
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2"]
            )

            if choice == "1":

                self.creature_encounter()
                return

            elif choice == "2":

                return

    # ====================================
    # CREATURE ENCOUNTER
    # ====================================

    def creature_encounter(self):

        if not self.creature.is_alive():

            print("\nThe creature has already been defeated.")
            return

        while (
            self.creature.is_alive()
            and self.player.is_alive()
            and not self.game_over
        ):

            print(f"""
================================
          ENCOUNTER
================================

A creature emerges from the darkness!

Your Health: {self.player.health}
Creature Health: {self.creature.health}

1. Attack
2. Run
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2"]
            )

            if choice == "1":

                self.attack()

            elif choice == "2":

                print("\nYou run back from the creature.")
                return

    # ====================================
    # ATTACK
    # ====================================

    def attack(self):

        if not self.player.has_item("Sword"):

            print("""
You don't have a sword yet!
You cannot attack the creature!
""")

            return

        # Player attacks
        self.creature.take_damage(20)

        print("\nYou attack the creature!")
        print("Creature loses 20 HP.")
        print(
            f"Creature Health: "
            f"{self.creature.health}"
        )

        # Creature defeated
        if not self.creature.is_alive():

            print("""
The creature has been defeated!
You won the fight!
""")

            return

        # Creature attacks back
        self.player.take_damage(10)

        print("\nThe creature attacks you!")
        print("You lose 10 health.")
        print(f"Your Health: {self.player.health}")

        if not self.player.is_alive():

            self.defeat()

    # ====================================
    # LIBRARY
    # ====================================

    def library_entrance(self):

        while not self.game_over and not self.game_won:

            print("""
================================
           LIBRARY
================================

You enter a huge library.

1. Search the library
2. Return to castle entrance
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2"]
            )

            if choice == "1":

                self.strange_bookshelf()

            elif choice == "2":

                return

    # ====================================
    # STRANGE BOOKSHELF
    # ====================================

    def strange_bookshelf(self):

        while not self.game_over and not self.game_won:

            print("""
================================
        STRANGE BOOKSHELF
================================

You notice a strange bookshelf.

1. Search bookshelf
2. Read an ancient book
3. Return
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2", "3"]
            )

            if choice == "1":

                self.search_bookshelf()

            elif choice == "2":

                self.read_ancient_book()

            elif choice == "3":

                return

    # ====================================
    # SEARCH BOOKSHELF
    # ====================================

    def search_bookshelf(self):

        if self.key_found:

            print("""
The mysterious key has already
been added to your inventory.
""")

            return

        print("""
You search through the bookshelf...

You found a mysterious key!
""")

        self.player.add_item("mysterious key")
        self.key_found = True

    # ====================================
    # ANCIENT BOOK
    # ====================================

    def read_ancient_book(self):

        print("""
================================
          ANCIENT BOOK
================================

You open an ancient book covered in dust.

Most of its pages are unreadable,
but one passage catches your attention.

It speaks of an ancient key hidden
somewhere within the library and a
sealed door deep inside the castle.
""")

    # ====================================
    # LOCKED DOOR
    # ====================================

    def locked_door(self):

        if not self.player.has_item("mysterious key"):

            print("""
================================
          LOCKED DOOR
================================

You find an ancient locked door.

The door won't open.

You need a key.

Go and search for the key.
It's somewhere in the castle.
""")

            return

        print("""
================================
          LOCKED DOOR
================================

You use the mysterious key.

The ancient door slowly opens...
""")

        self.hidden_chamber()

    # ====================================
    # HIDDEN CHAMBER
    # ====================================

    def hidden_chamber(self):

        while not self.game_over and not self.game_won:

            print("""
================================
        HIDDEN CHAMBER
================================

You step through the ancient door.

The room is completely dark.

You see something glowing in
the distance.

1. Investigate
2. Return to castle entrance
""")

            choice = self.get_choice(
                "Choose an option: ",
                ["1", "2"]
            )

            if choice == "1":

                self.investigate_artifact()

            elif choice == "2":

                return

    # ====================================
    # INVESTIGATE ARTIFACT
    # ====================================

    def investigate_artifact(self):

        print("""
================================
        ANCIENT ARTIFACT
================================

You discover an ancient artifact.

1. Take it
2. Leave it
""")

        choice = self.get_choice(
            "Choose an option: ",
            ["1", "2"]
        )

        if choice == "1":

            self.take_artifact()

        elif choice == "2":

            print("\nYou leave the artifact untouched.")

    # ====================================
    # TAKE ARTIFACT
    # ====================================

    def take_artifact(self):

        if self.player.has_item("ancient crown"):

            print("\nThe artifact is no longer here.")
            return

        self.player.add_item("ancient crown")

        print("""
You obtained: Ancient Crown

The crown feels strangely warm
in your hands...
""")

    # ====================================
    # ESCAPE
    # ====================================

    def escape_castle(self):

        if not self.player.has_item("ancient crown"):

            print("""
You search for an exit...

But the castle refuses to let you leave.

You need the Ancient Crown first.
""")

            return

        print("""
================================
            ESCAPE
================================

You approach the castle gates.

The Ancient Crown begins to glow.

The ancient gates slowly open.

You step outside.

The castle disappears behind you...
""")

        print("""
================================
           YOU WIN!
================================

You escaped the Dark Castle.

Congratulations!
""")

        self.game_won = True

    # ====================================
    # INVENTORY
    # ====================================

    def inventory(self):

        print("""
================================
          INVENTORY
================================
""")

        if self.player.inventory:

            for item in self.player.inventory:
                print(f"- {item}")

        else:

            print("Your inventory is empty.")

        print("""
1. Return
""")

        self.get_choice(
            "Choose an option: ",
            ["1"]
        )

    # ====================================
    # DEFEAT
    # ====================================

    def defeat(self):

        print("""
================================
          GAME OVER
================================

You have been defeated.

The Dark Castle claims another victim...
""")

        self.game_over = True


# ========================================
# START PROGRAM
# ========================================

game = Game()
game.run()