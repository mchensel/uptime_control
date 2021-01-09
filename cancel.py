import main
import getpass
import mypass

msg = "Du musst Papa oder Mama fragen!"
p=""
while p != mypass.my_simple_pass:
	p = getpass.getpass(msg)

	if p == mypass.my_simple_pass:
		with open(main.FILE_NAME, "w") as f:
			f.write(main.CANCEL)
			exit()
	else:
		print("falsch.")
	
