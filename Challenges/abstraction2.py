from abc import ABC, abstractmethod

class Donation(ABC):
    #regular method that prints the donation amount
    def makeDonation(self, amount):
        print('Donation amount: $', amount)
    #abstract method that will be customized by each donation type
    @abstractmethod
    def thank(self, amount):
        pass
    
#Child class that prints a different thank you message.
#If it is a one-time donation they will simply be thanked for their gift
class OneTimeDonation(Donation):
    def thank(self, amount):
        print('Thank you for your donation of $' + str(amount))

#Child class that prints a different thank you message.
#if it is a monthly donation they will be notified that they will be charged monthly
class MonthlyDonation(Donation):
    def thank(self, amount):
        print('Thank you for your donation. You will be charged $' + str(amount) + ' monthly, until you cancel.')
        

#create new object of the child class OneTimeDonation
oneTimeDonation = OneTimeDonation()
#utilize the parent method makeDonation
oneTimeDonation.makeDonation(100)
#utilize the child method thank
oneTimeDonation.thank(100)

#create new object of the child class Monthly Donation
monthlyDonation = MonthlyDonation()
#utilize the parent method makeDonation
monthlyDonation.makeDonation(20)
#utilize the child method thank
monthlyDonation.thank(20)
