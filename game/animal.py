#Spawn weights: Base / Total = Probability of spawning
#Common: 50, Uncommon: 25, Rare: 12, Epic: 5, Legendary: 1
#Total weight = 50 + 50 + 50 + 25 + 25 + 12 + 12 + 5 + 5 + 1 = 235
#Rarity for each animal:
    #Common: 21.74%
    #Uncommon: 10.87%
    #Rare: 5.22%
    #Epic: 2.17%
    #Legendary: 0.43%


Bestiary = [
{
    "name": "Rabbit", "rarity": "Common", "weight": 50, "colour": (255, 255, 255),"buffs": {"speed": 0.1}
},
{
    "name": "Sparrow", "rarity": "Common", "weight": 50, "colour": (255, 255, 255), "buffs": { "moneyBoost": 0.1}
},
{
    "name": "Hedgehog", "rarity": "Common", "weight": 50, "colour": (255, 255, 255), "buffs": {"staminaRegen": 0.1}
},
{
    "name": "Fox", "rarity": "Uncommon", "weight": 25, "colour": (0, 255, 0), "buffs": { "speed": 0.15, "moneyBoost": 0.1}
},
{
    "name": "Deer", "rarity": "Uncommon", "weight": 25, "colour": (0, 255, 0), "buffs": { "maxStamina": 0.2}
},
{
    "name": "Owl", "rarity": "Rare", "weight": 12, "colour": (0, 0, 255), "buffs": {"luck": 0.2, "catchChance": 0.1}
},
{
    "name": "Badger", "rarity": "Rare", "weight": 12, "colour": (0, 0, 255), "buffs": {"catchChance": 0.25, "staminaRegen": 0.15}
},
{
    "name": "Swan", "rarity": "Epic", "weight": 5, "colour": (255, 0, 255),"buffs": {"moneyBoost": 0.25, "luck": 0.2}
},
{
    "name": "Wolf", "rarity": "Epic", "weight": 5, "colour": (255, 0, 255), "buffs": {"speed": 0.25, "staminaRegen": 0.2}
},
{
    "name": "Peacock", "rarity": "Legendary", "weight": 1, "colour": (255, 215, 0), "buffs": {"speed": 0.15, "moneyBoost": 0.2, "staminaRegen": 0.15, "maxStamina": 0.15, "luck": 0.15, "catchChance": 0.15}
}
]


#Weighted random selection function to spawn random animal
def spawnAnimal():
    import random
    total = sum(animal["weight"] for animal in Bestiary) #Total weight of all animals
    num = random.randint(1, total) #Random number between 1 and total weight
    current = 0
    for animal in Bestiary:
        current += animal["weight"]
        if num <= current:
            return animal
        
#Animal collection function to add caught animals to player collection, with a max of 12 animals in the collection at once, and a max of 2 equipped animals at once
def addAnimalToCollection(animal, collection):
    if len(collection) >= 12:
        print("Your collection is full! Please release an animal before adding a new one.")
        return collection
    collection.append(animal)
    return collection

#Collection
animalCollection = []