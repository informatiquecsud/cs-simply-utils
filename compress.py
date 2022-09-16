
def compress2(text):
    compressed = ''
    already_seen_words = {}

    current_word = ''
    current_position = 1

    for c in text + "\n":
        # Cédric Donner, removed the '-' symbol as word separator ... generates
        # too much ambiguities

        # if c in ['\r', '\n', ' ', ',', '.', '!', '?', '-']:
        if c in ['\r', '\n', ' ', ',', '.', '!', '?']:
            if current_word in already_seen_words:
                compressed += '#' + str(already_seen_words[current_word])
            else:
                if len(current_word) > 2:
                    already_seen_words[current_word] = current_position
                compressed += current_word
            if len(current_word) > 0:
                current_position += 1
            current_word = ''
            compressed += c

        elif current_word in already_seen_words:
            compressed += '#' + str(already_seen_words[current_word])
            current_word = c

        else:
            current_word += c
        #print(current_word, already_seen_words)

    return compressed


def compress(text):
    compressed = ''
    already_seen_words = {}

    current_word = ''
    current_position = 1

    for c in text + "\n":
        if c in ['\r', '\n', ' ', ',', '.', '!', '?', '-']:
            if current_word in already_seen_words:
                compressed += '#' + str(already_seen_words[current_word])
            else:
                if len(current_word) > 2:
                    already_seen_words[current_word] = current_position
                compressed += current_word
            if len(current_word) > 0:
                current_position += 1
            current_word = ''
            compressed += c

        else:
            current_word += c
        #print(current_word, already_seen_words)

    return compressed


text = '''
LA MÈRE DE TA MÈRE EST TA GRAND-MÈRE. 
TA MÈRE VA DEVENIR LA GRAND-MÈRE DE TES ENFANTS.
'''


text2 = '''
DANS LA FORÊT LOINTAINE, ON ENTEND LE COUCOU 
DU HAUT DE SON GRAND CHÊNE, IL RÉPOND AU HIBOU 
COUCOU, COUCOU 
ON ENTEND LE COUCOU 
COUCOU, COUCOU 
ON ENTEND LE COUCOU 
DANS LA FORÊT LOINTAINE, ON ENTEND LE COUCOU 
DU HAUT DE SON GRAND CHÊNE, IL RÉPOND AU HIBOU 
'''

text = '''
BONJOUR MADAME SANS SOUCI!
COMBIEN SONT CES SIX SAUCISSONS-CI?
CES SIX SAUCISSONS-CI SONT SIX SOUS.
SI CES SIX SAUCISSONS-CI SONT SIX SOUS,
CES SIX SAUCISSONS-CI SONT TROP CHERS!
'''
text = '''
LA MÈRE DE TA MÈRE EST TA GRAND-MÈRE. LA MÈRE DE TA GRAND-MÈRE EST TON
ARRIÈRE-GRAND-MÈRE.
'''

text = '''
J’AI ACHETÉ UN ORDINATEUR TRÈS RAPIDE QUI EST RAPIDEMENT DEVENU OBSOLÈTE. J’ACHÈTE DONC PLUTÔT DES ORDINATEURS D’OCCASION.
'''
text = '''
SI SIX SCIES SCIENT SIX CYPRÈS, SIX CENT SIX SCIES SCIENT SIX CENT SIX CYPRÈS.
'''
text = '''
CET ORDINATEUR TRÈS CHER ET TRÈS RAPIDE EST RAPIDEMENT DEVENU TRÈS LENT. JE ME SUIS DONC LENTEMENT MIS À ACHETER DES ORDINATEURS D’OCCASION.
'''

text = '''
VOS ENFANTS NE SONT PAS VOS ENFANTS.
ILS SONT LES ENFANTS DE L’ASPIRATION DE LA VIE À ELLE-MÊME.
ILS VIENNENT PAR VOUS, MAIS PAS DE VOUS,
ET BIEN QU’ILS SOIENT AVEC VOUS, ILS NE SONT PAS À VOUS.
VOUS POUVEZ LEUR DONNER VOTRE AMOUR, MAIS PAS VOS PENSÉES,
CAR ILS ONT LEURS PROPRES PENSÉES.
LEUR ÂME VIT DANS LA MAISON DE DEMAIN,
QUE VOUS NE POUVEZ PAS VISITER, MÊME DANS VOS RÊVES.
VOUS POUVEZ ESSAYER D’ÊTRE COMME EUX,
MAIS N’ESSAYEZ PAS DE FAIRE EN SORTE QU’ILS SOIENT COMME VOUS.
'''

compressed = compress2(text.strip())


#def len(x): return x


print(len(text.replace(' ', '')))
print(len(compressed.replace(' ', '')))
print(len(text))
print(len(compressed))
print(compressed)
