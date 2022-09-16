from utils import *
from caesar import *





def sanitize(text):
    return text.upper().replace(' ', '').replace('.', '').replace(',', '')

print(frequency_analysis('TOUTLEMONDEDEVRAITSAVOIRLIREETECRIRE', 1))
text = sanitize('Essaye encore. Echoue de nouveau Echoue mieux')
print(text)
print(frequency_analysis(text, 1))

text = 'Les bonnes choses arrivent à ceux qui travaillent fort'
text = 'Les bonnes choses arrivent a ceux qui travaillent fort'
text = 'Quoi que tu fasses, faisle avec toutes tes forces'
text = 'Prends le risque ou perds ta chance'
text = 'Le passe ne correspond pas a l’avenir'
text = 'Oublie le style pense aux resultats'
text = 'Ta vitesse importe peu tant que tu n’arretes pas'
text = 'Vas sur ton chemin, car celuici nexiste que par tes pas'
text = sanitize(text)
print(text)
freqs = frequency_analysis(text)
print(
    sorted(
        freqs.items(), key=lambda x: x[1], reverse=True
    )
)
print(len(text))