from random import shuffle

from utils import *


class PermutationCypher:

    def __init__(self, permutation):
        self.permutation = permutation
        self.permutation_dict = dict(zip(alphabet(), permutation))

    def encrypt(self, message):
        result = ''
        for c in message:
            if c in self.permutation_dict:
                result += self.permutation_dict[c]
            else:
                result += c
        return result

    def decrypt(self, crypto_text):
        result = ''
        reversed_dict = get_reversed_dict(self.permutation_dict)
        for c in crypto_text:
            result += reversed_dict[c]

        return result

    def permutation_as_str(self):
        return ''.join(self.permutation)


if __name__ == "__main__":
    # idem en Français
    message = 'MARCHEZVERSLENORDOUVERSLOUEST'
    message = 'MARCHEZVERSLENORDOUVERSLOUEST'
    freqs = frequency_analysis(message)
    show_dict_sorted(freqs)
    permutation = list(alphabet())
    shuffle(permutation)
    permutation = 'EIUHXDNCTRLWBMZAQPJYOFGSVK'
    perm_cypher = PermutationCypher(permutation)
    print(alphabet())
    print(perm_cypher.permutation_as_str())
    crypted = perm_cypher.encrypt(message)
    print(crypted)
    print(frequency_analysis(crypted))
    print(frequency_analysis(crypted, pattern_length=2))
    print(message)
    print(crypted)
    print(substitute(crypted, {
        'X': 'E',
        'P': 'R',
        'J': 'S',
        'Z': 'O',
        # 'F': 'V',
        # 'Z': 'U',
    }))

    '''
    indices à donner:

    Le O est codé par le Z
    Le R est chiffré par le P
    Le V est codé par F



    '''

    # Exercice 14
    message = '''
    l'etude des codes secrets est appelee cryptologie (du grec kryptos signifiant
    cache et logos signifiant la parole, l'etude, l'art). Les activites des
    personnes voulant communiquer de maniere privee et celles des cryptanalystes
    separent la cryptologie en deux domaines. La cryptographie (du grec kryptos,
    cache et graphein, ecrire) est la science du developpement des cryptosystemes et
    la cryptanalyse est l'etude de l'analyse des codes secrets et des
    cryptosystemes. Cette derniere est censee permettre de casser les cryptosystemes
    analyses.
    '''
    permutation = list(alphabet())
    shuffle(permutation)
    permutation = 'QUHWANXSDMTFKPLOJYZVCRIEGB'
    cypher = PermutationCypher(permutation)
    print("=== Permutation")
    print(alphabet())
    print(cypher.permutation_as_str())
    print("=== Analyse")
    message = message.upper()
    message = message.replace('\n', ' ').replace('    ', '')
    print(message)
    cyphered = cypher.encrypt(message)
    print(cyphered)
    print(substitute(cyphered, {
        'A': 'E',
        'Z': 'S',
        'V': 'T',
        'Y': 'R',
        'W': 'D',
        'H': 'C',
        'C': 'U',
        'L': 'O',
        'X': 'G',
        'Q': 'A',
        'G': 'Y',
        'O': 'P',
        'D': 'I',
        'T': 'K',
        'R': 'V',
        'P': 'N',
        'K': 'M',
        'J': 'Q',
        'N': 'F',
        'S': 'H',
        'E': 'X',
        '\'': '\'',
        '.': '.',
        '.': '.',
        ',': ',',
        ',': ',',
        ')': ')',
        '(': '(',
        ':': ':',
        '\n': '\n',
        ' ': ' ',
        'F': 'L',
    }))
    # show_dict_sorted(frequency_analysis(cyphered))
