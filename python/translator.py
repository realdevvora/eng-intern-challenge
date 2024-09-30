import sys

text_to_braille_dict = {
    # Letters
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",

    # Numbers
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    
    "capital": ".....O",
    "number": ".O.OOO",
    " ": "......"
}

braille_to_text_numbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",

    ".....O": "capital",
    ".O.OOO": "number",
    "......": " "
}

braille_to_text_indicators = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",

    ".....O": "capital",
    ".O.OOO": "number",
    "......": " "
}

def text_to_braille(text):
    output = []

    number = False
    for letter in text:
        # invalid character
        if letter.upper() not in text_to_braille_dict:
            return ""
        # uppercase character
        if letter.isupper():
            output.append(text_to_braille_dict["capital"])
            output.append(text_to_braille_dict[letter.upper()])
            letter = letter.lower()
        # number
        elif letter.isdigit():
            if not number:
                output.append(text_to_braille_dict["number"])
            output.append(text_to_braille_dict[letter.upper()])
            number = True

        # space
        elif letter == " ":
            output.append(text_to_braille_dict[" "])
            number = False
        else:
            output.append(text_to_braille_dict[letter.upper()])

    return "".join(output)

def braille_to_text(braille):
    output = []
    number = False
    capital = False
    for i in range(0, len(braille), 6):
        letter = braille[i:i+6]

        # space
        if braille_to_text_indicators[letter] == " ":
            output.append(" ")
            number = False

        # applying capital letter
        elif capital:
            output.append(braille_to_text_indicators[letter].upper())
            capital = False

        # reading number
        elif number:
            output.append(braille_to_text_numbers[letter])

        # checking capital letter
        elif braille_to_text_indicators[letter] == "capital":
            capital = True

        # checking number
        elif braille_to_text_indicators[letter] == "number":
            number = True
            
        # printing regular lowercase letter
        else:
            output.append(braille_to_text_indicators[letter].lower())

    return "".join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text1> <text2> ...")
        return

    output = []
    args = " ".join(sys.argv[1:])
    if "." in args:
        output.append(braille_to_text(args))
    else:
        output.append(text_to_braille(args))

    print("".join(output), end="")

if __name__ == "__main__":
    main()