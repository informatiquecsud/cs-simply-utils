class SwapCypher:

    @staticmethod
    def even_to_odd(init_position):
        if init_position % 2 == 0:
            return init_position + 1
        else:
            return init_position - 1

    def __init__(self, index_swap_func=None):
        self.index_swap_func = index_swap_func or SwapCypher.even_to_odd

    def encrypt(self, message):
        result = list(message)
        swapped = [False] * len(message)

        for i, char in enumerate(result):
            if not swapped[i]:
                j = self.index_swap_func(i)
                try:
                    result[i], result[j] = result[j], result[i]
                    swapped[i] = swapped[j] = True
                except:
                    # handle the odd number of letters casey
                    pass

        return ''.join(result)


def test():
    message = "PEUTONSEVOIRATREIZEHEURES"
    message = "OKNEENWNRINUUSNMUETNERFFNE"
    message = "IDTEXEETNIMEIASLISDNIWOEFFNEBEIRFEE"
    message = "UNCOURRIELESTCOMMEUNELETTREOUVERTE"
    def nils_swap(i): return i + (-1) ** i
    cyphered = SwapCypher(nils_swap).encrypt(message)
    print(message, "=>", cyphered)

    message = "OUIRENDEZVOUSAUKIOSK"
    message = "KSOIKTKNUPFFERTAJ"
    def mia_swap(i): return -i - 1
    cyphered = SwapCypher(mia_swap).encrypt(message)
    print(message, "=>", cyphered)

    message = "HCSIERDEBNIEAPEWSSREORETEINCNUFIHIRFTREFUA"
    message = "NECRISJAMAISTESMOTSDEPASSEENCLAIR"
    message = "ABCDEF"
    def tim_swap(i): return (i + 2 if (i % 3 == 0) else i)
    cyphered = SwapCypher(tim_swap).encrypt(message)
    print(message, "=>", cyphered)


if __name__ == "__main__":
    test()
