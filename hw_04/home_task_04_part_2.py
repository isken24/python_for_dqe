import re

ABSTRACT = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def text_normalization(text: str) -> str:
    delete_blank_lines_and_fix_grammar = text.replace('\n\n\n\n', '\n').replace('\n\n', '\n').replace(' iz', ' is')

    processed_text = []

    for index, row in enumerate(re.split('\n', delete_blank_lines_and_fix_grammar)):
        processed_text.append([])                       # For each line we use separate element of the list.
        punctuation_mark = '.'                      # row[-1] Punctuation mark to be added to each sentence (':' or '.')
        if index > 0 and not row.isspace():             # All sentence except first should be moved to the right.
            processed_text[index].append(' ')
        for sentence in re.split('\. ', row):           # Capitalizing sentences.
            sentence = sentence.strip(".: ")
            processed_text[index].append(f'{sentence.capitalize()}{punctuation_mark}')

    normalized_text = '\n'.join([(' '.join([elem for elem in row])) for row in processed_text])
    return normalized_text


def normalize_text(text:str) ->str:
    processed_text = []
    if text:
        for sentence in text.split('.'):
            processed_text.append(sentence.strip().capitalize())
        normalized_text = '. '.join(processed_text)
        return normalized_text


def create_sentence_from_last_words(converted_result: str) -> str:
    last_words = []
    for row in re.split('\n', converted_result):
        for sentence in re.split('\. ', row):
            last_words.append(sentence.strip('.: ').split(' ')[-1])
    sentence_from_last_words = ' '.join(last_words)
    return sentence_from_last_words


def count_number_of_spaces(text: str):
    space_counter = len(re.findall(r'\s', text))
    return space_counter


normalized_abstract = text_normalization(ABSTRACT)


if __name__ == '__main__':
    print(normalized_abstract)
    print(f'Sentence from last words_count: {create_sentence_from_last_words(normalized_abstract)}')
    print(f'Number of spaces in text: {count_number_of_spaces(normalized_abstract)}')
