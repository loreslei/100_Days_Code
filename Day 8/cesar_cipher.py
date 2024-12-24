alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' do encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))

size_alphabet = len(alphabet)

def caesar(text, shift, direction):
    if(direction == 'encode'):
        encrypt(text, shift)
    else:
        decrypt(text, shift)

def encrypt(text, shift):
    message = ''
    for letter in text:
        position = alphabet.index(letter)
        final_posi = position + shift
        #solucao 1
        #if(final_posi > len(alphabet)):
        #    final_posi -= len(alphabet)
        #solucao 2
        final_posi %= len(alphabet)
        message += alphabet[final_posi]
    print(message)
    
    
def decrypt(text, shift):
    message = ''
    for letter in text:
        position = alphabet.index(letter)
        final_posi = position - shift
        #solucao 1
        #if(final_posi > len(alphabet)):
        #    final_posi -= len(alphabet)
        #solucao 2
        final_posi %= len(alphabet)
        message += alphabet[final_posi]
    print(message)



    
caesar(direction)