
class SwapCypher:

    def encrypt(self, message):
        encrypted = [0] * len(message)
        for i in range(0, len(message), 2):
            if i+1 < len(encrypted):
                encrypted[i], encrypted[i+1] = message[i+1], message[i]
            else:
                encrypted[i] = message[i]

        return ''.join(encrypted)

    def decrypt(self, crypto_text):
        return self.encrypt(crypto_text)


if __name__ == "__main__":
    cypher = SwapCypher()
    crypted = cypher.encrypt('CETTEIDEEESTVIELLEDETROISMILLEANS')
    print(crypted)
    print(cypher.decrypt(crypted))
