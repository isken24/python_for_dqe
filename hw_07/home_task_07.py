"""
Home Task 7:
Calculate number of words_count and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words_count are preprocessed in lowercase)
2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)
CSVs should be recreated each time new record added.
"""

import csv
import re


class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as input_file:
            self.content = input_file.read().replace('_', '').replace('\n\n', '')


def dict_to_list_converter(input_data: dict) -> list:
    output_data = []
    for key, value in input_data.items():
        output_data.append([key, value])
    return sorted(output_data)


class Counter:
    def __init__(self, text: str):
        self.text = text
        self.total_number_of_letters = len(re.sub('[^a-zA-Z]+', '', self.text))
        self.words_count = self.words_counter()
        self.letters_count, self.upper_letters_count = self.letters_counter()
        self.data_for_letters_count_csv = self.format_data()

    def words_counter(self) -> list:
        words_count = {}
        for word in self.text.lower().split():
            word = word.strip('.,')
            if word.isalpha():
                words_count[word] = words_count.get(word, 0) + 1
        return dict_to_list_converter(words_count)

    def letters_counter(self):
        letters_count = {}
        upper_letters_count = {}
        all_letters_from_text = re.sub('[^a-zA-Z]+', '', self.text)
        for letter in all_letters_from_text:
            if letter.isupper():
                upper_letters_count[letter] = upper_letters_count.get(letter, 0) + 1
                letters_count[letter.lower()] = letters_count.get(letter.lower(), 0) + 1
            else:
                letters_count[letter] = letters_count.get(letter, 0) + 1
        return letters_count, upper_letters_count

    def format_data(self):
        data_for_letter_count_csv = []
        for key, value in self.upper_letters_count.items():
            key = key.lower()
            if key in self.letters_count:
                letter_percentage = round(self.letters_count[key] / self.total_number_of_letters * 100, 1)
                data_for_letter_count_csv.append([key, self.letters_count[key], value, letter_percentage])
                del self.letters_count[key]
        for key, value in self.letters_count.items():
            letter_percentage = round(self.letters_count[key] / self.total_number_of_letters * 100, 1)
            data_for_letter_count_csv.append([key, self.letters_count[key], 0, letter_percentage])
        return sorted(data_for_letter_count_csv)

    def write_words_count_csv(self):
        with open(f'hw_07_word_count.csv', 'w', encoding='UTF8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter='-')
            writer.writerows(self.words_count)

    def write_letter_count_csv(self):
        with open('hw_07_letter_count.csv', 'w', encoding='UTF8', newline='') as csv_file:
            fieldnames = ['letter', "count_all", "count_uppercase", "percentage"]
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows([fieldnames])
            writer.writerows(self.data_for_letters_count_csv)


if __name__ == '__main__':
    content = FileReader('../hw_06/hw_06_result.txt').content

    counter = Counter(content)
    counter.write_words_count_csv()
    counter.write_letter_count_csv()
