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

from typing import Self



class Table:

    truncate: int = 3 # how many rows to show in table representation
    
    def __init__(self) -> None:
        self.title: list | None = None # column titles
        self.ignore = None # data to treat as missing
        self.default = None # value to use when data is missing

        self.table : list[list] | None = None


    @property
    def table(self):
        self.table: list[list] | None = None # list of rows
    
    @table.setter
    def table(self, value:list[list]) -> None:
        if len(self.table) == 0:
            self.table = value
        else:
            raise Exception('Table already populated')
        
    @table.getter
    def table(self):
        if self.table != None:
            return self.table
        else:
            raise Exception('Table unset')
        
    # doesn't show full table but stops at self.truncate which is 3 by default
    # col1 col2 col3
    # val1 val2 val3
    # val1 val2 val3
    # val1 val2 val3
    # .  .  .
    # .  .
    # .     .
    def __repr__(self):
        l = len(self.table)
        return '\n'.join([', '.join(self.title)] +\
                         [', '.join(self.title[i]) for i in range(max(self.truncate, l))])\
                         (+ '\n.  .  .\n.  .\n.     .' if l > 3 else '')
    
    def __len__(self) -> tuple[int,int]:
        return len(self.table, self.title) # rows x columns

    # transpose Table, i.e. table[x][y] == table.transpose()[y][x]
    def transpose(self) -> Self:
        t = Table()
        for index in len(self.titles):
            ...
        return t
    
    def insert_column(self, index) -> None:
        ...

    def insert_row(self, index) -> None:
        ...

    def column(self, index) -> list | None:
        col = []
        try:
            for row in self.table:
                col.append(row[index])
        except IndexError:
            col = None
        return col


    def titles(self) -> list:
        ...
    # this might be useless
    # def get_row(self, index) -> list:
    #     ...








