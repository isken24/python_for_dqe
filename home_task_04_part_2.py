import re

abstract = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

text_without_empty_lines = ''
text_without_wrong_words = ''
sentence_from_last_words = ''
converted_result = ''
result = []


def remove_empty_lines(text: str) -> str:
    global text_without_empty_lines
    text_without_empty_lines = text.replace('\n\n\n\n', '\n').replace('\n\n', '\n')
    return text_without_empty_lines


def replace_wrong_words(text: str, wrong_word, proper_word) -> str:
    global text_without_wrong_words
    text_without_wrong_words = text.lower().replace(wrong_word, proper_word)
    return text_without_wrong_words


def capitalize_sentences_in_text(text: str) -> list:
    global result
    for index, row in enumerate(re.split('\n', text)):
        result.append([])                       # For each line we use separate element of the list.
        punctuation_mark = row[-1]              # Punctuation mark to be added to each sentence (':' or '.')
        if index > 0 and not row.isspace():     # All sentence except first should be moved to the right.
            result[index].append(' ')
        for sentence in re.split('\. ', row):   # Capitalizing sentences.
            sentence = sentence.strip(".: ")
            result[index].append(f'{sentence.capitalize()}{punctuation_mark}')
    return result


def create_sentence_from_last_words(text: list) -> str:
    global sentence_from_last_words
    last_words = []
    for row in text:
        for sentence in row:
            last_words.append(sentence.strip('.: ').split(' ')[-1])
    sentence_from_last_words = ' '.join(last_words)
    return sentence_from_last_words


def convert_result_to_string(text: list) -> str:
    global converted_result
    converted_result = '\n'.join([(' '.join([elem for elem in row])) for row in text])
    return converted_result


def count_number_of_spaces(text: str):
    space_counter = len(re.findall(r'\s', text))
    return space_counter


if __name__ == '__main__':
    remove_empty_lines(abstract)
    replace_wrong_words(text_without_empty_lines, ' iz', ' is')
    capitalize_sentences_in_text(text_without_wrong_words)
    create_sentence_from_last_words(result)
    convert_result_to_string(result)
    print(converted_result)
    print(f'Number of spaces in text: {count_number_of_spaces(converted_result)}')
    print(f'Sentence from last words: {sentence_from_last_words}')
