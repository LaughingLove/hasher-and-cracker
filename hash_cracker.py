import hashlib
import os
import sys

def encrypt_hash(hash, name):
    return hashlib.new(hash, str.encode(name)).hexdigest()

def decrypt_hash(hash, pass_list):
    len_of_hash = len(hash)
    if len_of_hash is 128:
        type_of_hash = "sha512"
    elif len_of_hash is 96:
        type_of_hash = "sha384"
    elif len_of_hash is 64:
        type_of_hash = "sha256"
    elif len_of_hash is 56:
        type_of_hash = "sha224"
    elif len_of_hash is 40:
        type_of_hash = "sha1"
    elif len_of_hash is 32:
        type_of_hash = "md5"
    else:
        print("Error: Cannot detect type of hash!")
        sys.exit()
    found = False
    for word in pass_list:
        encrypted_word = encrypt_hash(type_of_hash, word)
        if encrypted_word == hash.lower():
            print("Found! {}: {}".format(encrypted_word, word))
            found = True
    if not found:
        print("Cannot decrypt the hash using the password list given!")

def main():
    print("""
    1.) Hash
    2.) Crack a hash
    """)
    res = input("Pick one: ")

    if not res.isdigit():
        print("NaN!")
    else:
        if res == "1":
            hashes = {
                1: "md5",
                2: "sha1",
                3: "sha224",
                4: "sha256",
                5: "sha384",
                6: "sha512"
            }
            print("""
            Hashes
            1.) md5
            2.) sha1
            3.) sha224
            4.) sha256
            5.) sha384
            6.) sha512
            """)
            type_of_hash = input("Pick type of hash to encrypt: ")

            if not type_of_hash.isdigit():
                print("NaN!")
            else:
               name = input("String to be hashed: ")
               the_hash = encrypt_hash(hashes[int(type_of_hash)], name)
               print(the_hash)
        elif res == "2":
            hash_decrypt = input("Enter the hash to be decrypted: ")
            pass_list = input("Enter the directory of the password list: ")
            word_list = []
            
            if "~" in pass_list:
                pass_list = pass_list.replace("~", os.environ['HOME'])

            if not os.path.exists(pass_list):
                print("Directory given does not exist")
                sys.exit()
            
            with open(pass_list) as f:
                for line in f:
                    # :-1 removes \n from each line
                    if "\n" in line:
                        # Adds the word to the array
                        word_list.append(line[:-1])
                    else:
                        word_list.append(line)
            decrypt_hash(hash_decrypt, word_list)
            

if __name__ == "__main__":
    main()