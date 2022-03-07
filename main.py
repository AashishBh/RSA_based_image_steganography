from encryptor import decrypt, generate_keypair, encrypt
from steganography import steganography_decode, steganography_encode
# ask user if he/she wants to encode or decode:

user_choice = input('Hello, Type 1 to Encode and 2 to Decode. ')
print(user_choice)
if user_choice=='1':
    message = input('\nEnter a message to encrypt with your private key: \n')
    if (len(message)==0):
        raise ValueError('Data is empty')
    public, private = generate_keypair(17,23)
    print(public)
    print('Use this key to decode: ' + str(public[0]))
    encrypted_msg = encrypt(private,message) 
    encrypted_message_string = ''
    for item in encrypted_msg:
        encrypted_message_string+=str(item)+'-'
    print('The encrypted message is : ' + encrypted_message_string)
    
    # now encrypting with steganography
    steganography_encode(encrypted_message_string)
elif user_choice=='2':
    userInput = int(input('enter the public keys '))
    public = (userInput,391)
    print(public)
    steganophaphy_decoded_msg = steganography_decode()
    steganography_decoded_msg_list = list(steganophaphy_decoded_msg.split('-'))
    print(steganography_decoded_msg_list)
    decrypted_msg = list(decrypt(public, steganography_decoded_msg_list))
    decrypted_msg_string = ''
    for letter in decrypted_msg:
        decrypted_msg_string += letter
    print(decrypted_msg_string)

else:
    print('invalide choice')
