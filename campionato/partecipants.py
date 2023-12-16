# Copyright (c) 2023 Jules aka Netherfield
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# reference to own class in hints
from typing import NoReturn
from collections.abc import Sequence
from utils import parse_file


from datetime import datetime

class Player():
    def __init__(self, name:str, surname:str, birth_year:int, attendance:int=0):
        self.name = name
        self.surname = surname
        try:
            self.birth_year = int(birth_year)
            self.attendance = int(attendance)
        except ValueError:
            pass
    
    def __repr__(self):
        return '(' + self.name + ', ' + self.surname + ', ' + str(self.birth_year) + ', ' + str(self.attendance) + ')'
    
    def increase_attendance(self, att:int=1):
        self.attendance += att

    def info(self):
        return str(self)
    
    def age(self) -> int:
        try:
            delta = datetime.today().year - self.birth_year
        except:
            pass
        if delta > 0:
            return delta
        else:
            raise ValueError("Time continuum break: birth year later than current year.")
    
class Team:
    def __init__(self, name:str):
        self.name = name
        self._players = []

    def __repr__(self):
        return self.name + ':\n' + '\n'.join([str(p) for p in self.players]) + '\n'

    @property
    def size(self):
        return len(self._players)

    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, player:Player):
        if player not in self.players:
            self._players = player
        else:
            raise Exception("Player list already populated, please use add_player")


    def add_player(self, player:Player) -> None:
        # no check if player or not
        self._players.append(player)
        return None
    
    def remove_player(self, player:Player) -> None:
        try:
            self._players.remove(player)
            return None
        except ValueError:
            print("Player not in team")

    def total_attendance(self) -> int:
        att = 0
        for player in self.players:
            att += player.attendance
        return att
    
    def mean_age(self) -> float:
        age = 0
        for player in self.players:
            age += player.age()
        try:
            age = float(age/self.size)
            return age
        except ZeroDivisionError:
            return 0
    

    def validate():
        ...

    def info(self) -> tuple[str]:
        return self.name, self.total_attendance(), self.mean_age()



# so for property setters/getters to work we need new style classes and specify inheritance (i.e. object here)
class Championship(Sequence):
    def __init__(self):
        # dictionary = { Team.name = Team }
        self._teams = {}
    
    # we made it iterable, let's make it a sequence as well at this point
    def __getitem__(self, key):
        return self._teams[key]
    # def __setitem__(self, key, value):
    #     self._teams[key] = value
    # this is mandatory when defining get item :(
    def __len__(self):
        return len(self._teams)
    
    # to make championship terable we pass to next its list version
    def __iter__(self):
        self.list = self.to_list()
        self.index = 0
        return self

    def __next__(self) -> str:
        try:
            key = self.list[self.index].name
        except IndexError: # with list index error comes for free ;)
            raise StopIteration
        self.index += 1
        return key

    def __repr__(self):
        return '\n'.join([ str(self[team]) for team in self ])
    
    @property
    def teams(self):
        return self._teams
    
    # This adds the team to self.teams but be careful, this is not a dictionary call!
    # you should write: self.teams = team AND NOT [self.teams[team.name] = team]
    @teams.setter 
    def teams(self, team:Team) -> NoReturn:
        if team.name not in self._teams:
            self._teams[team.name] = team
        else:
            raise Exception("Team list already populated, please use add_team")
        
    def add_team(self, team:Team) -> None:
        # no check if team or not
        self._teams[team.name] = team
        return None
    
    def remove_team(self, team:Team) -> None | NoReturn:
        try:
            del self._teams[team]
            return None
        except ValueError:
            print("Team not in championship")

    def to_list(self) -> list[Team]:
        return [ self.teams[name] for name in self.teams ]
    

    def from_file(self, path:str) -> None:
        file_lines = parse_file(path)
        for lines in file_lines:
            *kplayer, kteam = lines.split(";")
            p = Player(*kplayer)
            # if team already exists the setter throws an exception >:)
            try:
                self.teams = Team(kteam)
            except:
                pass
            self.teams[kteam].add_player(p)

    # one line implementation
    def attendance(self) -> dict[str: int]:
        return dict(sorted([(team.name, team.total_attendance()) for team in self.to_list()], key=(lambda a: a[1]), reverse=True ))

    def age(self) -> dict[str: list[Player]]:
        d = self
        for team in self:
            d[team].players.sort(key=lambda a: a.age(), reverse=True)
        return d
    
    def top_attendance(self) -> dict[str: list[Player]]:
        d = self
        for team in self:
            d[team].players.sort(key=lambda a: a.attendance, reverse=True)
            d[team].players = d[team].players[0:3]
        return d



