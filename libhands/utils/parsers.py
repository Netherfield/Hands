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
from typing import Any
from csv import reader,writer
from libhands.objects.tables import Table


# methods to parse csv based on known class types and matching column types
# - From csv form Table object
# - From class instance c fill instance with table values | create list with filled instances
# - Extract column function
# - ? page functionality, estract only n lines

class Thumb(Table):
    def __init__(self) -> None:
        ...

    # parses csv into a table object
    def parse(self, path:str, *, sep=',') -> None:
        with open(path, 'r', newline='') as fp:
            ptr = reader(fp, delimiter=sep)
            'rewrite with proper methods of the Table class'
            # self.title = ptr.__next__()
            # self.table = []
            # for line in ptr:
            #     self.table.append(line)

    def column(self, path:str, value:str, *, sep=',') -> list | None:
        with open(path, 'r', newline='') as fp:
            ptr = reader(fp, delimiter=sep)
            'rewrite with the methods of the table class'
            # titles = ptr.__next__()
            # try:
            #     index = titles.index(value)
            #     col = []
            #     for line in ptr:
            #         col.append(line[index])
            # except:
            #     col = None
            # return col


    # parse c.__dict__to search value names matching
    # even partially the table's headers
    def autocompile(self, c:Any, *, extend:bool=True) -> None | list:
        # a loop like this:
        """for att in c.__dict__:
            c.__dict__[att] = self.table[att]"""
        



