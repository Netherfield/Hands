
# don't import all, just keep the parts needed
from partecipants import Championship
from utils import report_to_file, info
from resources.data import *

from config import ftest, source

def scenario(n):
    c = Championship()
    match n:
        case 1:
            c.add_team(t1)
            c.add_team(t2)
            c[t1.name].add_player(p1)
            c[t2.name].add_player(p2)
            info(t1)
            print("Total attendance for "+ t1.name + ": " + str(t1.total_attendance()) )
            print("Mean age of "+ t1.name + ": " + str(t1.mean_age()) )
            print(c.attendance())

        # untested:
        case 2:
            try:
                c.from_file(source)
            except:
                pass
            try:
                report_to_file(ftest["out"], c)
            except:
                pass
            try:
                report_to_file(ftest["age"], c, "age")
            except:
                pass
            try:
                report_to_file(ftest["att"], c, "top_att")
            except:
                pass

