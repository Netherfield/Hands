
# don't import all, just keep the parts needed
from partecipants import Championship
from utils import *
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

        case 2:
            try:
                c.from_file(source)
            except:
                pass
            try:
                report(ftest["out"], c)
            except:
                pass
            try:
                report_age(ftest["age"], c)
            except:
                pass
            try:
                report_top_attendance(ftest["att"], c)
            except:
                pass

