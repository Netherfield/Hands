import os

if len(os.sys.argv) > 1 and os.sys.argv[1] == "--with-dep":
    print("Installing required dependencies")
    os.system("py -m pip install --no-input -r requirements.txt")

else:
    print("Running without dependencies:")

main = os.path.join('./championship-manager/', '__main__.py')
os.system("py " +  main)

try:
    # clean up environment at the end of execution
    os.system("pyclean .")
except:
    print("pyclean . \nFailed execution. Exiting...")