#!/usr/bin/python

# Mahdi M3x 
# Welcome to Word Generator.
# This program works same as 'Crunch' in kali Linux.

import sys
import itertools

print "[=] Welcome to Pybf tool! [=]"
print "[=] To continue type '1' [=]"
print "[=] To exit type '0' [=]"

choice = input()
if choice.lower() == '1':
	length = raw_input("Please type in what would be the maximum length\n>>>")
	letters = raw_input("Please type in the letters you want to generate\n>>>")
	generate = list(map(''.join, itertools.product(letters, repeat=int(length))))
	print "The output length would be: ", len(generate)
	fs = open("Pybf-Generates", "w")
	for i in range(int(length)+1):
		for w in itertools.permutations(letters, i):
			fs.write("".join(w) + "\n")
			fs.flush() # For the buffer..
		f.close()
		
elif choice.lower() == '0':
	print "[=] Thanks for using Bypf [=]"
	sys.close()
	
else:
	print "[!] Invalid Input.. Try Again [!]"
