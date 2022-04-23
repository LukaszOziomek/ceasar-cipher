def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result

def decrypt(text: str, shift: int) -> str:
    result = ""
    space = chr((ord(char) + shift - 65) % 26 + 65)
    for char in text:
        if char == space:
            result += ""
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    assert encrypt("CEASER CIPHER DEMO", 4) == "GIEWIVrGMTLIVrHIOS"
    assert encrypt("A", 1) == "B"
    assert decrypt("GIEWIVrGMTLIVrHIOS", 4) == "CEASER CIPHER DEMO"
    assert decrypt("B", 1) == "A"

print("")

