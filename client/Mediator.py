from ActionHandler import RegisterHandler, LoginHandler, LoginHandler, FoodHandler, AddFoodHandler, EatFoodHandler

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
        action, state = request
        handlerType = self.handlerMap[action]
        handler = handlerType()

        return handler.handle(request)