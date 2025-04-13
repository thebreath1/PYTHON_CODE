def Welc():
	print("\tLogin Account\n")
	print('\tAnda harus login terlebih dahulu.\n')


def LogUser():
	while True:
		user = input('\nMasukkan Username : ')
		if(user.isalpha()):
			break
		else:
			print("TOLOL")
			return;


def LogPw():
	while True:	
		passwd = input('\nMasukkan password anda : ')
		if(passwd.isalpha()):
			break
		else:
			print("Tolol")
			return;

Welc()
LogUser()
LogPw()
