import random

COUNTRIES = ['Республика Беларусь', 'Российская Федерация', 'Республика Казахстан', 'Республика Армения']

def random_country():
    print(random.choice(COUNTRIES))

def main():
    for i in range(random.randint(1, 7)):
        random_country()

main()