import app

def print_app2():
    name  = (__name__)
    return name

if __name__ == "__main__":
    # dunder main is the script being run when you use the run command. If it's not the dunder main you are calling it outside
    #the following is calling code within this script
    print("I am running code from {}".format(print_app2()))

    #the following is calling code from the imported app.py
    print("I am running code from {}".format(app.print_app()))
