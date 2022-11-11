from hw_07.home_task_07 import *

def main():
    content = file_reader('hw_06/result.txt')
    counter = Counter(content)
    counter.write_words_count_csv()
    counter.write_letter_count_csv()

if __name__ == "__main__":
    main()
