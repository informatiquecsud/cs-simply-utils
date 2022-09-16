from random import choice

def shift_char(char, shift):
    return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))


def patterns(message, pattern_length=1):
    found_patterns = []
    for i in range(len(message)):
        try:
            p = message[i:i+pattern_length]
            # print('found pattern', p, 'at index', i)
            found_patterns += [p]
        except:
            break

    return found_patterns


def frequency_analysis(message, pattern_length=1):
    dico = {}
    for pattern in patterns(message, pattern_length):
        if pattern in dico:
            dico[pattern] += 1
        else:
            dico[pattern] = 1
    return dico


def substitute(message, substitutions):
    result = ''
    for c in message:
        if c in substitutions:
            result += substitutions[c]
        else:
            result += '_'

    return result


def get_reversed_dict(_dict):
    reversed_dict = dict()
    for key, value in _dict.items():
        if value not in reversed_dict:
            reversed_dict[value] = key
    return reversed_dict


def alphabet():
    start_letter = ord('A')
    return ''.join([chr(start_letter + i) for i in range(26)])


def show_dict_sorted(_dict):
    for key, values in sorted(_dict.items(), key=lambda x: x[1], reverse=True):
        print(key, values)


def test_frequency_analysis():
    messages = '''
    APPRENEZACOMPRENDRE
    ELIERAMASSEMESFLEURS
    CENESTPASMATASSEDETHE
    '''

    for m in [x.strip() for x in messages.split('\n')]:
        print(m)
        show_dict_sorted(frequency_analysis(m))
        print("========")
        
def chunk(message, block_len):
    blocks = []
    
    for (i, char) in enumerate(message):
        if i % 6 == 0:
            current_block = ''
        current_block += char
        if i % 6 == 5 or i == len(message) - 1:
            blocks.append(current_block)
            
    # complete last block with random chars
    if len(blocks[-1]) < block_len:
        additional_chars = ''.join([choice(message) for _ in range(block_len - len(blocks[-1]))])
        blocks[-1] = blocks[-1] + additional_chars
        
    return blocks

def replace_many(message, substitutions=None):
    DEFAULT_SUBSTITUTIONS = {' ': '', ',': '', '.': '', ';': '', ':':'', 'é': 'e', 'è': 'e', 'à': 'a', 'ê':'e', 'ä': 'a', "'":'', 'â': 'a'}
    substitutions = substitutions or DEFAULT_SUBSTITUTIONS
    result = ''
    for c in message.lower():
        result += c if c not in substitutions else substitutions[c]
    return result
    

def to_message(message):
    return replace_many(message).upper()


if __name__ == "__main__":
    test_frequency_analysis()
    print(chunk(to_message('juste pour rire, tu ne pourrais pas te faire un café'), 6))
