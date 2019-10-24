import unittest

from polybius import PolybiusCypher, square_de, square_fr


class FrenchTestCase(unittest.TestCase):
    def setUp(self):
        self.cypher = PolybiusCypher(square_fr)

    def test_dict_is_correct(self):
        correct_dict = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
                        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'}

        self.assertDictEqual(self.cypher.get_dict(), correct_dict)

    def test_reversed_dict_is_correct(self):
        correct_reversed_dict =
        self.assertDictEqual(
            self.cypher.get_reversed_dict(), correct_reversed_dict)

    def test_encrypt_SECRET(self):
        message = 'SECRET'
        correct_cypher = '431513421544'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_encrypt_BIDULE(self):
        message = 'BIDULE'
        correct_cypher = '122414453115'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_encrypt_JOYEUX(self):
        message = 'JOYEUX'
        correct_cypher = '243454154553'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_encrypt_LAMESOPOTAMIEFUTLEBERCEAUDELECRITURE(self):
        message = 'LAMESOPOTAMIEFUTLEBERCEAUDELECRITURE'
        correct_cypher = '311132154334353444113224152145443115121542131511451415311513422444454215'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_empty_message(self):
        message = ''
        correct_cypher = ''
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_double_letters(self):
        message = 'I'
        correct_cypher = '24'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

        message = 'J'
        correct_cypher = '24'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_decrypt_SECRET(self):
        message = 'SECRET'
        cypher = '431513421544'
        self.assertEqual(self.cypher.decrypt(cypher), message)

    def test_decrypt_BIDULE(self):
        message = 'BIDULE'
        cypher = '122414453115'
        self.assertEqual(self.cypher.decrypt(cypher), message)

    def test_decrypt_JOYEUX_to_IOYEUX(self):
        message = 'IOYEUX'
        cypher = '243454154553'
        self.assertEqual(self.cypher.decrypt(cypher), message)

    def test_empty_message(self):
        message = ''
        cypher = ''
        self.assertEqual(self.cypher.decrypt(cypher), message)

    def test_decrypt_24_not_J_but_I(self):
        message = 'I'
        cypher = '24'
        self.assertEqual(self.cypher.decrypt(cypher), message)

    def test_decrypt_24_I(self):
        message = 'I'
        cypher = '24'
        self.assertEqual(self.cypher.decrypt(cypher), message)


class GermanTestCase(unittest.TestCase):
    def setUp(self):
        self.cypher = PolybiusCypher(square_de)

    def test_dict_is_correct(self):
        correct_dict = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
                        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'}

        self.assertDictEqual(self.cypher.get_dict(), correct_dict)

    def test_reversed_dict_is_correct(self):
        correct_reversed_dict = {'11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', '21': 'F', '22': 'G', '23': 'H', '24': 'I', '25': 'K', '31': 'L',
                                 '32': 'M', '33': 'N', '34': 'O', '35': 'P', '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U', '51': 'V', '52': 'W', '53': 'X', '54': 'Y', '55': 'Z'}
        self.assertDictEqual(
            self.cypher.get_reversed_dict(), correct_reversed_dict)

    def test_encrypt_GEHEIM(self):
        message = 'GEHEIM'
        correct_cypher = '221523152432'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_empty_message(self):
        message = ''
        correct_cypher = ''
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_double_letters_IJ(self):
        message = 'I'
        correct_cypher = '24'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

        message = 'J'
        correct_cypher = '24'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_double_letters_UV(self):
        message = 'U'
        correct_cypher = '45'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

        message = 'V'
        correct_cypher = '45'
        self.assertEqual(self.cypher.encrypt(message), correct_cypher)

    def test_decrypt_GEHEIM(self):
        message = 'GEHEIM'
        cypher = '221523152432'
        self.assertEqual(self.cypher.decrypt(cypher), message)
