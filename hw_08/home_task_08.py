""" Home task 08:
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed"""


from home_task_04_part_2 import text_normalization
from hw_06.home_task_06 import News, PrivateAd, Greetings, get_expiration_date
import os
import logging
import json


class JSONParser:
    def __init__(self, filepath='../hw_08/input_08.json'):
        self.filepath = filepath
        self.read_json()
        self.create_feed_from_json()

    def read_json(self) -> None:
        with open(self.filepath, 'r') as source_file:
            self.content = json.load(source_file)

    def create_feed_from_json(self) -> None:
        feed_path = f'{os.getcwd()}/result.txt'
        with open(feed_path, 'a') as feed:
            for record in self.content:
                record_type = record['record_type'].lower()
                record_text = text_normalization(record['record_text'])
                if record_type == 'news':
                    city = text_normalization(record['city'])
                    news = News(record_text, city)
                    feed.write(news.create_news_publication())
                elif record_type == "ad":
                    expiration_date = get_expiration_date(record['expiration_date'])
                    ad = PrivateAd(record_text, expiration_date)
                    feed.write(ad.create_ad_publication())
                elif record_type == "greeting":
                    greeting = Greetings()
                    feed.write(greeting.create_greeting())
                else:
                    logging.info(f"Wrong type of record: {record_type}/{record_text}.")
            os.remove(self.filepath)


if __name__ == '__main__':
    alternative_filepath = input("Specify alternative filepath or press Enter:")     # Alternative filepath: '../hw_08/alt_input_08.json'
    if alternative_filepath:
        JSONParser(alternative_filepath)
    else:
        JSONParser()
