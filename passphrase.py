def first_letter(word):
    return word[0]
def last_letter(word):
    return word[-1]
def first_letter_and_length(word):
    return first_letter(word) + str(len(word))
def last_letter_and_length(word):
    return last_letter(word) + str(len(word))

def passphrase(phrase, func=None):
    func = func or first_letter
    words = phrase.split()
    return ''.join([func(word) for word in words])

def test():
    phrase = "Roger Federer est un modèle pour beaucoup de jeunes"
    print(passphrase(phrase))
    print(passphrase(phrase, func=first_letter_and_length))
    
test()