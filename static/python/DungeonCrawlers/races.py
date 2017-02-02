from attributes import Attributes


    class dwarf(Attributes):
        def __init__(self, str, end, agi, int, wis, luc):
            self.str = 10
            self.end = 10
            self.agi = 5
            self.int = 3
            self.wis = 7
            self.luc = 13


    class elf(Attributes):
        def __init__(self, str, end, agi, int, wis, luc):
            self.str = 4
            self.end = 6
            self.agi = 9
            self.int = 9
            self.wis = 9
            self.luc = 5


    class human(Attributes):
        def __init__(self, str, end, agi, int, wis, luc):
            self.str = 8
            self.end = 8
            self.agi = 8
            self.int = 8
            self.wis = 8
            self.luc = 8


    class orc(Attributes):
        def __init__(self, str, end, agi, int, wis, luc):
            self.str = 14
            self.end = 11
            self.agi = 9
            self.int = 3
            self.wis = 4
            self.luc = 7