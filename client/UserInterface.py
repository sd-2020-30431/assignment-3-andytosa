class UserInterface:
    def printFood(foods):
        print()
        for food in foods:
            print(f'{food[1]:<10}: quantity {food[2]} calories {food[3]} expires {food[5]}   [{food[0]:2}]')
