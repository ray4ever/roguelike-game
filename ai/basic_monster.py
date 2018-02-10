class BasicMonster:
    owner = None  # this is AI component, must be owned by Object
    #AI for a basic monster.
    def take_turn(self, dungeon, console):
        #a basic monster takes its turn. If you can see it, it can see you
        monster = self.owner

        player = dungeon.player

        if (monster.x, monster.y) in player.fov_coords:
            #move towards player if far away
            if monster.distance_to(player) >= 2:
                monster.move_towards(player.x, player.y, dungeon)

            #close enough, attack! (if the player is still alive.)
            elif hasattr(player.fighter, 'hp') and player.fighter.hp > 0:
                monster.fighter.attack(player, console)