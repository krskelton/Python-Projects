def getName(name = ""):
     name = askName(name)
     print("Thank you, welcome {}!".format(name))
def askName(name):
     go = True
     while go:
         if name == "":
             name = input("Please enter your name:\n>>> ")
             if name != "":
                 go = False
                 return name
     
if __name__ == '__main__':
     getName()
