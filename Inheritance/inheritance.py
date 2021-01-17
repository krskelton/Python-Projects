#create the parent class User
class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

#create the child class Employee. It will inherit all of the attributes from User as well as adding it's own
class Employee(User):
    base_pay = 11.00
    department = 'General'

#create the child class Customer. It will inherit all of the attributes from User as well as adding it's own
class Customer(User):
    mailing_address = ' '
    mailing_list = True
