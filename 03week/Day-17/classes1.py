class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
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

user_1.follow(user_2)

print(user_1.username, user_1.followers, user_1.following,'\n', user_2.username, user_2.followers, user_1.following)


class Car:
    def __init__(self, seats):
        self.seats = seats
        
    def enter_race_mode():
        self.seats = 2

my_car = Car(5)
# same as my_car.seats = 5