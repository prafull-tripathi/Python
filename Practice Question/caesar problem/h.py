import string

def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)

    return plain_text[::-1].translate(trantab)

str=input("String?")
shift=int(input("shift by"))
print(caesar(str,shift))