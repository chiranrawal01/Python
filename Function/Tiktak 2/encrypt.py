           
# Ceasar cipher
# encrypt(msg,key)
#if
def ciper(msg, key, type='encrypt'):
    msg = msg.upper()
    new_msg_list =[]
    for each_char in msg :
        if(type == 'encrypt'):
            new_msg_list.append(chr(ord(each_char) + key))
        elif(type == 'decrypt'):
            new_msg_list.append(chr(ord(each_char)- key))
    return ''.join(new_msg_list)

    if _name_ =='_main_':
        encrpted_msg = ciper("helloz", 3)
        print(encrypted_msg)
        decrypted_msg = ciper(encrypted_msg,3, type='decrypt')
        print(decrypted_msg)


