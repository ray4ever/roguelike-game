from dungeon import DungeonGenerator
from .level import Level

class LevelManager:
    def __init__(self):
        self.levels = []
        self.level_count = 0
        self.dungeon = DungeonGenerator()
        self.game_state = 'active'
        self.player_action = None

    def createLevel(self):
        self.level_count += 1
        new_level = Level('Level ' + str(self.level_count))
        self.levels.append(new_level)
        return new_level

    def getCurrentLevel(self):
        for level in self.levels:
            if level.level_state == 'active':
                return level