# script that reverses the words in a sentence and formats the output correctly

import re

print('Type the message you want to decrypt: ')
sentence = input()

re.sub(' +', ' ', sentence)
sentence.strip()

words = sentence.split()

lastwd = words[-1]
clean_lastwd = ''.join(char for char in lastwd if char.isalpha())
del words[-1]
words.append(clean_lastwd)
words.reverse()

for item in words:
    if item is words[0]:
        cap = item.capitalize()
        del words[0]
        words.insert(0, cap)

    elif item is words[-1]:
        lower = item.lower()
        del words[-1]

        if lower.endswith('.') == False:
            lower = lower + '.'
        words.append(lower)

reverse_sentence = ' '.join(words)
print(reverse_sentence)
