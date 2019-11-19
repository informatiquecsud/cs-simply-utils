class PolybiusCypher:

    def __init__(self, square):

        self._square = square
        self._dict = self.get_dict()
        self._reversed_dict = self.get_reversed_dict()

    def get_dict(self):
        polybius_dict = dict()

        for (i, row) in enumerate(self._square):
            for (j, letters) in enumerate(row):
                for letter in letters.split('/'):
                    polybius_dict[letter] = str(i+1) + str(j+1)

        return polybius_dict

    def show_dict(self):
        print(self._dict)

    def show_square(self):
        square_string = '  | 1 2 3 4 5\n' + '=' * 13 + '\n'
        for i, line in enumerate(self._square):
            square_string += str(i+1) + "| "
            for letter in line:
                square_string += letter + " "
            square_string += '\n'
        return square_string

    def encrypt(self, message):
        return ''.join([self._dict[c] for c in message])

    def decrypt(self, cypher_text):
        message_chars = []
        for i in range(0, len(cypher_text), 2):
            key = cypher_text[i:i+2]
            message_chars += [self._reversed_dict[key]]
        return ''.join(message_chars)

    def get_reversed_dict(self):
        reversed_dict = dict()
        for key, value in self._dict.items():
            if value not in reversed_dict:
                reversed_dict[value] = key
        return reversed_dict


square_de = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I/J', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U/V'],
    ['W', 'X', 'Y', 'Z'],
]

square_fr = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I/J', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z'],
]


def get_reverse_square(square):
    reversed_square = []
    for line in reversed(square):
        reversed_square += [list(reversed(line))]

    return reversed_square


if __name__ == '__main__':

    cypher_de = PolybiusCypher(square_de)
    cypher_fr = PolybiusCypher(square_fr)

    print(cypher_de.get_reversed_dict())

    for message in [
        'GEHEIM'
    ]:
        print(message, "=>", cypher_de.encrypt(message))

    square_french_reversed = get_reverse_square(square_fr)
    cypher_fr_reversed = PolybiusCypher(square_french_reversed)
    print('exo 2', cypher_fr_reversed.encrypt('LECOURSCOMMENCEAHUITHEURES'))


message = 'WEUIEALEUXIIMVSNENSKY'
for i in range(26):
    print(''.join(chr((ord(c) - ord('A') + i) % 26 + ord('A'))
                  for c in message))

print(PolybiusCypher(square_fr).encrypt('POLYBE'))
print(PolybiusCypher(square_fr).decrypt(
    '311132154334353444113224152145443115121542131511451415311513422444454215'))
