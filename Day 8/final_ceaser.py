from logo import logo_ceaser

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo_ceaser[0])

def caesar(text, shift, encode_or_decode):
    message = ''
    if(encode_or_decode == 'encode'):
        shift *= -1
        
    for letter in text:
        if letter not in alphabet:
            message += letter
            
        else:
            position = alphabet.index(letter)
            final_posi = position - shift
            final_posi %= len(alphabet)
            message += alphabet[final_posi]
    print(f"The {encode_or_decode}d message is: {message}")
    
restart = True

while restart:
    direction = input("Type 'encode' do encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(text, shift, direction)
    decision = input("Do you want to restart? (y/n):\n").lower()
    if decision == 'n':
        restart = False
        print("IT'S OVAR!!!!")
    
