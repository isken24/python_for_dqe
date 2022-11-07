""" Home task 08:
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed"""


from home_task_06 import create_news, create_private_ad, add_greeting
import os
import logging
import json


class JSONReader:
    def __init__(self, file_path=None):
        if file_path:
            self.path = file_path       # Alternative file path: '../hw_08/alternative_input_08.json'
        else:
            self.path = '../hw_08/input_08.json'
        with open(self.path, 'r') as source_file:
            self.content = json.load(source_file)


def parse_json(input_file):
    input_data = input_file.content
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
    parse_json(input_file)
