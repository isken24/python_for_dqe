"""
Home task 09:
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""


from hw_04.home_task_04_part_2 import capitalize_text
from hw_06.home_task_06 import News, PrivateAd, Greetings, get_expiration_date
import os
import xml.etree.ElementTree as ET
import logging


logging.basicConfig(level=logging.INFO, filename=f"{os.getcwd()}/logs/feed_writer.log",
                    filemode="a", format="%(asctime)s %(message)s")


class XMLParser:
    def __init__(self, filepath='../input/input_09.xml'):
        self.filepath = filepath
        self.read_xml()
        self.write_feed_from_xml()

    def read_xml(self):
        xml_file = ET.parse(self.filepath)
        self.content = xml_file.getroot()

    def write_feed_from_xml(self):
        feed_path = f'{os.getcwd()}/feed_writer_result.txt'
        with open(feed_path, 'a') as feed:
            for record in self.content:
                record_type = record.find('record_type').text.lower()
                record_text = capitalize_text(record.find('record_text').text)
                if record_type == 'news':
                    city = capitalize_text(record.find('city').text)
                    news = News(record_text, city)
                    feed.write(news.create_news_publication())
                elif record_type == "ad":
                    expiration_date = get_expiration_date(record.find('expiration_date').text)
                    ad = PrivateAd(record_text, expiration_date)
                    feed.write(ad.create_ad_publication())
                elif record_type == "greeting":
                    greeting = Greetings()
                    feed.write(greeting.create_greeting())
                else:
                    logging.info(f"Wrong type of record: {record_type}. record_text:{record_text}")
            os.remove(self.filepath)


if __name__ == '__main__':
    alternative_filepath = input("Specify alternative filepath or press Enter:")     # Alternative filepath: '../hw_08/alt_input_09.xml'
    if alternative_filepath:
        XMLParser(alternative_filepath)
    else:
        XMLParser()
