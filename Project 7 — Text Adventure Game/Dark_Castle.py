# ========================================
# GAME STATE
# ========================================

class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []

class Game:
    def __init__(self):
        self.trap = False
        self.chest_opened = False
        self.creature_health = 50
        self.mysterious_key = False

player = Player()
game = Game()

# ========================================
# MAIN MENU
# ========================================

def main_menu():
    print("""
================================
        THE DARK CASTLE
================================

1. Start Game
2. Exit
""")

    while True:
        
        choice = input("Choose an option: ")

        if choice == "1":
            start_game(player, game)
            break

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            continue


# ========================================
# START GAME
# ========================================

def start_game(player, game):
    print("""
================================
          START GAME
================================

You wake up inside a mysterious castle.
""")

    player.health = 100

    print(f"Health: {player.health}")
    print(f"Inventory: {player.inventory}")

    while True:

        choice = input("Enter code here to proceed: ")

        if choice == "2004":
            print("Access Granted!")
            castle_entrance(player, game)
            break

        else:
            print("Incorrect Code. Try again!")
            continue


# ========================================
# CASTLE
# ========================================

def castle_entrance(player, game):
    print("""
================================
        CASTLE ENTRANCE
================================

You find yourself standing inside
an enormous abandoned castle.

There are two doors.

1. Left door
2. Right door
3. Check inventory
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            dungeon_entrance(player, game)
            break

        elif choice == "2":
            library_entrance(player, game)
            break

        elif choice == "3":
            inventory_func(player, game)
            continue

        else:
            print("Invalid choice!")
            continue


# ========================================
# DUNGEON
# ========================================

def dungeon_entrance(player, game):
    print("""
================================
           DUNGEON
================================

You enter a dark dungeon.

1. Explore the dungeon
2. Return to castle entrance
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            dungeon(player, game)
            break

        elif choice == "2":
            castle_entrance_unlocked(player, game)
            break

        else:
            print("Invalid choice!")
            continue


def dungeon(player, game):

    if game.trap == False:
        player.health -= 20

        print(f"""
================================
           DUNGEON
================================

You step on a hidden trap!
You lost 20 health.

Health: {player.health}

You discover an old chest.

1. Open the chest
2. Leave the chest
3. Return
""")

        game.trap = True

    elif game.trap == True:
        print(f"""
================================
           DUNGEON
================================

Health: {player.health}

You discover an old chest.

1. Open the chest
2. Leave the chest
3. Return
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            chest_1(player, game)
            break

        elif choice == "2":
            print("You decide not to touch the chest.")
            continue

        elif choice == "3":
            dungeon_entrance(player, game)
            break

        else:
            print("Invalid choice!")
            continue


# ========================================
# CHEST
# ========================================

def chest_1(player, game):

    if game.chest_opened == False:
        print("""
You open the chest.

Inside, you find an old sword.

You obtained: Sword
""")

        player.inventory.append("Sword")
        game.chest_opened = True

    else:
        print("The chest has already been opened")

    dungeon_depths(player, game)


# ========================================
# DUNGEON DEPTHS
# ========================================

def dungeon_depths(player, game):
    print("""
================================
         DUNGEON DEPTHS
================================

You hear something moving
in the darkness...

1. Investigate
2. Run back
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            dungeon_depths_encounter(player, game)
            break

        elif choice == "2":
            dungeon(player, game)
            break

        else:
            print("Invalid choice!")
            continue


# ========================================
# CREATURE ENCOUNTER
# ========================================

def dungeon_depths_encounter(player, game):
    print(f"""
================================
           ENCOUNTER
================================

A creature emerges from the darkness!

Your Health: {player.health}
Creature Health: {game.creature_health}

1. Attack
2. Run
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            attack(player, game)
            break

        elif choice == "2":
            dungeon(player, game)
            break

        else:
            print("Invalid choice!")
            continue


def attack(player, game):

    if "Sword" not in player.inventory:
        print("You don't have a sword yet!")
        print("You cannot attack the creature!")

        dungeon_depths_encounter(player, game)

        return

    game.creature_health = max(0, game.creature_health - 20)

    print("\nYou attack the creature!")
    print("Creature loses 20 HP.")
    print(f"Creature Health: {game.creature_health}")

    if game.creature_health <= 0:
        print("\nThe creature has been defeated!")
        print("You won the fight!")

        dungeon(player, game)

        return

    player.health = max(0, player.health - 10)

    print("\nThe creature attacks you!")
    print("You lose 10 HP.")
    print(f"Your Health: {player.health}")

    if player.health <= 0:
        print("\nYou have been defeated!")
        print("GAME OVER")

        return

    dungeon_depths_encounter(player, game)


# ========================================
# LIBRARY
# ========================================

def library_entrance(player, game):
    print("""
================================
           LIBRARY
================================

You enter a huge library.

1. Search the library
2. Return to castle entrance
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            strange_bookshelf(player, game)
            break

        elif choice == "2":
            castle_entrance_unlocked(player, game)
            break

        else:
            print("Invalid choice!")
            continue


def strange_bookshelf(player, game):
    print("""
================================
           LIBRARY
================================

You notice a strange bookshelf.

1. Search bookshelf
2. Read an ancient book
3. Return
""")

    while True:
        
        choice = input("Choose an option: ")

        if choice == "1":

            if game.mysterious_key == False:
                print("You found a mysterious key.")

                player.inventory.append("mysterious key")
                game.mysterious_key = True

            else:
                print("The mysterious key has already been added to your inventory.")

            continue

        elif choice == "2":
            print("""
================================
          ANCIENT BOOK
================================

You open an ancient book covered in dust.
Most of its pages are unreadable, but one passage catches your attention.
It speaks of an ancient key hidden somewhere within the library and a sealed door deep inside the castle.
""")
            continue

        elif choice == "3":
            library_entrance(player, game)
            break

        else:
            print("Invalid choice!")
            continue


# ========================================
# LOCKED DOOR
# ========================================

def locked_door(player, game):

    if "mysterious key" not in player.inventory:
        print("""
================================
          LOCKED DOOR
================================

You find an ancient locked door.

The door won't open.

You need a key.

Go and search the key, it's somewhere in the castle.
""")

    elif "mysterious key" in player.inventory:
        print("""
================================
          LOCKED DOOR
================================

You use the mysterious key.

The ancient door slowly opens and you enter.....
""")

        hidden_chamber(player, game)


# ========================================
# HIDDEN CHAMBER
# ========================================

def hidden_chamber(player, game):
    print("""
================================
        HIDDEN CHAMBER
================================

You step through the ancient door.

The room is completely dark.

You see something glowing in the distance.

1. Investigate
2. Return to castle entrance
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            investigate(player, game)
            break

        elif choice == "2":
            castle_entrance_unlocked(player, game)
            break

        else:
            print("Invalid choice!")
            continue


def investigate(player, game):
    print("""
================================
        ANCIENT ARTIFACT
================================

You discover an ancient artifact.

1. Take it
2. Leave it
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            artifact(player, game)
            break

        elif choice == "2":
            print("You leave the artifact untouched.")
            hidden_chamber(player, game)
            break

        else:
            print("Invalid choice!")
            continue


def artifact(player, game):

    if "ancient crown" not in player.inventory:
        player.inventory.append("ancient crown")
        print("You obtained: Ancient Crown")
        castle_entrance_unlocked(player, game)

    elif "ancient crown" in player.inventory:
        print("The artifact is no longer here.")
        castle_entrance_unlocked(player, game)


def castle_entrance_unlocked(player, game):
    print("""
================================
        CASTLE ENTRANCE
================================

You find yourself standing inside
an enormous abandoned castle.

There are two doors.

1. Left door
2. Right door
3. Locked door
4. Check inventory
5. Escape the castle
""")

    while True:

        choice = input("Choose an option: ")

        if choice == "1":
            dungeon_entrance(player, game)
            break

        elif choice == "2":
            library_entrance(player, game)
            break

        elif choice == "3":
            locked_door(player, game)
            continue

        elif choice == "4":
            inventory_func(player, game)
            continue

        elif choice == "5":
            if "ancient crown" in player.inventory:
                print("""
================================
           YOU WIN!
================================

You escaped the Dark Castle.

Congratulations!
""")
                break

            else:
                print("Search the 'ancient crown' first to get through this gate!")

        else:
            print("Invalid choice!")
            continue


# ========================================
# INVENTORY
# ========================================

def inventory_func(player, game):
    print(f"""
================================
          INVENTORY
================================

Your inventory is {player.inventory}.

1. Return
""")

    while True:

        choice = input("Enter 1 here: ")

        if choice == "1":
            castle_entrance_unlocked(player, game)
            break

        else:
            print("Invalid choice!")
            continue


# ========================================
# START PROGRAM
# ========================================

main_menu()