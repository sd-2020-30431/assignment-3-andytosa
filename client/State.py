from User import User
class State:
    active_user = None
    food_list = None

    def setUser(self, data):
        self.active_user = User(data[0], data[1], data[2], data[3])

    def setFoodData(self, data):
        self.food_list = data

    def logOutUser(self):
        self.active_user = None
