import string

def ceasar(plainText):
    # plainText = raw_input('Enter the phrase to encrypt: ')
    lower_index = 0
    upper_index = 0
    result = ''
    lower_alpha = string.ascii_lowercase
    upper_alpha = string.ascii_uppercase
    for char in plainText:
        if char.isalpha() == True:
            if char.isupper() == True:
                upper_indexndex = upper_alpha.index(char)
                encrypted = upper_index + 13
                if encrypted > 25:
                    encrypted = encrypted % 26
                result += upper_alpha[encrypted]
            elif char.islower() == True:
                lower_index = lower_alpha.index(char)
                encrypted = lower_index + 13
                if encrypted > 25:
                    encrypted = encrypted % 26
                result += lower_alpha[encrypted]
        else:
            result += char
        encrypted = 0
    print result

ceasar('Be sure to drink your Ovaltine!')