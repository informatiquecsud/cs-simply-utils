from utils import alphabet, shift_char


class VigenereCypher:

    def __init__(self, key):
        self.key = [0] * len(key)

        alpha = alphabet()
        for i, el in enumerate(key):
            if isinstance(el, int):
                self.key[i] = el
            elif isinstance(el, str):
                if el in '0123456789':
                    self.key[i] = int(el)
                elif el == '_':
                    self.key[i] = el
                elif el in alpha:
                    self.key[i] = ord(el.upper()) - ord('A')

        # try:
        #     int(key)
        #     self.key = [int(c) for c in key]
        # except:
        #     self.key = [ord(c) - ord('A') for c in key]

    def encrypt(self, message, key=None):
        key = key or self.key
        N = len(key)
        result = [''] * len(message)

        for i, char in enumerate(message):
            result[i] = shift_char(char, key[i % N]) if key[i %
                                                            N] != '_' else key[i % N]

        return ''.join(result)

    def decrypt(self, crypted):
        return self.encrypt(crypted, key=[-k if isinstance(k, int) else k for k in self.key])


if __name__ == "__main__":
    c = VigenereCypher(key='BC')
    assert c.key == [1, 2]
    c = VigenereCypher(key='26')
    assert c.key == [2, 6]

    crypted = c.encrypt('LINFORMATIQUESIMPLEMENT')
    print(crypted)
    print(c.decrypt('NOPLQXOGVOSAGYKSRRGSGTV'))

    crypted = 'OGOPFFJGDNFXFTTVFPHGIGJOTEITJHUGOFFTHGTEIKDJUG'
    # for i in range(1, 26):
    for i in [1]:
        for j in range(1, 26):
            c = VigenereCypher(key=[i, j])
            print(c.decrypt(crypted))
            print(i, j)

    message = 'NOMMEZLESCODESSECRETSLESPLUSCELEBRESDELHISTOIRE'
    c = VigenereCypher(key=[1, 2])
    print(c.encrypt(message))
