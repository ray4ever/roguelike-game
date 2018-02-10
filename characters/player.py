from common import Object

class Player(Object):

    def __init__(self, *args, **kwargs):
        Object.__init__(self, *args, **kwargs)
        self.fov_coords = set()

    def move_or_attack(self, dx, dy, dungeon, action_log):

        # the coordinates the player is moving to/attacking
        x = self.x + dx
        y = self.y + dy

        # try to find an attackable object there
        target = None

        for object in dungeon.objects:
            if object.fighter and object.x == x and object.y == y:
                target = object
                break

        # attack if target found, move otherwise
        if target is not None:
            self.fighter.attack(target, action_log)
        else:
            self.move(dx, dy, dungeon)

    def heal_damage(self):
        self.fighter.hp += 10