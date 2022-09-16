from random import shuffle

from utils import frequency_analysis, substitute, get_reversed_dict


class CaesarCypher:

    def __init__(self, shift):
        self.shift = shift
        self.shifted_alphabet = self.shift_alphabet(shift=self.shift)

    @staticmethod
    def shift_alphabet(shift=0):
        start_letter = ord('A')
        return ''.join([chr(start_letter + (i+shift) % 26) for i in range(26)])

    @staticmethod
    def shift_string(message, shift=0):
        shifted = ''
        for c in message:
            shifted += chr(ord('A') + (ord(c) - ord('A') + shift) % 26)

        return shifted

    def encrypt(self, message):
        return CaesarCypher.shift_string(message, self.shift)

    def decrypt(self, cypher_text):
        return CaesarCypher.shift_string(cypher_text, shift=-self.shift)


if __name__ == '__main__':
    caesar0 = CaesarCypher(shift=0)
    caesar5 = CaesarCypher(shift=5)
    print(caesar5.shifted_alphabet)
    print(caesar5.encrypt('SALUT'))
    print(caesar5.decrypt('XFQZY'))
    print(caesar5.encrypt('QUESEPASSERAITILSILEDECALAGEETAITDEVINGTSIX'))
    caesar2 = CaesarCypher(shift=2)
    print(caesar2.decrypt('FCVGPUKEJGTJGKVYKTFKOOGTYKEJVKIGT'))
    print(caesar2.decrypt('LASECURITEDESDONNEESDEVIENTDEPLUSENPLUSIMPORTANTE'))
    print(caesar2.decrypt('XGTYGPFGUEJNWGUUGNBYGK'))
    message = "SERVEZVOUSDELACLEDEUX"
    print(caesar2.decrypt(message))
    print(frequency_analysis(message))
    print(frequency_analysis('JCPLCXSTCPQRCFCL'))
    print(CaesarCypher(shift=-2).decrypt('JCPLCXSTCPQRCFCL'))
    print(CaesarCypher(shift=-2).encrypt('APPRENEZACOMPRENDRE'))
    print(frequency_analysis('YNNPCLCXYAMKNPCLBPC'))
    # page 34
    print(frequency_analysis('SJSSJSJZSSFRJS'))
    print(CaesarCypher(shift=(ord('J')-ord('E'))).decrypt('SJSSJSJZSSFRJS'))
    print(frequency_analysis('DEUXDIDONSSEDANDINENT'))
    print(CaesarCypher(shift=23).encrypt('DEUXDIDONSSEDANDINENT'))
    print('ananas', frequency_analysis('LESANANASCESTLACLASSE'))
    print(CaesarCypher(shift=23).encrypt('LESANANASCESTLACLASSE'))
    print(CaesarCypher(shift=23).decrypt('IBPXKXKXPZBPQIXZIXPPB'))
    freqs = frequency_analysis('''
    RLJ AJHFJ RJF OJHJLETGHFLKNJM MJMMN EVM XFPUNDADOLJ (SDE OFLJGHLTGHJM
XFPUNDT, SJFQDFOJM, YMR ADODT, WDFN, AJHFJ, XYMRJ). RLJ VXNLSLNVJNJM RJF XDEEYMLBLJFJMRJM YMR XFPUNDVMVAPNLXJF NJLAJM RLJ XFPUNDADOLJ LM BWJL
OJQLJNJ JLM. RLJ XFPUNDOFVUHLJ (VYGH: XFPUNDOFVKLJ, SDE OFLJGHLTGHJM XFPUNDT, SJFQDFOJM, YMR OFVUHJLM, TGHFJLQJM) LTN RLJ WLTTJMTGHVKN RJF JMNWLGXAYMO SDM XFPUNDTPTNJEJM, YMR RLJ XFPUNDVMVAPTJ LTN RLJ AJHFJ RJF VMVAPTJ SDM
OJHJLENJCNJM YMR XFPUNDTPTNJEJM, RLJ BYE XMVGXJM RJF VMVAPTLJFNJM
XFPUNDPTNJEJ KYJHFJM TDAA
    '''.replace(' ', ''))
    print(freqs)
    for letter, freq in freqs.items():
        pass

    message = 'UBXBAGCXAZYHBAZHBYAGCXDBEFBA'
    print(frequency_analysis(message))
    print(frequency_analysis(message, pattern_length=2))
    print(message)
    message = substitute(message, get_reversed_dict({
        'H': 'X',
        'O': 'Z',
        'E': 'B',
        'N': 'A',
        # 'F': 'H',
        'A': 'G',
        'C': 'C',
        # 'Z': 'Z',
        # 'Y': 'Y',
        # 'L': 'L',
        # 'C': 'S',
        # 'E': 'E',
        'G': 'U',
        'R': 'Y',
        'D': 'H',
        'W': 'D',
        'S': 'E',
        'T': 'F',
    }))
    print(message)

    message = 'ELIERAMASSEMESFLEURS'
    print(message, "=>", CaesarCypher(-2).encrypt(message))
    message = 'CENESTPASMATASSEDETHE'
    print(message, "=>", CaesarCypher(23).encrypt(message))

    caesar1 = CaesarCypher(shift=1)
    print(caesar1.encrypt('NULNAPPRENDSANSFAIREDESERREURS'))

    message = 'OVMOBQQSFOETBOTGBJSFEFTFSSFVST'
    partial = substitute(message, get_reversed_dict({
        'N': 'O', 'P': 'Q', 'E': 'F', 'R': 'S', 'U': 'V', 'S': 'T',
    }))
    partial = partial.replace('_', '-')
    print(partial)
    print(CaesarCypher(3).encrypt('LENNEMIQUIDECOUVREVOSERREURS'))
    print(CaesarCypher(7).encrypt('ESTPOURVOUSPLUSUTILEQUUNAMI'))
    print(CaesarCypher(20).encrypt('QUIVOUSLESCACHELEONARDDEVINCI'))
    print(CaesarCypher(2).encrypt('SEULSLESCOURAGEUXGAGNENT'))

    print(CaesarCypher(22).encrypt('CITELESNOMSDENEUFCAMARADESDECLASSE'))
    print(CaesarCypher(22).encrypt('SEA'))

    print(frequency_analysis('TOUTLEMONDEDEVRAITSAVOIRLIREETECRIRE', 2))

    for key in range(1, 26):
        print("key", key)
        print(CaesarCypher(key).decrypt(
            'GUUCAGGPEQTGGEJQWGFGPQWXGCWGEJQWGOKGWZ'))

    print(frequency_analysis('VASSURTONCHEMINCARCELUICINEXISTEQUEPARTESPAS '))

    print(substitute('VASSURTONCHEMINCARCELUICINEXISTEQUEPARTESPAS', {
        'B': 'C',
        'C': 'B',
        'K': 'L',
        'L': 'K',
        'T': 'U',
        'U': 'T',
    }))

    print(frequency_analysis('TOUSLESCHEMINSMENENTAROME'))
    print(CaesarCypher(3).decrypt('WRXVOHVFKHPLQVPHQHQWDURPH'))

    print('Lösungen finden 5/6, exercice 2.9')
    print(CaesarCypher(1).encrypt('CENESTPASPARCEQUUNPROBLEME'))
    print(CaesarCypher(3).encrypt('NAPASETERESOLUQUILEST'))
    print(CaesarCypher(6).encrypt('IMPOSSIBLEARESOUDRE'))
    print(CaesarCypher(6).decrypt('OSVUYYOHRKGXKYUAJXK'))

    print("Exercice 2.10")
    print(CaesarCypher(ord('O') - ord('S')
                       ).decrypt('YEPAHAOJKIOZAJAQBYWIWNWZAOZAYHWOOA'))

    print("Enigme page 26")
    print(CaesarCypher(7).decrypt('AVBASLTVUKLKLCYHPAZHCVPYSPYLLALJYPYL'))

    print(CaesarCypher(16).encrypt('PLUSONDESIREUNECHOSEPLUSELLESEFAITATTENDRE'))
    print(CaesarCypher(3).encrypt('TOUSLESCHEMINSMENENTAROME'))
    print(CaesarCypher(3).encrypt('CESARETAITMALIN'))
    print(CaesarCypher(4).encrypt(
        'ILVAUTMIEUXSEDISPUTERAVECQUELQUUNDINTELLIGENTQUEPARLERAUNIMBECILE'))
    print(frequency_analysis(
        'ILVAUTMIEUXSEDISPUTERAVECQUELQUUNDINTELLIGENTQUEPARLERAUNIMBECILE'))
    print(CaesarCypher(2).encrypt('SEULSLESCOURAGEUXGAGNENT'))
    print(CaesarCypher(3).encrypt('CESARETAITMALIN'))  # => FHVDUHWDLWPDOLQ
    print(CaesarCypher(3).encrypt('LENNEMIQUIDECOUVREVOSERREURS'))  # =>
    print(CaesarCypher(7).encrypt('ESTPOURVOUSPLUSUTILEQUUNAMI'))  # =>
    print(CaesarCypher(20).encrypt('QUIVOUSLESCACHELEONARDDEVINCI'))  # =>
    print(CaesarCypher(2).decrypt('UGWNUNGUEQWTCIGWZICIPGPV'))  # =>
    print(CaesarCypher(1).decrypt('DFOFTUQBTQBSDFRVVOQSPCMFNF'))  # =>
    print(CaesarCypher(3).decrypt('QDSDVHWHUHVROXTXLOHVW'))  # =>
    print(CaesarCypher(6).decrypt('OSVUYYOHRKGXKYUAJXK'))  # =>
    print(CaesarCypher(22).decrypt('YEPAHAOJKIOZAJAQBYWIWNWZAOZAYHWOOA'))  # =>
