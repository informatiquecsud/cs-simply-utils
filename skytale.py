
from random import choice


class SkytaleCypher:

    def __init__(self, diameter):
        self.diameter = diameter

    @staticmethod
    def alphabet():
        start_letter = ord('A')
        return ''.join([chr(start_letter + i) for i in range(26)])

    def encrypt(self, message):
        encrpyted = ''
        alphabet = SkytaleCypher.alphabet()

        # compute number of columns
        nb_cols = int((len(message) - 0.0001) // self.diameter + 1)

        # add random letters to message to make it self.diameter * nb_cols long
        nb_chars_to_add = nb_cols * self.diameter - len(message)
        added_chars = ''.join([choice(alphabet)
                               for _ in range(nb_chars_to_add)])
        message += added_chars

        # read in column order
        for i in range(nb_cols):
            for j in range(0, len(message), nb_cols):
                encrpyted += message[i + j]

        return encrpyted

    def decrypt(self, crypto_text):
        message = ''
        nb_cols = len(crypto_text) // self.diameter

        for i in range(self.diameter):
            for j in range(0, len(crypto_text), self.diameter):
                message += crypto_text[i + j]

        return message


if __name__ == "__main__":
    skytale10 = SkytaleCypher(diameter=10)
    print(skytale10.encrypt('WIRGREIFENUMDREIVONWESTENANSCHLEICHENZUFUSSAN'))
    print(skytale10.decrypt('WEUIEALEUMIIMVSNENSLRFDOTSIZSWGERNECCUABRNEWNHHFNW'))
    print(skytale10.encrypt('ATROISHEURESNOUSATTAQUONSPARSURPRISEDEPUISLOUEST'))
    print(skytale10.decrypt('ASESQPREIETHSAUAPDSSRENTORRELTOUOTNSIPOSIRUASUSUUA'))
    skytale3 = SkytaleCypher(diameter=3)
    print(skytale3.decrypt('SWSPACARHREITNEASDUELNHIDRCAUHTNUHTVEEXNRY'))
    print(skytale3.encrypt('SPARTEETATHENESETAIENTTRESDIFFERENTES'))
