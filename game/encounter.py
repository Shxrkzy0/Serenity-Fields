import random
try:
    from animal import Bestiary, spawnAnimal
    from items import Berries, spawnBerry, berryInventory
except ImportError:
    from .animal import Bestiary, spawnAnimal
    from .items import Berries, spawnBerry, berryInventory


#Base catch chances for each rarity tier
BASE_CATCH_CHANCE = {
    "Common": 0.7, #70%
    "Uncommon": 0.5, #50%
    "Rare": 0.3, #30%
    "Epic": 0.15, #15%
    "Legendary": 0.05 #5%
}


#Catching animals with cap of 95% catch chance
def attemptCatch(animal, berry=None, catchBuff=0):
    baseChance = BASE_CATCH_CHANCE[animal["rarity"]]
    berryBoost = berry["catchChanceBoost"] if berry else 0 #Boost from berry, 0 if no berry is used
    totalChance = baseChance + berryBoost + catchBuff 
    totalChance = min(totalChance, 0.95) #Cap the catch chance at 95%
    roll = random.random()
    return roll < totalChance #True if caught, False if not

def encounter(catchBuff=0):
    animal = spawnAnimal()
    print(f"You encountered a {animal['name']}! It is a {animal['rarity']} animal.")
    print("\nWhat would you like to do?")
    print("1. Attempt to catch")
    print("2. Use a Wild berry")
    print("3. Use a Golden berry")
    print("4. Release")
    choice = input("\n> ").strip()
    if choice == "1":
        if attemptCatch(animal, catchBuff=catchBuff):
            print(f"You caught the {animal['name']}!")
            return animal
        else:
            print(f"The {animal['name']} got away...")
            return None
    elif choice == "2":
        berry = None
        for b in berryInventory:
            if b["name"] == "Wild Berry" and berryInventory[b["name"]] > 0:
                berry = b
                berryInventory[b["name"]] -= 1 #Remove the berry from inventory
                break
        if not berry:
            print("You don't have a Wild berry!")
            return encounter(catchBuff=catchBuff)
        print(f"You used a {berry['name']}! It gives a {int(berry['catchChanceBoost']*100)}% boost to catch chance.")
        if attemptCatch(animal, berry=berry, catchBuff=catchBuff):
            print(f"You caught the {animal['name']}!")
            return animal
        else:
            print(f"The {animal['name']} got away...")
            return None
    elif choice == "3":
        berry = None
        for b in berryInventory:
            if b["name"] == "Golden Berry" and berryInventory[b["name"]] > 0:
                berry = b
                berryInventory[b["name"]] -= 1 #Remove the berry from inventory
                break
        if not berry:
            print("You don't have a Golden berry!")
            return encounter(catchBuff=catchBuff)
        print(f"You used a {berry['name']}! It gives a {int(berry['catchChanceBoost']*100)}% boost to catch chance.")
        if attemptCatch(animal, berry=berry, catchBuff=catchBuff):
            print(f"You caught the {animal['name']}!")
            return animal
    elif choice == "4":
        print(f"You released the {animal['name']}.")
        return None
    else:
        print("Invalid choice.")
        return encounter(catchBuff=catchBuff)