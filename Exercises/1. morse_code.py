def morse_translator(text):
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    text = text.upper()

    morse_translated = []
    for word in text.split():
        morse_word = ' '.join(morse_code_dict[char] for char in word if char in morse_code_dict)
        morse_translated.append(morse_word)

    return ' / '.join(morse_translated)

test1 = morse_translator("HELLO WORLD")
test2 = morse_translator("Python")
test3 = morse_translator("Morse Code")

print(test1)
print(test2)
print(test3)
