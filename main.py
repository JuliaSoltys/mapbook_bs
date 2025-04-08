users = [
    {"name": "Julia", "location": "Rzeszów", "posts": 500},
    {"name": "Michał", "location": "Krasnystaw", "posts": 400},
    {"name": "Ksavier", "location": "Grudziądz", "posts": 300},
    {"name": "Damian", "location": "Krakow", "posts": 200},

]

# twój znajomy Michał z miejscowości Krasnystaw opublikował 400 postów
for user in users:
    print(f"Twój znajomy {user['name']}, z miejscowości {user['location']}, opublikował {user['posts']}")
