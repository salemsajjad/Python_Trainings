import csv
from hashlib import sha256
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):

    hashes = OrderedDict()
    hash_password_to_password = OrderedDict()

    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            hashes[row[1]] = row[0]
    
    for password in range(1000,10000):
            hashing_number = sha256(b'%i' % password).hexdigest()
            hash_password_to_password[hashing_number] = password
    
    with open(output_file_name , 'w') as out:
        count = 0
        for password in hashes.keys():
            if password in hash_password_to_password.keys():
                count += 1
                person = hashes[password]
                four_digit_pass = hash_password_to_password[password]
                if count == 1:
                    out.write(person + ","+ str(four_digit_pass))
                else:
                    out.write("\n"+ person+ ","+ str(four_digit_pass))



        
    



