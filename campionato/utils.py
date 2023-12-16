# utilities dealing with I/O, etc...
from typing import Any


# these are the actual functions to be called
def report_attendance(path:str, c:Any):
    report_to_file(path, c, "attendance")

def report_age(path:str, c:Any):
    report_to_file(path, c, "age")

def report_top_attendance(path:str, c:Any):
    report_to_file(path, c, "top_attendance")

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
    
    



def report(c:Any, prop:str) -> dict[str: Any]:
    
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
        data = report(c, prop)
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
         print("Invalid path?")


