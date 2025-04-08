users = [
    {"name": "Julia", "location": "Rzeszów", "posts": 500},
    {"name": "Michał", "location": "Krasnystaw", "posts": 400},
    {"name": "Ksavier", "location": "Grudziądz", "posts": 300},
    {"name": "Damian", "location": "Krakow", "posts": 200},

]


def get_user_info(users_data: list)->None:
    for user in users_data:
       print(f"Twój znajomy {user['name']}, z miejscowości {user['location']}, opublikował {user['posts']} postów")


get_user_info(users)