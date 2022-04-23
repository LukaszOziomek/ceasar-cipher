import string

# Z INTERNETU https://python101.readthedocs.io/pl/latest/podstawy/przyklady/przyklad07.html

KLUCZ = 3


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny


def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania: ")
    print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))