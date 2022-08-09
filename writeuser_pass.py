# This is a test program which I wish to convert into a usable code to store passes in a text file using python

import hashlib as hs

task_name = input("Enter the task for which you want to find and store the salted hashed value: \n")
hashinput= input("Enter the input string to get hash 256 :\n")
hashvalue= hs.sha256(hashinput.encode('utf-8')).hexdigest()
print("\nThe sha256 of {} is {}".format(hashinput,hashvalue))
print(len(hashvalue), (hashvalue.encode('utf-8')))
print("\nNow lets hash the input using a passphrase..\n")
#withpassphrase
passphrase= input("Enter a passphrase: \n")
temp_str= hashinput + passphrase
salted_hash_value = hs.sha256(temp_str.encode('utf-8')).hexdigest()
print(" \nThe salted hashvalue with your input and passphrase is:\n ",salted_hash_value)

# hashing thepassord and  passphrase before generating tge hash
print("\nNow lets hash the hash of both input and the passphrase..\n")
passphr_hash_value = hs.sha256(passphrase.encode('utf-8')).hexdigest()
print("The passphrase hash is: {}\n".format(passphr_hash_value))
pause = input("\nPress enter to get the hash of hashed input and passphrase:\n ")
# Here we are again hashing the( hashed inputstring + hashed passphrase) by joining the two hashes as string
temp_hashed_string = hashvalue + passphr_hash_value
hashed_salted_hash_value = hs.sha256(temp_hashed_string.encode('utf-8')).hexdigest()
print("\nHashed salted hashed value is :{}".format(hashed_salted_hash_value))
usr_data = task_name+ hashed_salted_hash_value
#Now lets write the hasged salted hashes to a file

with open("mypsses.txt",'a') as fw:
	print("Lets write the data in a file")
	print("The user data is as under :", usr_data)
	confirm_write = input("press 'y' without quotes to write the data in a file: ")
	if (confirm_write == 'y'):
		fw.write(usr_data)
		print("User details have been written in mypsses.txt")
	else:
		print("Nothing written")
	fw.close()
		
		
