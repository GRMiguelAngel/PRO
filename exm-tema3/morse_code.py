# ************
# CÓDIGO MORSE
# ************
from pathlib import Path


def run(morse_signals: Path, sentence: str) -> str:
    morse_sentence = ''
    morse_traslate = {}
    with open(morse_signals, 'r') as morse_file:
        for morse_chars in morse_file:
            morse_chars = morse_chars.rstrip().split(' ')
            morse_traslate[morse_chars[0]] = morse_chars[1]
        sentence_splitted = sentence.split(' ')
        for word in sentence_splitted:
            for letter in word:
                if letter.isalnum():
                    morse_sentence += f'{morse_traslate[letter.upper()]} '
        morse_sentence = morse_sentence.rstrip()

    return morse_sentence


if __name__ == '__main__':
    run('data/morse_code/signals.morse', 'hello, world!')
