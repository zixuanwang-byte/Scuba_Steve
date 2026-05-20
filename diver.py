import random
import tank
import bag
import items
import highscore


class Diver:
    
    def __init__(self, name, tankSize, bagCapacity):
        self.name = name
        self.tank = tank.Tank(tankSize)
        self.bag = bag.Bag(bagCapacity)
        self.divers_score = 0

    def search(self):
        print("search...")
        found = random.choice(items.rarity)
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
        print(f"Current high score: {highscore.highScore}")
        if self.divers_score > int(highscore.highScore):
            highscore.newHighScore(str(self.divers_score))
            print(f"New high score: {self.divers_score}")
        else:
            print("better luck next time.")