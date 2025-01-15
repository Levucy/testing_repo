import random

COUNTRIES = ['Республика Беларусь', 'Российская Федерация', 'Республика Казахстан']

def random_country():
    print(random.choice(COUNTRIES))

def main():
    for i in range(3):
        random_country()

main()