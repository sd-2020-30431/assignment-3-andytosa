from User import User
from FoodItem import FoodItem

class RegisterHandler:
    def handle(self, request):
        username = input('username: ')
        password = input('password: ')
        email = input('email: ')

        return (self.registerUser(User(None, username, password, email)), False, True)
    
    def registerUser(self, user):
        return f"INSERT INTO users (username, password, email) VALUES ('{user.username}', '{user.password}', '{user.email}');"

class LoginHandler:
    def handle(self, request):
        username = input('username: ')
        password = input('password: ')

        return (self.loginUser(username, password), True, True)
    
    def loginUser(self, username, password):
        return f"SELECT * FROM users WHERE users.username = '{username}' AND users.password = '{password}'"

class LogoutHandler:
    def handle(self, request):
        _, state = request
        state.logOutUser()
        print('User logged out.')
        return (None, None, True)

class FoodHandler:
    def handle(self, request):
        _, state = request
        user = state.active_user
        if user is None:
            return (None, False, False)

        return (self.selectFood(user.getID()), True, True)
    
    def selectFood(self, user_id):
        return f"SELECT * FROM foods WHERE foods.user_id = {user_id}"


class AddFoodHandler:
    def handle(self, request):
        _, state = request
        user = state.active_user
        if user is None:
            return (None, False, False)
        
        name = input('name: ')
        quantity = input('quantity: ')
        calories = input('calories: ')
        print('(date format YYYY-MM-DD)')
        buy_date = input('buy date: ')
        exp_date = input('exp date: ')
        
        food = FoodItem(name, quantity, calories, buy_date, exp_date, state.active_user.getID())
        return (self.insertFood(food), False, True)
    
    def insertFood(self, food):
        return f"""INSERT INTO foods (name, quantity, calories, buy_date, exp_date, user_id) VALUES (
            '{food.name}',
            {food.quantity},
            {food.calories}, 
            '{food.buy_date}', 
            '{food.exp_date}', 
            {food.user_id}
            );"""


class EatFoodHandler:
    def handle(self, request):
        food_id = input('food id: ')

        return (self.deleteFood(food_id), False, True)

    def deleteFood(self, food_id):
        return f"DELETE FROM foods WHERE id = {food_id}"
    


#return (None, None, False)



    



    
    
    

    

