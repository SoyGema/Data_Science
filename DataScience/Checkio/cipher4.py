def recall_password(cipher_grille, ciphered_password):
    message = ''
    
    for turn in range(0,4):
        for row in range(0,4):
            for column in range(0,4):
                if cipher_grille[row][column] == 'X':
                    message += ciphered_password[row][column]
                    
        
        rotate_cipher_grille = ()
        for column in range(0,4):
            new_row = ''
            for row in range(0,4):
                new_row += cipher_grille[3-row][column]    
            
            rotate_cipher_grille += (new_row,)
        cipher_grille = rotate_cipher_grille
    
    return message


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
