""" Home Task 7:
Calculate number of words_count and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words_count are preprocessed in lowercase)
2.letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)
CSVs should be recreated each time new record added."""

import csv


class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as input_file:
            self.content = input_file.read()


def dict_to_list_converter(input_data: dict) -> list:
    output_data = []
    for key, value in input_data.items():
        output_data.append([key, value])
    return sorted(output_data)


class Counter:
    def __init__(self, text: str):
        self.text = text
        self.total_number_of_letters = 0
        self.words_count = {}
        self.letters_count = {}
        self.upper_letters_count = {}
        self.words_counter()
        self.letters_counter()
        self.upper_letters_counter()

    def words_counter(self) -> dict:
        for line in self.text.lower().split('\n'):
            for word in line.split():
                word = word.strip('., ')
                if word.isalpha():
                    if word not in self.words_count:
                        self.words_count[word] = 1
                    else:
                        self.words_count[word] += 1
        return self.words_count

    def letters_counter(self) -> dict:
        for line in self.text.lower().split('\n'):
            for word in line.split():
                word = word.strip('., ')
                if word.isalpha():
                    for letter in word:
                        if letter not in self.letters_count:
                            self.letters_count[letter] = 1
                            self.total_number_of_letters += 1
                        else:
                            self.letters_count[letter] += 1
                            self.total_number_of_letters += 1
        return self.letters_count

    def upper_letters_counter(self) -> dict:
        for line in self.text.split('\n'):
            for word in line.split():
                word = word.strip('., ')
                if word.isalpha():
                    for letter in word:
                        if letter.isupper():
                            if letter not in self.upper_letters_count:
                                self.upper_letters_count[letter] = 1
                            else:
                                self.upper_letters_count[letter] += 1
        return self.upper_letters_count


class DataFormatterForLettersCSV:
    def __init__(self, letters_count, total_number_of_letters, upper_letters_count):
        self.upper_letters_count = upper_letters_count
        self.letters_count = letters_count
        self.total_number_of_letters = total_number_of_letters
        self.formatted_data = []
        self.format_data()

    def format_data(self):
        for key, value in self.upper_letters_count.items():
            key = key.lower()
            if key in self.letters_count:
                letter_percentage = round(self.letters_count[key] / self.total_number_of_letters * 100, 3)
                self.formatted_data.append([key, self.letters_count[key], value, letter_percentage])
                del self.letters_count[key]
        for key, value in self.letters_count.items():
            letter_percentage = round(self.letters_count[key] / self.total_number_of_letters * 100, 3)
            self.formatted_data.append([key, self.letters_count[key], 0, letter_percentage])
            self.formatted_data = sorted(self.formatted_data)
        return self.formatted_data


class WriterCSV:

    def write_word_count_csv(self, input_data: list):
        with open(f'hw_07_word_count.csv', 'w', encoding='UTF8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter='-')
            writer.writerows(input_data)

    def write_letter_count_csv(self, input_data: list):
        with open('hw_07_letter_count.csv', 'w', encoding='UTF8', newline='') as csv_file:
            fieldnames = ['letter', "count_all", "count_uppercase", "percentage"]
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows([fieldnames])
            writer.writerows(input_data)


if __name__ == '__main__':
    source_file = FileReader('../hw_06/hw_06_result.txt')
    content = source_file.content.replace('_', '').replace('\n\n', '')

    counter = Counter(content)
    words_count = dict_to_list_converter(counter.words_count)
    letters_count = counter.letters_count
    upper_letters_count = counter.upper_letters_count
    total_number_of_letters = counter.total_number_of_letters

    data_for_letters_csv = DataFormatterForLettersCSV(letters_count, total_number_of_letters, upper_letters_count)
    data_to_publish_in_letters_csv = data_for_letters_csv.formatted_data

    writer_csv = WriterCSV()
    writer_for_word_count = writer_csv.write_word_count_csv(words_count)
    writer_for_letters_count = writer_csv.write_letter_count_csv(data_to_publish_in_letters_csv)
