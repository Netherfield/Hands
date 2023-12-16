import os

from test.scenarios import scenario
from config import test_main,test_mode


if test_mode and test_main in [1,2]:
    try:
        scenario(test_main)
    except:
        print("Couldn't load scenario")

else:
    print("Invalid argument, exited")

# clean up environment at the end of execution
os.system("pyclean .")