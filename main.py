###############################################################################
#Title: Splunking Game
#Version: 005
###############################################################################
import random

highScoreFile = "SpelunkingHighScore.txt"
highScore = 0


class Item:

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def print_description(self):
        return f"You found a {self.description}."        
        

class Tank:

    def __init__(self, capacity):
        self.air = capacity

    def consume_air(self):
        self.air = self.air - 1


class Bag:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def evaluate_loot(self):
        print("You found the following items: ")
        value = 0
        for item in self.inventory:
            print(f" - {item.name} ({item.value})")
            value += item.value
        return value


class Diver:
    
    def __init__(self, name, tankSize, bagCapacity):
        self.name = name
        self.tank = Tank(tankSize)
        self.bag = Bag(bagCapacity)
        self.divers_score = 0

    def search(self):
        print("search...")
        found = random.choice(rarity)
        room = self.bag.capacity - len(self.bag.inventory)
        while True:
            print(found.print_description())
            print(f"You have {room} spots left in your bag. "
                  + "What do you want to do? ")
            print(f" - Keep the name (keep)")
            print(f" - Leave the name (leave)")
            choice = input("Choice: ").lower()
            if choice == "keep":
                self.keep(found)
                break
            elif choice == "leave":
                self.leave(found)
                break
            else:
                print("not an option...try again")
            
    def keep(self, item):
        print(f"keep {item.name}...")
        self.bag.add_to_inventory(item)
        self.tank.consume_air()
 
    def leave(self, item):
        print(f"leave {item.name}...")
        self.tank.consume_air()

    def enjoy(self):
        print("enjoy...")
        self.tank.consume_air()

    def calculate_score(self):
        self.divers_score = self.bag.evaluate_loot()
        print(f"Total value of your loot: {self.divers_score}")
        print(f"Current high score: {highScore}")
        if self.divers_score > int(highScore):
            newHighScore(str(self.divers_score))
            print(f"New high score: {self.divers_score}")
        else:
            print("better luck next time.")


def introduction():
    print("Welcome!...")
    getHighScore()
    print(f"Current high score: {highScore}")


def getHighScore():
    global highScore
    with open(highScoreFile, 'r') as file:
        highScore = file.read()


def newHighScore(newScore):
    with open(highScoreFile, 'w') as file:
        file.write(newScore)


def action():
    print("Choose one of the following options:")
    print(" - Enjoy the Sights (enjoy)")
    print(" - Search for Treasure (search)")
    print(" - Quit the Game (quit)")
    choice = input("Choice: ").lower()
    if choice == "enjoy":
        scuba_steve.enjoy()
    elif choice == "search":
        scuba_steve.search()
    elif choice == "quit":
        ending()
        quit()
    else:
        print("not an option...try again")


def game():
    introduction()
    # Game Ending Conditions.
    while scuba_steve.tank.air>0 \
    and len(scuba_steve.bag.inventory)<scuba_steve.bag.capacity:
        action()    
    print("Returned to the surface.")
    scuba_steve.calculate_score()
    ending()


def ending():
    print("Good-bye...")


# Main -------------------------------------------------------------------------
scuba_steve = Diver("Steve", 5, 3)

rock = Item("rock", "ordinary rock", 0)
silverCoin = Item("silver coin", "tarnished silver coin", 2)
goldCoin = Item("gold coin", "shiny gold coin",3)
ruby = Item("ruby", "beautiful red ruby", 5)

# List to represent items rarity.
rarity = [rock, rock, silverCoin, silverCoin, silverCoin,
          silverCoin, goldCoin, goldCoin, goldCoin, ruby, ruby]

game()