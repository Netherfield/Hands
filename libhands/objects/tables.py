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
# from libhands.extensions.decorators import expose
    

class Table:
    # class attributes
    truncate: int = 3 # how many rows to show in table representation

    def __init__(self) -> None:
        self.matrix: list[list] | None = None
        self.title: list | None = None
        self.row: list | None = None
        self.column: list | None = None
        self.tr: bool = False


    # right now table is a wrapper used to initialize matrix, title, row, column
    # inside matrix is stored the table + title
    # while 
    @property
    def table(self):
        return self.table
    
    @table.getter
    def table(self):
        return self.matrix
    
    # let's explain this mess. When you 
    @table.setter
    def table(self, t:Self | list[list]):
        if self.table == None:
            if isinstance(t,self.__class__):
                self.matrix = t.matrix
            elif isinstance(t, list):
                self.matrix = t
            self.title = self.matrix[0]
            self.row = self.matrix[1:]
            self.column = []
            for i in range(len(self.matrix[1])):
                self.column += [[]]
                for j in range(1, len(self.matrix)):
                    self.column[i] += [self.matrix[j][i]]
            
            '''Copy from other Table t or fill manually or don't copy?'''
            self.table = {'titles' : self.title, # table titles
                          'size' : (len(self.row), len(self.column)), # rows x columns
                          'type' : None,    # data type of the entries
                          'default' : None} # default value when data is missing
        else:
            raise Exception('Table already populated')


    # to me this looks like forbidden code, I am creating a class instance within the class
    # but since it works nothing bad can happen
    @property
    def transpose(self):
        t = Table()
        t.tr = not t.tr # set transposed to opposite
        t.table = [self.title] + [[]]   # create it with no row x column to not compute columns again
        t.row = self.column             # since it's just a matter of swapping them
        t.column = self.row
        return t

    # doesn't show full table but stops at self.truncate which is 3 by default
    # col1 col2 col3
    # val1 val2 val3
    # val1 val2 val3
    # val1 val2 val3
    # .  .  .
    # .  .
    # .     .
    # NOTE There were a million different ways to do this, all of them better, but I started doing it like this and 
    # I won't bother rewriting __repr__ no thanks
    def __repr__(self):
        l = len(self.row)
        f = lambda x, y: '\n'.join(y +\
                         [x(i) + ', '.join(list(map(lambda a: str(a), self.row[i]))) for i in range(min(self.truncate, l))])\
                         + ('\n.  .  .\n.  .\n.     .' if l > 3 else '')
        if self.tr:
            ret = f(lambda k: self.title[k] + ': ', [])
        else:
            ret = f(lambda k: '', [', '.join(self.title)])
        
        return ret
    
    def __len__(self) -> tuple[int,int]:
        return (len(self.column), len(self.row)) # rows x columns
    


t = Table()
t.table = [['ciao', 'bye'],[1,2],[3,4],[5,6]]
m1 = t.column[1]
t1 = t.transpose.row[1]
print(m1, t1, m1==t1,'\n')
print(t.transpose)

    

