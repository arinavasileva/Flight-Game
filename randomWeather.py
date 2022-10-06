import random


def random_weather():
    temperature = random.randint(-40, 40)
    conditions = random.choice(['Clouds', 'Clear'])
    wind = random.randint(0, 15)

    randomized_weather = (temperature, conditions, wind)

    return randomized_weather


print(random_weather())