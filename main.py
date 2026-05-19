###############################################################################
#Title: Spelunking Game
#Version: 003.2 - modules removed
###############################################################################
import random

highScoreFile = "SpelunkingHighScore.txt"
highScore = 0

tank = {"air": 5}

scuba_bag = {"inventory": [], "capacity": 3}

diver = {"name": "Steve", "tank": tank,"bag": scuba_bag,
         "score": 0, "diving": True}

items = {"rock": {"name": "rock", "description": "ordinary rock",
                  "value": 0},
         "silverCoin": {"name": "silver coin", "description":
                        "tarnished silver coin","value": 2},
         "goldCoin": {"name": "gold coin", "description": "shiny gold coin",
                      "value": 3},
         "ruby": {"name": "ruby", "description": "beautiful red ruby",
                  "value": 5}}

# List to represent items rarity.
rarity = ["rock", "rock", "silverCoin", "silverCoin", "silverCoin",
          "silverCoin","goldCoin", "goldCoin", "goldCoin", "ruby", "ruby" ]


def consume_air():
    global diver
    diver["tank"]["air"] -= 1


def add_to_inventory(item):
    global diver
    diver["bag"]["inventory"].append(item)


def keep(item):
    print("keep...")
    add_to_inventory(item)
    consume_air()


def leave(item):
    print(f"leave {items[item]['name']}...")
    consume_air()


def search():
    print("search...")
    found = random.choice(rarity)
    room = diver["bag"]["capacity"] - len(diver["bag"]["inventory"])
    while True:
        print(f"You found a {items[found]['description']}.")
        print(f"You have {room} spots left in your bag. "
              + "What do you want to do? ")
        print(f" - Keep the {items[found]['name']} (keep)")
        print(f" - Leave the {items[found]['name']} (leave)")
        choice = input("Choice: ").lower()
        if choice == "keep":
            keep(found)
            break
        elif choice == "leave":
            leave(found)
            break
        else:
            print("not an option...try again")
 

def enjoy():
    global air_tank, diver
    print("enjoy...")
    consume_air()


def return_to_surface():
    print("Return to surface...")
    diver["diving"] = False


def action():
        print("Choose one of the following options:")
        print(" - Enjoy the Sights (enjoy)")
        print(" - Search for Treasure (search)")
        print(" - Quit the Game (quit)")
        choice = input("Choice: ").lower()
        if choice == "enjoy":
            enjoy()
        elif choice == "search":
            search()
        elif choice == "quit":
            return_to_surface()
        else:
            print("not an option...try again")
            
            
def evaluate_loot():
    score = 0
    print("You found the following items: ")
    for item in diver["bag"]["inventory"]:
        print(f" - {items[item]['name']} ({items[item]['value']})")
        score += items[item]["value"]
    return score


def calculate_score():
    global diver
    diver["score"] = evaluate_loot()
    print(f"Total value of your loot: {diver['score']}")
    print(f"Current high score: {highScore}")
    if diver["score"] > int(highScore):
        newHighScore(str(diver["score"]))
        print(f"New high score: {diver['score']}")
    else:
        print("better luck next time.")


def getHighScore():
    global highScore
    with open(highScoreFile, 'r') as file:
        highScore = file.read()


def newHighScore(newScore):
    with open(highScoreFile, 'w') as file:
        file.write(newScore)


def introduction():
    print("Welcome!...")
    getHighScore()
    print(f"Current high score: {highScore}")


def game():
    introduction()
    while diver["tank"]["air"] > 0 and \
          len(diver["bag"]["inventory"]) != diver["bag"]["capacity"]:
        action()
    calculate_score()
    ending()


def ending():
    print("Good-bye...")


# Main -------------------------------------------------------------------------
game()