print('CEASAR CIPHER')
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text,shift_number,cipher_choice):
    end_text = ""
    if cipher_choice == 'decode':
            shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f'The {cipher_choice}d text is {end_text}')

to_continue = True
while to_continue:
    choice=input('Type "encode" if you want to encrypt or type "decode" if you want to decrypt the text message:\n')
    text=input('Enter the text message:\n').lower()
    shift=int(input('Enter the shift number:\n'))

    shift = shift % 25


    caesar(start_text=text,shift_number=shift,cipher_choice=choice)

    restart = input('Type "yes" if you want to continue, otherwise type "no".\n')
    if restart == "no":
        to_continue = False
        print('Goodbye')


