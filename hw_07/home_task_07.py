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


def file_reader(filepath) -> str:
    with open(filepath, 'r') as input_file:
        content = input_file.read().replace('_', '').replace('\n\n', '')
    return content


class Counter:
    def __init__(self, text: str):
        self.text = text
        self.total_number_of_letters = len(re.sub('[^a-zA-Z]+', '', self.text))
        self.words_counter()
        self.letters_counter()
        self.format_data_for_letters_count_csv()

    def words_counter(self) -> None:
        self.words_count = {}
        for word in self.text.lower().split():
            word = word.strip('.,')
            if word.isalpha():
                self.words_count[word] = self.words_count.get(word, 0) + 1
        self.words_count = list(self.words_count.items())

    def letters_counter(self) -> None:
        self.letters_count = {}
        self.upper_letters_count = {}
        all_letters_from_text = re.sub('[^a-zA-Z]+', '', self.text)
        for letter in all_letters_from_text:
            if letter.isupper():
                self.upper_letters_count[letter] = self.upper_letters_count.get(letter, 0) + 1
                self.letters_count[letter.lower()] = self.letters_count.get(letter.lower(), 0) + 1
            else:
                self.letters_count[letter] = self.letters_count.get(letter, 0) + 1

    def format_data_for_letters_count_csv(self) -> None:
        self.data_for_letters_count_csv = []
        for key, value in self.upper_letters_count.items():
            key = key.lower()
            if key in self.letters_count:
                letter_percentage = round(self.letters_count[key] / self.total_number_of_letters * 100, 1)
                self.data_for_letters_count_csv.append([key, self.letters_count[key], value, letter_percentage])
                del self.letters_count[key]
        for key, value in self.letters_count.items():
            letter_percentage = round(self.letters_count[key] / self.total_number_of_letters * 100, 1)
            self.data_for_letters_count_csv.append([key, self.letters_count[key], 0, letter_percentage])
        self.data_for_letters_count_csv = sorted(self.data_for_letters_count_csv)

    def write_words_count_csv(self) -> None:
        with open(f'hw_07_word_count.csv', 'w', encoding='UTF8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter='-')
            writer.writerows(self.words_count)

    def write_letter_count_csv(self) -> None:
        with open('hw_07_letter_count.csv', 'w', encoding='UTF8', newline='') as csv_file:
            fieldnames = ['letter', "count_all", "count_uppercase", "percentage"]
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows([fieldnames])
            writer.writerows(self.data_for_letters_count_csv)


if __name__ == '__main__':
    content = file_reader('../hw_06/hw_06_result.txt')

    counter = Counter(content)
    counter.write_words_count_csv()
    counter.write_letter_count_csv()
