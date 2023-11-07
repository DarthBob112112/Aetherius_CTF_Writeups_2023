from sympy import *
from sympy.abc import x

def to_matrix(str):
    ar=[]
    for i in range(3):
        ar.append(ord(str[i])-ord('a'))
    return Matrix(Array(ar,(3,1)))

def to_text(mat):
    return "".join(str(chr(mat[i]+ord('a'))) for i in range(3))

def from_matrix(mat):
    return "".join(str(chr(int(mat[i])+ord('a'))) for i in range(3))

def decrypt(encrypted_flag, encrypted_helper, matrices,key):
    flag_dec = ''
    helper_dec = ''
    for i in range(len(encrypted_flag)//3):
        enc_flag_part = to_matrix(encrypted_flag[3*i:3*(i+1)])
        enc_helper_part = to_matrix(encrypted_helper[3*i:3*(i+1)])
        mat = matrices[i]
        if i==9-1:          #bruteforcing value of x in matrix
            mat[i]=key
        mat=Matrix(Array(mat,(3,3)))

        dec_flag_part = (mat.inv_mod(26) * enc_flag_part) % 26
        dec_helper_part = (mat.inv_mod(26) * enc_helper_part) % 26

        flag_dec += from_matrix(dec_flag_part)
        helper_dec += from_matrix(dec_helper_part)

    return flag_dec, helper_dec

# Read the encrypted flag and helper text from the file
with open("./enc_flag.txt", "r") as file:
    # print()
    encrypted_flag, encrypted_helper = file.read().split('\n')[:-1]

# Read the matrices from the file
with open("./matrix.txt", "r") as file:
    matrices = [Matrix(eval(line)) for line in file]

for key in range(26):
    try:
        flag, helper = decrypt(encrypted_flag, encrypted_helper, matrices,key)  #bruteforces the value of x
        print(key)
        print(f"Decrypted flag: {flag}")
        print(f"Decrypted helper: {helper}")
    except:
        pass
    
flag, helper = decrypt(encrypted_flag, encrypted_helper, matrices,11)
# flag, helper = decrypt(encrypted_flag, encrypted_helper, matrices)
print(f"Decrypted flag: {flag}")
print(f"Decrypted helper: {helper}")