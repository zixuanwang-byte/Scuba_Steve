class Item:

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def print_description(self):
        return f"You found a {self.description}."   


rock = Item("rock", "ordinary rock", 0)
silverCoin = Item("silver coin", "tarnished silver coin", 2)
goldCoin = Item("gold coin", "shiny gold coin",3)
ruby = Item("ruby", "beautiful red ruby", 5)

# List to represent items rarity.
rarity = [rock, rock, silverCoin, silverCoin, silverCoin,
          silverCoin, goldCoin, goldCoin, goldCoin, ruby, ruby]