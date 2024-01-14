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

    # Translate each character to Morse code
    morse_code_list = []
    for char in text:
        if char.isalpha():
            morse_code_list.append(morse_code_dict[char])

    # Join the Morse code list with spaces and words with forward slashes
    morse_code_result = " / ".join(morse_code_list)

    return morse_code_result

# Test cases
print(morse_translator("HELLO WORLD")) 
print(morse_translator("Python"))
print(morse_translator("Morse Code"))
