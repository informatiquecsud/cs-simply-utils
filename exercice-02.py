
from caesar import *

from utils import alphabet

crypted = 'LINFORMATIQUESIMPLEMENT'
odd_letters = crypted[0::2]
even_letters = crypted[1::2]

c2 = CaesarCypher(shift=2)
odds = c2.encrypt(odd_letters)
print(odd_letters)
print(odds)

c6 = CaesarCypher(shift=6)
evens = c6.encrypt(even_letters)
print(even_letters)
print(evens)

zipped = zip(odds, evens)
print(list(zipped))
print(crypted)
print(''.join([x + y for x, y in list(zipped)]))

for (i, letter) in enumerate(alphabet()):
    print(i+1, letter)


c = CaesarCypher(shift=4)
print(c.encrypt('OMEMMPMEEPOM'))
