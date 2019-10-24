
from utils import *


class MaskAndShiftCypher:

    def __init__(self, mask, shift):
        self.mask = mask
        self.shift = shift

    def encrypt(self, message):
        result = [''] * len(message)
        N = len(self.mask)

        for i, char in enumerate(message):
            if self.mask[i % N] == '0':
                result[i] = char
            else:
                result[i] = shift_char(char, self.shift)

        return ''.join(result)

    def decrypt(self, crypted):
        c = MaskAndShiftCypher(mask=self.mask, shift=-self.shift)
        return c.encrypt(crypted)


if __name__ == "__main__":
    c = MaskAndShiftCypher(mask='011010', shift=4)
    print(c.encrypt('APFELAPFELAPFELWURMAPFEL'))
    print(c.encrypt('POMMEPOMMEPOMMEVERSPOMME'))
    print(c.decrypt(c.encrypt('POMMEPOMMEPOMMEVERSPOMME')))
