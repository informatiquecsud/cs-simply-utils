from permutation import *
from utils import *

perm = PermutationCypher('ACBDEFGHIJLKMNOPQRSUTVWXYZ')
print(perm.encrypt('VASSURTONCHEMINCARCELUICINEXISTEQUEPARTESPAS'))

message = to_message("Les ordinateurs ne font qu'obéir à nos ordres")
print(message)
print(
    ''.join(
        [''.join(list(reversed(block))) for block in chunk(message, 6)]
    )
)

message = 'participe au castor informatique'
message = to_message(message)
print(
     ''.join(
        [''.join(list(reversed(block))) for block in chunk(message, 6)]
    )
)

message = "La jeunesse a un joli visage mais l'âge a une belle âme."
message = to_message(message) + 'XYZAB'
print((message))

