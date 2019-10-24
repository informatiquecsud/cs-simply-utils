from swap import *
from caesar import *

swap = SwapCypher()
caesar5 = CaesarCypher(shift=5)

# A
crypted = 'SNTKRWYFPN'
message = caesar5.decrypt(swap.decrypt(crypted))
print(message)
print(crypted)

# B
message = 'INFORMATIQUE'
crypted = caesar5.encrypt(swap.encrypt(message))
print(message)
print(crypted)
