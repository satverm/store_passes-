# This is a test program which I wish to convert into a usable code to store passes in a text file using python

import hashlib as hs

# task name is the input which will be stored as it is to provide the user a description about the passes you have stored as hex codes
print("Let's first store some details which we can associate the pass to be secured by hashing.\n")
task_name = input("Enter the task for which you want to store the  hashed value: \n")
input_pass= input("Enter the input string(pass) which you want to soore as hash 256 :\n")
input_hashvalue= hs.sha256(input_pass.encode('utf-8')).hexdigest()
print("\nThe sha256 of {} is {}".format(input_pass,input_hashvalue))
print(len(input_hashvalue), (input_hashvalue.encode('utf-8')))
print("\nNow lets hash the input using a passphrase..\n")
# Now let's add a pass-phrase and hash it to secure.
while True:
	passphrase= input("Enter a passphrase to secure the input strings: \n")
	print("Remember the passphrase or write in a piece of paper!!\n")
	passphrase_confirm = input("Enter the pass-phrase again to confirm: ")
	if passphrase == passphrase_confirm:
		passphr_hash_value = hs.sha256(passphrase.encode('utf-8')).hexdigest()
		print("The passphrase hash is: {}\n".format(passphr_hash_value))
		break
	else:
		print("The pass-phrase entered by you don't match!!\n")
# the commented code bellow can be used for hashing only once.
# temp_str= input_pass + passphrase
# salted_hash_value = hs.sha256(temp_str.encode('utf-8')).hexdigest()
# print(" \nThe salted input_hashvalue with your input and passphrase is:\n ",salted_hash_value)

# hashing the input_pass and  passphrase before generating the hash
# Here we are again hashing the( hashed inputstring + hashed passphrase) by joining the two hashes as string
print("\nNow lets hash the hash of both input and the passphrase..\n")
temp_hashed_string = input_hashvalue + passphr_hash_value
# let's hash the temp_hashed_string
hashed_salted_hash_value = hs.sha256(temp_hashed_string.encode('utf-8')).hexdigest()
pause = input("\nPress enter to get the hash of hashed input and passphrase:\n ")
print("\nHashed salted hashed value is :{}".format(hashed_salted_hash_value))
# usr_data is the variable to store the information as a string which can be stored in a file
usr_data = task_name +':'+ hashed_salted_hash_value  # ':' is used as a separator

#Now lets write the secured information to a file
print("The secured information can be stored in a file\n")
default_file = input("Press 'y' to select a new file name or Enter to use default (my_passes.txt)")
if default_file == 'y':
	file_to_store = input("Enter the file name to store the information.. (any_file_name.txt):")
else:
	file_to_store = 'my_passes.txt'
print("The information will be stored in a file {}".format(file_to_store))

with open(file_to_store,'a') as fw:
	print("Lets write the data in a file")
	print("The user data is as under :", usr_data)
	confirm_write = input("press 'y' without quotes to write the data in the file: ")
	if (confirm_write == 'y'):
		fw.writelines(usr_data)
		
		print("User details have been written in the file :{}".format(file_to_store))
		print("Program finished with success..")
	else:
		print("Nothing written in file\n")
		print("Closing the file and exiting program!!")
	fw.close()
		
		
