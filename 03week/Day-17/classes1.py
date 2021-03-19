class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
    #pass
    #pass lets having empty class
    
# user_1 = User()
# user_1.id = '001'
# user_1.username = 'angela'
# user_2 = User()
# user_2.id = '002'
# user_2.username = 'artur'
user_1 = User('001', 'angela')
user_2 = User('002', 'artur')


print(user_1.username, user_2.username)


class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5)
# same as my_car.seats = 5