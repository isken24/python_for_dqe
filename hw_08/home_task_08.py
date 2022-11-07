""" Home task 08:
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed"""


from home_task_04_part_2 import text_normalization
from datetime import datetime, date
from random import randrange
import os
import logging
import json


logging.basicConfig(level=logging.INFO, filename="../hw_08/hw_08.log", filemode="a",
                    format="%(asctime)s %(message)s")


class Publication:
    def __init__(self, text_of_publication):
        self.text_of_publication = text_of_publication


class News(Publication):
    def __init__(self, text_of_publication, city):
        super().__init__(text_of_publication)
        self.publication_date = datetime.now().strftime("%Y/%m/%d %H:%M")
        self.city = city

    def create_news_publication(self):
        news_publication = f'News___________________________________\n' \
                           f'{self.text_of_publication}\n' \
                           f'{self.city}, {self.publication_date}\n' \
                           f'_______________________________________\n\n'
        return news_publication


class PrivateAd(Publication):
    def __init__(self, text_of_publication, expiration_date):
        super().__init__(text_of_publication)
        self.expiration_date = expiration_date

    def get_number_of_days_left(self):
        number_of_days_left = self.expiration_date - date.today()
        number_of_days_left = number_of_days_left.days
        return number_of_days_left

    def create_ad_publication(self):
        ad_publication = f'Private ad_____________________________\n' \
                           f'{self.text_of_publication}\n' \
                           f'Actual until: {self.expiration_date}, {self.get_number_of_days_left()} days left\n' \
                           f'_______________________________________\n\n'
        return ad_publication


class Greetings:
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


def create_news(raw_record):
    raw_record = text_normalization(raw_record).split('. ')
    text_of_publication = '. '.join(raw_record[:-1])
    city = raw_record[-1]

    record = News(text_of_publication, city)

    with open('hw_08_result.txt', 'a') as result:
        result.write(record.create_news_publication())


def create_private_ad(raw_record):
    raw_record = raw_record.split('. ')
    advertisement_text = text_normalization('. '.join(raw_record[:-1]))

    try:
        expiration_date = datetime.strptime(raw_record[-1], '%d/%m/%Y')
        expiration_date = expiration_date.date()
        if expiration_date < date.today():
            logging.info(f"Outdated advertisement! Record: {advertisement_text}; expiration_date: {expiration_date}")
            expiration_date = date.today()

    except ValueError as e:
        expiration_date = date.today()      # In case of ValueError advertisement will be published only for 1 day.
        logging.info(f"Wrong date format at Record: {advertisement_text}")

    record = PrivateAd(advertisement_text, expiration_date)

    with open('hw_08_result.txt', 'a') as result:
        result.write(record.create_ad_publication())


def add_greeting():
    record = Greetings()

    with open('hw_08_result.txt', 'a') as result:
        result.write(record.create_greeting())


class JSONReader:
    def __init__(self, file_path=None):
        if file_path:
            self.path = file_path       # Alternative file path: '../hw_08/alternative_input_08.json'
        else:
            self.path = '../hw_08/input_08.json'
        with open(self.path, 'r') as source_file:
            self.content = json.load(source_file)


def parse_json(input_data):
    for message in input_data:
        record_type = message['record_type'].lower()
        raw_record = message['content']
        if record_type == "news":
            create_news(raw_record)
        elif record_type == "ad":
            create_private_ad(raw_record)
        elif record_type == "greeting":
            add_greeting()
        else:
            logging.info(f"Wrong type of record: {record_type}/{raw_record}.")
    os.remove(input_file.path)


if __name__ == '__main__':
    input_file = JSONReader(input('Provide path to the input file:'))
    input_data = input_file.content
    parse_json(input_data)
