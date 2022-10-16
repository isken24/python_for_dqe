"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.

Each new record should be added to the end of file. Commit file in git for review.
"""


from datetime import datetime, date
from random import randrange


class News:
    header = 'News -------------------------\n'
    end_of_record = '------------------------------\n\n'

    def __init__(self):
        self.publication_date = datetime.now()
        self.__text_of_news = ''
        self.__city = ''

    @property
    def text_of_news(self):
        return self.__text_of_news

    @text_of_news.setter
    def text_of_news(self, text_of_news):
        self.__text_of_news = text_of_news

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    def add_timestamp(self):
        timestamp = self.publication_date.strftime("%Y/%m/%d %H:%M")
        return timestamp


class PrivateAd:
    header = 'Private Ad ------------------\n'
    end_of_record = '------------------------------\n\n'

    def __init__(self):
        self.__advertisement_text = ''
        self.__expiration_date = date.today()

    @property
    def advertisement_text(self):
        return self.__advertisement_text

    @advertisement_text.setter
    def advertisement_text(self, advertisement_text):
        self.__advertisement_text = advertisement_text

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    def number_of_days_left(self):
        number_of_days_left = self.__expiration_date - date.today()
        number_of_days_left = number_of_days_left.days
        return number_of_days_left


class Greetings:
    header = 'Greeting in foreign language--\n'
    end_of_record = '------------------------------\n\n'
    GREETINGS = ['Spanish: hola', 'French: bonjour', 'German: guten tag', 'Italian: salve',
                 'Chinese: nin hao', 'Portuguese: ola', 'Arabic: asalaam alaikum', 'Japanese: konnichiwa',
                 'Korean: anyoung haseyo', 'Russian: Zdravstvuyte']
    number_of_languages = len(GREETINGS)

    def __init__(self):
        randomizer = randrange(Greetings.number_of_languages)
        self.greeting = Greetings.GREETINGS[randomizer]

    def get_greeting(self):
        return self.greeting


def create_news():
    record = News()
    record.text_of_news = input('Enter text of the news: ')
    record.city = input('Enter city: ')

    with open('hw_05_result.txt', 'a') as result:
        result.write(f'{record.header}'
                     f'{record.text_of_news}\n'
                     f'{record.city}, {record.add_timestamp()}\n'
                     f'{record.end_of_record}')


def create_private_ad():
    record = PrivateAd()
    record.advertisement_text = input('Enter text of the Private Ad: ')
    while True:
        try:
            record.expiration_date = datetime.strptime(input('Enter expiration date (dd/mm/yyyy):'), '%d/%m/%Y')
            record.expiration_date = record.expiration_date.date()
            if record.expiration_date < date.today():
                print("Enter valid date. We don't have timemachine yet.")
                continue
            else:
                break
        except ValueError as e:
            print(f'Input value must be numerical.\n{e}')
            continue

    with open('hw_05_result.txt', 'a') as result:
        result.write(f'{record.header}'
                     f'{record.advertisement_text}\n'
                     f'Actual until: {record.expiration_date}, {record.number_of_days_left()} days left'
                     f'\n{record.end_of_record}')


def add_greeting():
    record = Greetings()
    with open('hw_05_result.txt', 'a') as result:
        result.write(f'{record.header}'
                     f'{record.get_greeting()}'
                     f'\n{record.end_of_record}')


def main():
    while True:
        try:
            print('Choose type of record: 1 - News, 2 - Private Ad, 3 - Random Fact, 0 - EXIT PROGRAM')
            x = int(input('Enter single digit 0-3:'))
            if x == 0:
                print('Good buy!')
                break
            elif x == 1:
                create_news()
                continue
            elif x == 2:
                create_private_ad()
                continue
            elif x == 3:
                add_greeting()
                continue
            else:
                print(f'Input value must be single digit from 0 to 3!')
                continue
        except ValueError as e:
            print(f'Input value must be single digit from 0 to 3!\n{e}')
            continue


if __name__ == '__main__':
    main()
