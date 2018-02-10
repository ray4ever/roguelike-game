import math

class Object:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, x, y, char, name, blocks=False, fighter=None, ai=None, item=None):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.blocks = blocks
        self.fighter = fighter
        self.ai = ai
        self.item = item

        if self.fighter:  # let the fighter component know who owns it
            self.fighter.owner = self

        if self.ai:  # let the AI component know who owns it
            self.ai.owner = self

        if self.item:  # let the Item component know who owns it
            self.item.owner = self

    def move(self, dx, dy, dungeon):
        #move by the given amount, if the destination is not blocked
        if not is_blocked(self.x + dx, self.y + dy, dungeon):
            self.x += dx
            self.y += dy

    def get(self, player):
        if (self.x, self.y) in player.fov_coords:
            return self

    def clear(self):
        del self

    def move_towards(self, target_x, target_y, dungeon):
        #vector from this object to the target, and distance
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        #normalize it to length 1 (preserving direction), then round it and
        #convert to integer so the movement is restricted to the map grid
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy, dungeon)

    def distance_to(self, other):
        #return the distance to another object
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


def send_to_back(obj, objects):
    # make this object be drawn first, so all others appear above it if
    # they're in the same tile.

    objects.remove(obj)
    objects.insert(0, obj)


def is_blocked(x, y, dungeon):
    #first test the map tile
    x = int(x)
    y = int(y)
    if dungeon.map[x][y].blocked:
        return True

    #now check for any blocking objects
    for object in dungeon.objects:
        if object.blocks and object.x == x and object.y == y:
            return True

    return False