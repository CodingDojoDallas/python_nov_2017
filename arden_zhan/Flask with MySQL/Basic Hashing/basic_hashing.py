import md5 # imports the md5 module to generate a hash
password = 'password'
# encrypt the password we provided as 32 character string
hashed_password = md5.new(password).hexdigest()
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!


# Salted Hashing

import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))

# salt = '123' #where the value 123 changes randomly
hashed_password = md5(password + salt)
print hashed_password
