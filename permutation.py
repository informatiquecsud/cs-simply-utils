
from random import choice


class PermutationCypher:

    def __init__(self, permutation):
        if len(permutation) == 26:
            self.permutation = permutation
        else:
            raise ValueError(
                "The key should be a permutation of the alphabet, i.e. a 26 character long string of unique characters")
        self._dict = self.get_dict()
        self._reversed_dict = self.get_reversed_dict()

    def get_dict(self):
        alphabet = PermutationCypher.alphabet()
        cypher_dict = {}

        for i, char in enumerate(alphabet):
            cypher_dict[alphabet[i]] = self.permutation[i]

        return cypher_dict

    def get_reversed_dict(self):
        reversed_dict = dict()
        for key, value in self._dict.items():
            if value not in reversed_dict:
                reversed_dict[value] = key
        return reversed_dict

    @staticmethod
    def alphabet():
        start_letter = ord('A')
        return ''.join([chr(start_letter + i) for i in range(26)])

    def use_dict(self, message, crypto_dict):
        encrypted = ''

        for c in message:
            encrypted += crypto_dict[c]

        return encrypted

    def encrypt(self, message):
        return self.use_dict(message, self._dict)

    def decrypt(self, crypto_text):
        return self.use_dict(crypto_text, self._reversed_dict)


if __name__ == "__main__":
    perm1 = PermutationCypher(permutation='ZEABCDYXWHIVUTGFJKRQLMSNPO')
    print(perm1.encrypt('GEHEDEINENWEGUNDLASSDIELEUTEREDEN'))
    print(perm1.encrypt('VATONCHEMINSANSTESOUCIERDUQUENDIRATON'))
    print(perm1.decrypt('BZTQCZVWYXWCKW'))
    print(perm1.encrypt('LAPATIENCEESTLACLEDELAJOIE'))
