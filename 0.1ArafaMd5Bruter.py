#!/usr/bin/python

from termcolor import colored
from hashlib import md5

def tryOpen(wordlist):
	global pass_file
	try:	pass_file=open(wordlist,"r")
	except:	print("[!!] No such file at that path"),quit()

print("\n","\t"*5,"===>    Simple and fast MD5 Brute-force    <===","\n"),print("\t"*4,"By : Abd Almoen Arafa (0.1Arafa)"),print("\t"*4,"Age : 15\n"),print("\t"*2,"#"*75,"\n")
pass_hash=input("[*] Enter MD5 Hash value: ")
wordlist=input("[*] Enter The Wordlist: ")
tryOpen(wordlist)
count=1
for word in pass_file:
	print(colored("[ %s ] Trying : "%(count)+word.strip(),"red"))
	enc_wrd=word.encode("utf-8")
	md5digest=md5(enc_wrd.strip()).hexdigest()
	count+=1
	if md5digest == pass_hash:	print(colored("[ + ] Password found!!: "+word,"green")),quit()
print("[!!] Password not in list")
#By : Abd Almoen Arafa (0.1Arafa)
#Age : 15
