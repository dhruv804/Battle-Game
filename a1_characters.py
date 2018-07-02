"""
The classes for the two types of the characters in the game.
Namely, Rogue and Mage

"""
from typing import List


class Characters:
    """A superclass for the two types of characters."""

    def __init__(self) -> None:
        """Initializes the Character"""
        self.hp = 100
        self.sp = 100
        self.defense = 0
        self.enemy = None

    def get_hp(self) -> int:
        """Returns the HealthPoints of the chrarcter.
        >>> c = Characters()
        >>> c.get_hp()
        100
        """
        raise NotImplementedError

    def get_sp(self) -> int:
        """Returns the SkillPoints of the character.
        >>> c = Characters()
        >>> c.get_sp()
        100"""
        raise NotImplementedError


class Rogue(Characters):
    """The class containing the Rogue character.

    Attributes:
        - Name (name): The name of the Character
        - BattleQueue (bq): The BattleQueue used for the game
        - Playstyle (play): The playstyle used by the Character
        - HealthPoints (hp): Contains the health of the character
        - SkillPoints (sp): Contains the skill points of the character
        - Defense (defense): Contains the defense stats of a character.
        - Enenmy (enemy): The enemy of the player in the game
        - Animation State (animation_state): Keeps the track of the character's
         current animation state.
        - Current State (curr_state): Keeps track of the sprites.
        """

    def __init__(self, name: str, bq: 'BattleQueue', play: 'Playstyle') -> None:
        """Initializes the Rogue character with the given (name) and given
        Playstyle(play)"""

        self.name = name
        self.bq = bq
        self.playstyle = play
        self.enemy = None
        self.hp = 100
        self.sp = 100
        self.defense = 10
        self.animation_state = "idle"
        self.curr_state = -1

    def get_hp(self) -> int:
        """Returns the HealthPoints of the chrarcter.
        >>> c = Rogue()
        >>> c.get_hp()
        100
        """
        return self.hp

    def get_sp(self) -> int:
        """Returns the HealthPoints of the chrarcter.
        >>> c = Rogue()
        >>> c.get_sp()
        100
        """
        return self.sp

    def get_name(self) -> str:
        """Returns the name of the character.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Rogue("Dhruv", bq, ps)
        >>> r.get_name()
        'Dhruv'
        """
        return self.name

    def attack(self) -> None:
        """Allows the rogue to attack once using certain SP.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Rogue("Dhruv", bq, ps)
        >>> p = Rogue("Satish", bq, ps)
        >>> r.enemy = p
        >>> p.enemy = r
        >>> r.attack()
        >>> p.get_hp()
        95
        """
        self.animation_state = "attack"
        self.curr_state = -1
        self.bq.add(self)
        self.sp -= 3
        self.enemy.hp -= (15 - self.enemy.defense)
        if self.enemy.hp <= 0:
            self.enemy.hp = 0

    def special_attack(self) -> None:
        """Allows the rogue to perform a special attack once using
        certain SP.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Rogue("Dhruv", bq, ps)
        >>> p = Rogue("Satish", bq, ps)
        >>> r.enemy = p
        >>> p.enemy = r
        >>> r.special_attack()
        >>> p.get_hp()
        90
        """
        self.animation_state = "sp_attack"
        self.curr_state = -1
        self.bq.add(self)
        self.bq.add(self)
        self.sp -= 10
        self.enemy.hp -= (20 - self.enemy.defense)
        if self.enemy.hp <= 0:
            self.enemy.hp = 0

    def is_valid_action(self, action: str) -> bool:
        """Returns wheter the given (action) is valid or no depending upon
        the available SkillPoints.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Rogue("Dhruv", bq, ps)
        >>> r.is_valid_action("A")
        True
        """

        if action == 'A':
            return self.sp >= 3
        if action == 'S':
            return self.sp >= 10

    def get_available_actions(self) -> List[str]:
        """Returns a list of all the possible actions depending upon the
         available SkillPoints.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Rogue("Dhruv", bq, ps)
        >>> r.get_available_actions()
        ['A', 'S']
        """

        available_actions = []
        if self.sp >= 10:
            available_actions.append("A")
            available_actions.append("S")
        elif 3 <= self.sp < 10:
            available_actions.append("A")
        return available_actions

    def __repr__(self) -> str:
        """Returns a representation of the character
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Rogue("Dhruv", bq, ps)
        >>> r
        Dhruv (Rogue): 100/100
        """

        string = '{} (Rogue): {}/{}'.format(self.name, self.hp, self.sp)
        return string

    def idle_helper(self) -> str:
        """Helper Method for Idel state"""

        idle = ["rogue_idle_0", "rogue_idle_1", "rogue_idle_2", "rogue_idle_3",
                "rogue_idle_4", "rogue_idle_5", "rogue_idle_6", "rogue_idle_7",
                "rogue_idle_8", "rogue_idle_9"]

        if self.curr_state == -1:
            self.curr_state += 1
            return idle[0]
        if self.curr_state == 0:
            self.curr_state += 1
            return idle[1]
        if self.curr_state == 1:
            self.curr_state += 1
            return idle[2]
        if self.curr_state == 2:
            self.curr_state += 1
            return idle[3]
        if self.curr_state == 3:
            self.curr_state += 1
            return idle[4]
        if self.curr_state == 4:
            self.curr_state += 1
            return idle[5]
        if self.curr_state == 5:
            self.curr_state += 1
            return idle[6]
        if self.curr_state == 6:
            self.curr_state += 1
            return idle[7]
        if self.curr_state == 7:
            self.curr_state += 1
            return idle[8]
        if self.curr_state == 8:
            self.curr_state += 1
            return idle[9]
        if self.curr_state == 9:
            self.curr_state = -1
            return idle[0]

    def attack_helper(self) -> str:
        """Helper method for attack state"""

        attack = ["rogue_attack_0", "rogue_attack_1", "rogue_attack_2",
                  "rogue_attack_3", "rogue_attack_4", "rogue_attack_5",
                  "rogue_attack_6", "rogue_attack_7", "rogue_attack_8",
                  "rogue_attack_9"]
        idle = ["rogue_idle_0", "rogue_idle_1", "rogue_idle_2", "rogue_idle_3",
                "rogue_idle_4", "rogue_idle_5", "rogue_idle_6", "rogue_idle_7",
                "rogue_idle_8", "rogue_idle_9"]

        if self.curr_state == -1:
            self.curr_state += 1
            return attack[0]
        if self.curr_state == 0:
            self.curr_state += 1
            return attack[1]
        if self.curr_state == 1:
            self.curr_state += 1
            return attack[2]
        if self.curr_state == 2:
            self.curr_state += 1
            return attack[3]
        if self.curr_state == 3:
            self.curr_state += 1
            return attack[4]
        if self.curr_state == 4:
            self.curr_state += 1
            return attack[5]
        if self.curr_state == 5:
            self.curr_state += 1
            return attack[6]
        if self.curr_state == 6:
            self.curr_state += 1
            return attack[7]
        if self.curr_state == 7:
            self.curr_state += 1
            return attack[8]
        if self.curr_state == 8:
            self.curr_state += 1
            return attack[9]
        if self.curr_state == 9:
            self.curr_state = -1
            self.animation_state = "idle"
            return idle[0]

    def sp_attack_helper(self) -> str:
        """Helper method for Sp_attack state"""
        sp_attack = ["rogue_special_0", "rogue_special_1", "rogue_special_2",
                     "rogue_special_3", "rogue_special_4", "rogue_special_5",
                     "rogue_special_6", "rogue_special_7", "rogue_special_8",
                     "rogue_special_9"]
        idle = ["rogue_idle_0", "rogue_idle_1", "rogue_idle_2", "rogue_idle_3",
                "rogue_idle_4", "rogue_idle_5", "rogue_idle_6", "rogue_idle_7",
                "rogue_idle_8", "rogue_idle_9"]

        if self.curr_state == -1:
            self.curr_state += 1
            return sp_attack[0]
        if self.curr_state == 0:
            self.curr_state += 1
            return sp_attack[1]
        if self.curr_state == 1:
            self.curr_state += 1
            return sp_attack[2]
        if self.curr_state == 2:
            self.curr_state += 1
            return sp_attack[3]
        if self.curr_state == 3:
            self.curr_state += 1
            return sp_attack[4]
        if self.curr_state == 4:
            self.curr_state += 1
            return sp_attack[5]
        if self.curr_state == 5:
            self.curr_state += 1
            return sp_attack[6]
        if self.curr_state == 6:
            self.curr_state += 1
            return sp_attack[7]
        if self.curr_state == 7:
            self.curr_state += 1
            return sp_attack[8]
        if self.curr_state == 8:
            self.curr_state += 1
            return sp_attack[9]
        if self.curr_state == 9:
            self.curr_state = -1
            self.animation_state = "idle"
            return idle[0]

    def get_next_sprite(self) -> str:
        """Returns the correct sprites for the surrent animation state of the
        character."""

        if self.animation_state == "idle":
            return self.idle_helper()

        elif self.animation_state == "attack":
            return self.attack_helper()

        elif self.animation_state == "sp_attack":
            return self.sp_attack_helper()


class Mage(Characters):
    """The class containing the Rogue character.

    Attributes:
        - Name (name): The name of the Character
        - BattleQueue (bq): The BattleQueue used for the game
        - Playstyle (play): The playstyle used by the Character
        - HealthPoints (hp): Contains the health of the character
        - SkillPoints (sp): Contains the skill points of the character
        - Defense (defense): Contains the defense stats of a character.
        - Enenmy (enemy): The enemy of the player in the game
        - Animation State (animation_state): Keeps the track of the character's
         current animation state.
        - Current State (curr_state): Keeps track of the sprites.
        """

    def __init__(self, name: str, bq: 'BattleQueue', play: 'Playstyle') -> None:
        """Initializes the Rogue character with the given (name) and given
        Playstyle(play)"""

        self.name = name
        self.bq = bq
        self.playstyle = play
        self.enemy = None
        self.hp = 100
        self.sp = 100
        self.defense = 8
        self.animation_state = "idle"
        self.curr_state = -1

    def get_hp(self) -> int:
        """Returns the HealthPoints of the chrarcter.
        >>> c = Mage()
        >>> c.get_hp()
        100
        """
        return self.hp

    def get_sp(self) -> int:
        """Returns the HealthPoints of the chrarcter.
        >>> c = Mage()
        >>> c.get_sp()
        100
        """
        return self.sp

    def get_name(self) -> str:
        """Returns the name of the character.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Mage("Dhruv", bq, ps)
        >>> r.get_name()
        'Dhruv'"""
        return self.name

    def attack(self) -> None:
        """Allows the rogue to attack once using certain SP.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Mage("Dhruv", bq, ps)
        >>> p = Mage("Satish", bq, ps)
        >>> r.enemy = p
        >>> p.enemy = r
        >>> r.attack()
        >>> p.get_hp()
        88
        """
        self.animation_state = "attack"
        self.curr_state = -1
        self.bq.add(self)
        self.sp -= 5
        self.enemy.hp -= (20 - self.enemy.defense)
        if self.enemy.hp <= 0:
            self.enemy.hp = 0

    def special_attack(self) -> None:
        """Allows the rogue to perform a special attack once using
        certain SP.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Mage("Dhruv", bq, ps)
        >>> p = Mage("Satish", bq, ps)
        >>> r.enemy = p
        >>> p.enemy = r
        >>> r.special_attack()
        >>> p.get_hp()
        68
        """
        self.animation_state = "sp_attack"
        self.curr_state = -1
        self.bq.add(self.enemy)
        self.bq.add(self)
        self.sp -= 30
        self.enemy.hp -= (40 - self.enemy.defense)
        if self.enemy.hp <= 0:
            self.enemy.hp = 0

    def is_valid_action(self, action: str) -> bool:
        """Returns wheter the given (action) is valid or no depending upon
        the available SkillPoints.a
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Mage("Dhruv", bq, ps)
        >>> r.is_valid_action("A")
        True
        """

        if action == 'A':
            return self.sp >= 5
        if action == 'S':
            return self.sp >= 30

    def get_available_actions(self) -> List[str]:
        """Returns a list of all the possible actions depending upon the
         available SkillPoints.
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Mage("Dhruv", bq, ps)
        >>> r.get_available_actions()
        ['A', 'S']
        """

        available_actions = []
        if self.sp >= 30:
            available_actions.append("A")
            available_actions.append("S")
        elif 5 <= self.sp < 30:
            available_actions.append("A")
        return available_actions

    def __repr__(self) -> str:
        """Returns a representation of the character
        >>> bq = BattleQueue()
        >>> ps = Playstyle(bq)
        >>> r = Mage("Dhruv", bq, ps)
        >>> r
        Dhruv (Mage): 100/100
        """

        string = "{} (Mage): {}/{}".format(self.name, self.hp, self.sp)
        return string

    def idle_helper(self) -> str:
        """Helper Method for Idel state"""

        idle = ["mage_idle_0", "mage_idle_1", "mage_idle_2", "mage_idle_3",
                "mage_idle_4", "mage_idle_5", "mage_idle_6", "mage_idle_7",
                "mage_idle_8", "mage_idle_9"]

        if self.curr_state == -1:
            self.curr_state += 1
            return idle[0]
        if self.curr_state == 0:
            self.curr_state += 1
            return idle[1]
        if self.curr_state == 1:
            self.curr_state += 1
            return idle[2]
        if self.curr_state == 2:
            self.curr_state += 1
            return idle[3]
        if self.curr_state == 3:
            self.curr_state += 1
            return idle[4]
        if self.curr_state == 4:
            self.curr_state += 1
            return idle[5]
        if self.curr_state == 5:
            self.curr_state += 1
            return idle[6]
        if self.curr_state == 6:
            self.curr_state += 1
            return idle[7]
        if self.curr_state == 7:
            self.curr_state += 1
            return idle[8]
        if self.curr_state == 8:
            self.curr_state += 1
            return idle[9]
        if self.curr_state == 9:
            self.curr_state = -1
            return idle[0]

    def attack_helper(self) -> str:
        """Helper method for attack state"""

        attack = ["mage_attack_0", "mage_attack_1", "mage_attack_2",
                  "mage_attack_3", "mage_attack_4", "mage_attack_5",
                  "mage_attack_6", "mage_attack_7", "mage_attack_8",
                  "mage_attack_9"]
        idle = ["mage_idle_0", "mage_idle_1", "mage_idle_2", "mage_idle_3",
                "mage_idle_4", "mage_idle_5", "mage_idle_6", "mage_idle_7",
                "mage_idle_8", "mage_idle_9"]

        if self.curr_state == -1:
            self.curr_state += 1
            return attack[0]
        if self.curr_state == 0:
            self.curr_state += 1
            return attack[1]
        if self.curr_state == 1:
            self.curr_state += 1
            return attack[2]
        if self.curr_state == 2:
            self.curr_state += 1
            return attack[3]
        if self.curr_state == 3:
            self.curr_state += 1
            return attack[4]
        if self.curr_state == 4:
            self.curr_state += 1
            return attack[5]
        if self.curr_state == 5:
            self.curr_state += 1
            return attack[6]
        if self.curr_state == 6:
            self.curr_state += 1
            return attack[7]
        if self.curr_state == 7:
            self.curr_state += 1
            return attack[8]
        if self.curr_state == 8:
            self.curr_state += 1
            return attack[9]
        if self.curr_state == 9:
            self.curr_state = -1
            self.animation_state = "idle"
            return idle[0]

    def sp_attack_helper(self) -> str:
        """Helper method for Sp_attack state"""
        sp_attack = ["mage_special_0", "mage_special_1", "mage_special_2",
                     "mage_special_3", "mage_special_4", "mage_special_5",
                     "mage_special_6", "mage_special_7", "mage_special_8",
                     "mage_special_9"]
        idle = ["mage_idle_0", "mage_idle_1", "mage_idle_2", "mage_idle_3",
                "mage_idle_4", "mage_idle_5", "mage_idle_6", "mage_idle_7",
                "mage_idle_8", "mage_idle_9"]

        if self.curr_state == -1:
            self.curr_state += 1
            return sp_attack[0]
        if self.curr_state == 0:
            self.curr_state += 1
            return sp_attack[1]
        if self.curr_state == 1:
            self.curr_state += 1
            return sp_attack[2]
        if self.curr_state == 2:
            self.curr_state += 1
            return sp_attack[3]
        if self.curr_state == 3:
            self.curr_state += 1
            return sp_attack[4]
        if self.curr_state == 4:
            self.curr_state += 1
            return sp_attack[5]
        if self.curr_state == 5:
            self.curr_state += 1
            return sp_attack[6]
        if self.curr_state == 6:
            self.curr_state += 1
            return sp_attack[7]
        if self.curr_state == 7:
            self.curr_state += 1
            return sp_attack[8]
        if self.curr_state == 8:
            self.curr_state += 1
            return sp_attack[9]
        if self.curr_state == 9:
            self.curr_state = -1
            self.animation_state = "idle"
            return idle[0]

    def get_next_sprite(self) -> str:
        """Returns the correct sprites for the surrent animation state of the
        character."""

        if self.animation_state == "idle":
            return self.idle_helper()

        elif self.animation_state == "attack":
            return self.attack_helper()

        elif self.animation_state == "sp_attack":
            return self.sp_attack_helper()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
