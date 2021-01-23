class Car:

    def __init__(self):
        #These are private variables
        self.__maxspeed = 200
        self.__name = "Prius"
        self.__updateSoftware()
        #protected variable - can technically change but the developer shouldn't
        self._make = "Toyota"

    def drive(self):
        print('driving ' + self._make + ' ' + self.__name + '. maxspeed ' + str(self.__maxspeed))

    #private function
    def __updateSoftware(self):
        print("updating software")

    #sets the value of a private variable, this is not accessible from an object but will be called when the object is created
    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

#create a car object and call the drive method
redcar = Car()
redcar.drive()

#will not change the data because it's private
redcar.__maxspeed = 10
redcar.drive()

#can pass a value the function that sets the value of the private variable though
redcar.setMaxSpeed(320)
redcar.drive()


