"""
Home task 10
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
1.Different types of records require different data tables
2.New record creates new row in data table
3.Implement “no duplicate” check.
"""


import os
import sqlite3
import json
import xml.etree.ElementTree as ET
import logging
import re
from hw_04.home_task_04_part_2 import text_normalization, capitalize_text
from hw_06.home_task_06 import News, PrivateAd, Greetings, get_expiration_date


class DBWriter:

    conn = sqlite3.connect('hw_10.db')
    c = conn.cursor()

    def create_tables(self) -> None:
        with self.conn:
            try:
                self.c.execute("""CREATE TABLE news (
                       news_text text,
                       city text,
                       publication_date text,
                       unique (news_text, city, publication_date)
                       )""")
            except sqlite3.OperationalError as e:
                print(e)
            try:
                self.c.execute("""CREATE TABLE ads (
                               ad_text text,
                               expiration_date text,
                               number_of_days_left text,
                               unique (ad_text, expiration_date)
                               )""")
            except sqlite3.OperationalError as e:
                print(e)
            try:
                self.c.execute("""CREATE TABLE greetings (
                               greeting text,
                               unique (greeting)
                               )""")
            except sqlite3.OperationalError as e:
                print(e)

    def insert_news(self, news) -> None:
        with self.conn:
            try:
                self.c.execute("INSERT INTO news VALUES (:news_text, :city, :publication_date)",
                          {'news_text': news.text_of_publication, 'city': news.city,
                           'publication_date': news.publication_date})
            except sqlite3.IntegrityError as e:
                print(e, f'news_text: {news.text_of_publication}, city: {news.city}, '
                         f'publication_date: {news.publication_date}')

    def insert_advertisement(self, ad) -> None:
        with self.conn:
            try:
                self.c.execute("INSERT INTO ads VALUES (:ad_text, :expiration_date, :number_of_days_left)",
                          {'ad_text': ad.text_of_publication, 'expiration_date': ad.expiration_date,
                           'number_of_days_left': ad.number_of_days_left})
            except sqlite3.IntegrityError as e:
                print(e, f'ad_text: {ad.text_of_publication} expiration_date: {ad.expiration_date}, '
                         f'number_of_days_left: {ad.number_of_days_left}')

    def insert_greeting(self, greeting) -> None:
        with self.conn:
            try:
                self.c.execute("INSERT INTO greetings VALUES (:greeting)", {'greeting': greeting})
            except sqlite3.IntegrityError as e:
                print(e, f'greeting: {greeting}')

    def update_db_from_json(self, input_json) -> None:
        with open(input_json, 'r') as json_file:
            json_file.content = json.load(json_file)
            for record in json_file.content:
                record_type = record['record_type'].lower()
                record_text = text_normalization(record['record_text'])
                if record_type == 'news':
                    city = text_normalization(record['city'])
                    news = News(record_text, city)
                    self.insert_news(news)
                elif record_type == "ad":
                    expiration_date = get_expiration_date(record['expiration_date'])
                    ad = PrivateAd(record_text, expiration_date)
                    self.insert_advertisement(ad)
                elif record_type == "greeting":
                    greeting = Greetings().greeting
                    self.insert_greeting(greeting)
                else:
                    logging.info(f"Wrong type of record: {record_type}/{record_text}.")
        os.remove(input_json)

    def update_db_from_xml(self, input_xml) -> None:
        xml_file = ET.parse(input_xml)
        content = xml_file.getroot()
        for record in content:
            record_type = record.find('record_type').text.lower()
            record_text = capitalize_text(record.find('record_text').text)
            if record_type == 'news':
                city = capitalize_text(record.find('city').text)
                news = News(record_text, city)
                self.insert_news(news)
            elif record_type == "ad":
                expiration_date = get_expiration_date(record.find('expiration_date').text)
                ad = PrivateAd(record_text, expiration_date)
                self.insert_advertisement(ad)
            elif record_type == "greeting":
                greeting = Greetings().greeting
                self.insert_greeting(greeting)
        os.remove(input_xml)

    def update_db_from_txt(self, input_txt) -> None:
        with open(input_txt, 'r') as input_file:
            content = input_file.read()
            for line in content.split(';\n'):
                line = re.split('\: |\. ',line.strip('.'))
                type_of_record = line[0]
                if type_of_record == "News":
                    city = line[-1]
                    record_text = capitalize_text('. '.join(line[1:-1]))
                    news = News(record_text, city)
                    self.insert_news(news)
                elif type_of_record == "Ad":
                    record_text = capitalize_text('. '.join(line[1:-1]))
                    exp_date = line[-1]
                    expiration_date = get_expiration_date(exp_date)
                    ad = PrivateAd(record_text, expiration_date)
                    self.insert_advertisement(ad)
                elif type_of_record == "Greeting":
                    greeting = Greetings().greeting
                    self.insert_greeting(greeting)
                else:
                    if len(line) > 0:
                        logging.info(f"Wrong type of record: {line}/{record_text}")
        os.remove(input_txt)


if __name__ == '__main__':

    DBWriter().create_tables()
    DBWriter().update_db_from_json('../input/alt_input_08.json')
    DBWriter().update_db_from_xml('../input/alt_input_09.xml')
    DBWriter().update_db_from_txt('../input/input_06.txt')

"""
    DBWriter.c.execute("Drop TABLE news")
    DBWriter.c.execute("Drop TABLE ads")
    DBWriter.c.execute("Drop TABLE greetings")
"""
