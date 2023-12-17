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


# utilities dealing with I/O, etc...
from typing import Any


# these are the actual functions to be called
def report(path:str, c:Any):
    report_to_file(path, c)

def report_age(path:str, c:Any):
    report_to_file(path, c, "age")

def report_attendance(path:str, c:Any):
    report_to_file(path, c, "att")

def report_top_attendance(path:str, c:Any):
    report_to_file(path, c, "top_att")

def info(c:Any):
    print(c.info())



# add os.path.exists(path) to io methods, not to remove or create the wrong files

def parse_file(path:str) -> list[str]:
    try:
        with open(path, "r") as fp:
            file_lines = fp.readlines()
        for i, line in enumerate(file_lines):
            file_lines[i] = line.strip()
        return file_lines

    except FileNotFoundError as f:
            print(f, "\nCheck path")

def from_prop(c:Any, prop:str) -> dict[str: Any]:
    
    match prop:
        case "att":
            return c.attendance()
        case "top_att":
            return c.top_attendance()
        case "age":
            return c.age()
        case None:
            return c

# print to file a dictionary of the form { string: Any }
def report_to_file(path:str, c:Any, prop:str=None):
    try:
        data = from_prop(c, prop)
    except:
        data = c
    
    # implement checking if file exists alreay
    try:
        with open(path, "w") as fp:
            for k in data:
                # i wrote data[k] instead of data.teams[k] so for revenge i made
                # my classes be sequences
                fp.write(str(data[k])) # note, write doesn't call __str__ like print, so you have to convert on your own babe
    except:
         print("Invalid path!")


