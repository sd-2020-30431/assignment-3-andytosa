from User import User
from FoodItem import FoodItem
from UserInterface import UserInterface

class ActionHandler:

    def getCommand(self, action, state):
        if action == 'register':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            return (self.registerUser(User(username, password, email)), False, True)
        
        if action == 'login':
            username = input('username: ')
            password = input('password: ')

            return (self.loginUser(username, password), True, True)

        if action == 'logout':
            state.logOutUser()
            print('User logged out.')
            return (None, None, True)

        if action == 'food':
            user = state.active_user
            if user is None:
                return (None, False, False)

            return (self.selectFood(user.getID()), True, True)
        
        if action == 'addfood':
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
 
        if action == 'eatfood':
            food_id = input('food id: ')

            return (self.deleteFood(food_id), False, True)

        return (None, None, False)


    def handleData(self, action, data, state):
        if action == 'login':
            if data is not None:
                state.setUser(data[0])
                print(f"Login succesful. Logged in as {state.active_user.username}")
            else:
                print(f"Wrong username or password.")

        if action == 'food':
            state.setFoodData(data)
            UserInterface.printFood(data)


    def registerUser(self, user):
        return f"INSERT INTO users (username, password, email) VALUES ('{user.username}', '{user.password}', '{user.email}');"


    def insertFood(self, food):
        return f"""INSERT INTO foods (name, quantity, calories, buy_date, exp_date, user_id) VALUES (
            '{food.name}',
            {food.quantity},
            {food.calories}, 
            '{food.buy_date}', 
            '{food.exp_date}', 
            {food.user_id}
            );"""
    
    def deleteFood(self, food_id):
        return f"DELETE FROM foods WHERE id = {food_id}"
    
    def selectFood(self, user_id):
        return f"SELECT * FROM foods WHERE foods.user_id = {user_id}"


    def loginUser(self, username, password):
        return f"SELECT * FROM users WHERE users.username = '{username}' AND users.password = '{password}'"

