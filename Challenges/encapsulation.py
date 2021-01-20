#protected class
class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

#create private object
obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
