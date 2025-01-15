import random

COUNTRIES = ['Республика Беларусь', 'Российская Федерация', 'Республика Казахстан', 'Республика Армения',
             'Республика Сербия']
LEADERS = ['Владимир Владимирович Путин', 'Александр Вучич', 'Александр Григорьевич Лукашенко',
           'Гарникович Ваагн Хачатурян', 'Кемелевич Касым-Жомарт Токаев']
CONTINENTS = ['Европа', 'Азия', 'Африка', 'Австралия', 'Северная Америка', 'Южная Америка']

def random_country():
    return random.choice(COUNTRIES)

def random_leader():
    return random.choice(LEADERS)

def random_continent():
    return random.choice(CONTINENTS)

def main():
    for i in range(random.randint(2, 4)):
        print(f'''Страна: {random_country()} | Президент: {random_leader()} | Континент: {random_continent()}''')

main()