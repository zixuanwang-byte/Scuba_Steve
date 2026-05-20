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