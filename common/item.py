class Item:
    owner = None
    def pickUp(self, objects, console):
        objects.remove(self.owner)
        console.printStr('You picked up ' + self.owner.name + '!')
        if self.owner.name == 'Cone of Dunshire':
            return True
        else:
            return False