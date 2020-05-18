from ActionHandler import RegisterHandler, LoginHandler, LogoutHandler, FoodHandler, AddFoodHandler, EatFoodHandler

class Mediator:
    handlerMap = {
        'register': RegisterHandler,
        'login': LoginHandler,
        'logout': LogoutHandler,
        'food': FoodHandler,
        'addfood': AddFoodHandler,
        'eatfood': EatFoodHandler
    }

    def handle(self, request):
        action, _ = request
        handlerType = self.handlerMap[action]
        handler = handlerType()

        return handler.handle(request)

    def handleData(self, action, data, state):
        if action == 'login':
            if data is not None:
                state.setUser(data[0])
                print(f"Login succesful. Logged in as {state.active_user.username}")
            else:
                print(f"Wrong username or password.")

        if action == 'food':
            state.setFoodData(data)
            print()
            for food in data:
                print(f'{food[1]:<10}: quantity {food[2]} calories {food[3]} expires {food[5]}   [{food[0]:2}]')