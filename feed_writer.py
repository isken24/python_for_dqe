from hw_06.home_task_06 import write_feed_from_txt
from hw_08.home_task_08 import JSONParser
from hw_09.home_task_09 import XMLParser
from hw_10.home_task_10 import DBWriter
import os


class FeedWriter:
    TXT = '.txt'
    JSON = '.json'
    XML = '.xml'

    def __init__(self, input_file_path=f'{os.getcwd()}/input/input_06.txt'):
        self.input_file_path = input_file_path
        self.input_file_name = os.path.basename(self.input_file_path)

    def write_feed_to_txt(self):
        if self.input_file_name.lower().endswith(self.TXT):
            write_feed_from_txt(self.input_file_path)
        elif self.input_file_name.lower().endswith(self.JSON):
            JSONParser(self.input_file_path)
        elif self.input_file_name.lower().endswith(self.XML):
            XMLParser(self.input_file_path)
        else:
            print("Wrong file format. Allowed file formats: TXT, JSON, XML")


if __name__ == '__main__':
    alternative_filepath = input("Specify alternative filepath or press Enter:")
    if alternative_filepath:
        feedwriter = FeedWriter(alternative_filepath)
    else:
        feedwriter = FeedWriter()

    while True:
        try:
            output_format_option = int(input("Select output format: 1 - write to '.txt' file; 2 - write to DB; 0 - EXIT \n"))
            if output_format_option == 1:
                feedwriter.write_feed_to_txt()
                print("Finished writing to text file. Closing the app...")
                break
            elif output_format_option == 2:
                DBWriter(feedwriter.input_file_path)
                print("Finished writing to DB. Closing the app...")
                break
            elif output_format_option == 0:
                print("Good bye!")
                break
            else:
                print("Wrong number, choose number from 0 to 2.")
        except ValueError as e:
            print(f'Input value must be single digit from 0 to 2!\n{e}')
