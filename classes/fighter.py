class Fighter:
    owner = None  # this is class component, and must be owned by Object
    #combat-related properties and methods (monster, player, NPC).
    def __init__(self, hp, defense, power, death_function=None):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.death_function = death_function

    def take_damage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.hp -= damage

        #check for death. if there's a death function, call it
        if self.hp <= 0:
            function = self.death_function
            if function is not None:
                function(self.owner)

    def attack(self, target, console):
        #a simple formula for attack damage
        damage = self.power - target.fighter.defense
        resultStr = ''

        if damage > 0:
            #make the target take some damage
            resultStr = (self.owner.name.capitalize() +
                         ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.\n\n')
            target.fighter.take_damage(damage)
        else:
            resultStr = (self.owner.name.capitalize() +
                         ' attacks ' + target.name + ' but it has no effect!\n\n')

        console.printStr(resultStr)