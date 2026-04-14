#Wild Berry - +15% chance to catch animal 
#Golden Berry - +35% chance to catch animal
#These will be flat percentages since these do not need to be balanced against other buffs and are only used for catching animals.

Berries = [
    {"name": "Wild Berry", "catchChanceBoost": 0.15, "colour": (255, 0, 215), "weight": 85}, #Pink colour
    {"name": "Golden Berry", "catchChanceBoost": 0.35, "colour": (255, 215, 0), "weight": 15} #Gold colour
]

def spawnBerry():
    import random
    total = sum(berry["weight"] for berry in Berries) #Total weight of all berries
    num = random.randint(1, total) #Random number between 1 and total weight
    current = 0
    for berry in Berries:
        current += berry["weight"]
        if num <= current:
            return berry

#Function to add berries to player inventory, with a random chance to get either a Wild Berry or a Golden Berry
def addBerryToInventory():
    berry = spawnBerry()
    berryInventory[berry["name"]] += 1
    print(f"You found a {berry['name']}! It has been added to your inventory.")

#Inventory to keep track of how many berries the player has
berryInventory = {
    "Wild Berry": 0,
    "Golden Berry": 0
}