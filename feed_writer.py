from hw_06.home_task_06 import write_feed_from_txt
from hw_08.home_task_08 import JSONParser
from hw_09.home_task_09 import XMLParser
import os


class FeedWriter:
    TXT = '.txt'
    JSON = '.json'
    XML = '.xml'

    def __init__(self, filepath=f'{os.getcwd()}/input/input_06.txt'):
        self.filepath = filepath
        self.file_name = os.path.basename(self.filepath)
        self.write_feed()

    def write_feed(self):
        if self.file_name.lower().endswith(self.TXT):
            write_feed_from_txt(self.filepath)
        elif self.file_name.lower().endswith(self.JSON):
            JSONParser(self.filepath)
        elif self.file_name.lower().endswith(self.XML):
            XMLParser(self.filepath)
        else:
            print("Wrong file format. Allowed file formats: TXT, JSON, XML")


if __name__ == '__main__':
    alternative_filepath = input("Specify alternative filepath or press Enter:")
    if alternative_filepath:
        FeedWriter(alternative_filepath)
    else:
        FeedWriter()
