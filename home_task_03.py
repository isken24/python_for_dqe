import re

abstract = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# First of all we will eliminate excessive blank lines and replace 'iz' with 'is' when needed.
abstract = abstract.replace('\n\n\n\n', '\n')
abstract = abstract.replace('\n\n', '\n')
abstract = abstract.lower().replace(' iz', ' is')

# Here we create 'result' variable to store resulting string. And 'sentence_from_last_words' to store sentence
# with last words of each existing sentence.
result = ''
sentence_from_last_words = []

# We will iterate through each line of the text and then divide each line into independent sentences.
# Text will be divided into lines by using '\n' separator. Lines will be divided into sentences by '\. ' separator.
# All spaces, dots and colons (' ', '.', ':') will be deleted from beginning and end of each sentence.
# In order to restore necessary punctuation marks at the end of sentences we create 'punctuation_mark' variable.
# To align text we will use f-string, and then replace double spaces between sentences with single space.
for row in re.split('\n', abstract):
    punctuation_mark = row[-1]
    for sentence in re.split('\. ', row):
        sentence = sentence.strip(':. ')
        sentence_from_last_words.append(sentence.split()[-1])
        result += f'  {sentence.capitalize()}{punctuation_mark}'
    result = result.replace('.  ', '. ').strip()
    result += '\n'



# In order to count number of spaces in the text we will iterate through each symbol in 'result'. If symbol is space,
# then 'space_counter' will be incremented by 1.
def count_number_of_spaces(result):
    space_counter = 0
    for i in result:
        if i.isspace():
            space_counter += 1
    print(f"Number of Spaces : {str(space_counter)}.")


if __name__ == '__main__':
    print(result)
    print("Sentence from last words:", *sentence_from_last_words)
    count_number_of_spaces(result)
