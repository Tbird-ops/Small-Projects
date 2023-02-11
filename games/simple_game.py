class Hero():
    weapon = None
    health = None
    potion = True 

    def __init__(self, weapon, health):
        self.weapon = weapon
        self.health = health

    def fight(self, weapon):
        print("You slash at the monster!")
        print("Your ", weapon," lands a serious blow")
        Monster.lose()

    def drink(self, potion):
        if potion == True:
            self.health += 5
    
    def hurt(self, damage):
        self.health -= damage
    
    def die(self, health):
        if health <= 0
            print("The hero has fallen. Game Over")
            break




class Monster():
    health = None
    damage = None
    
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


