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

    def __init__(self, text_of_news, city):
        self.publication_date = datetime.now().strftime("%Y/%m/%d %H:%M")
        self.__text_of_news = text_of_news
        self.__city = city

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

    def create_news_publication(self):
        news_publication = f'News___________________________________\n' \
                           f'{self.text_of_news}\n' \
                           f'{self.city}, {self.publication_date}\n' \
                           f'_______________________________________\n\n'
        return news_publication


class PrivateAd:

    def __init__(self, advertisement_text, expiration_date):
        self.__advertisement_text = advertisement_text
        self.__expiration_date = expiration_date

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

    def create_ad_publication(self):
        ad_publication = f'Private ad_____________________________\n' \
                           f'{self.advertisement_text}\n' \
                           f'Actual until: {self.expiration_date}, {self.number_of_days_left()} days left\n' \
                           f'_______________________________________\n\n'
        return ad_publication


class Greetings:
    header = 'Greeting in foreign language--\n'
    end_of_record = '------------------------------\n\n'
    GREETINGS = ['Spanish: hola', 'French: bonjour', 'German: guten tag', 'Italian: salve',
                 'Chinese: nin hao', 'Portuguese: ola', 'Arabic: asalaam alaikum', 'Japanese: konnichiwa',
                 'Korean: anyoung haseyo', 'Russian: Zdravstvuyte']
    number_of_languages = len(GREETINGS)

    def __init__(self):
        greeting_picker = randrange(Greetings.number_of_languages)
        self.greeting = Greetings.GREETINGS[greeting_picker]

    def create_greeting(self):
        greeting_publication = f'Greeting_______________________________\n' \
                         f'{self.greeting}\n' \
                         f'_______________________________________\n\n'
        return greeting_publication


def create_news():
    text_of_news = input('Enter text of the news: ')
    city = input('Enter city: ')

    record = News(text_of_news, city)

    with open('hw_05_result.txt', 'a') as result:
        result.write(record.create_news_publication())


def create_private_ad():
    advertisement_text = input('Enter text of the Private Ad: ')

    while True:
        try:
            expiration_date = datetime.strptime(input('Enter expiration date (dd/mm/yyyy):'), '%d/%m/%Y')
            expiration_date = expiration_date.date()
            if expiration_date < date.today():
                print("Enter valid date. We don't have timemachine yet.")
            else:
                break
        except ValueError as e:
            print(f'Input value must be numerical.\n{e}')

    record = PrivateAd(advertisement_text, expiration_date)

    with open('hw_05_result.txt', 'a') as result:
        result.write(record.create_ad_publication())


def add_greeting():
    record = Greetings()

    with open('hw_05_result.txt', 'a') as result:
        result.write(record.create_greeting())


def main():
    while True:
        try:
            print('Choose type of record: 1 - News, 2 - Private Ad, 3 - Random Fact, 0 - EXIT PROGRAM')
            x = int(input('Enter single digit 0-3:'))
            if x == 0:
                print('Goodbye!')
                break
            elif x == 1:
                create_news()
            elif x == 2:
                create_private_ad()
            elif x == 3:
                add_greeting()
            else:
                print('Number is out of scope. Choose correct number from menu.')
        except ValueError as e:
            print(f'Input value must be single digit from 0 to 3!\n{e}')


if __name__ == '__main__':
    main()
