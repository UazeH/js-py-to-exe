import os, sys, time

def listmenu():
    os.system("title Menu List")
    os.system("color 0b")
    os.system('cls')
    print("""[!] Github : github.com/uazeh

[+] Menu :

[1] JS TO EXE
[2] PY TO EXE
[3] Install pkg (if you already installed it you don't need to install it again)
[4] Install pyinstaller (if you already installed it you don't need to install it again)
""")

    pilih = input("[>] Select Menu: ")

    if pilih == "1":jstoexe()
    elif pilih == '2':pytoexe()
    elif pilih == '3':installpkg()
    elif pilih == '4':pyinstalls()
    else:
        os.system("cls")
        print("Menu Not Available!")
        print(" ")
        y = input("Back To List Menu? (y/n): ")
    if y == "y":
        listmenu()

def jstoexe():
    os.system("cls")
    os.system("color 0b")
    os.system("title JS TO EXE")
    namefile = input("Enter name file (Must 1 directory) : ")
    time.sleep(1)
    os.system("pkg " + namefile + "")
    time.sleep(1)
    os.system("cls")
    os.system("color 0b")
    print("File already converted...")
    y = input("Back To List Menu? (y/n): ")
    if y == "y":
        listmenu()

def pytoexe():
    os.system("cls")
    os.system("color 0b")
    os.system("title PY TO EXE")
    namefile1 = input("Enter name file (Must 1 directory) : ")
    time.sleep(1)
    os.system("pyinstaller -F " + namefile1 + "")
    time.sleep(5)
    os.system("cls")
    os.system("color 0b")
    print("File already converted...")
    y = input("Back To List Menu? (y/n): ")
    if y == "y":
        listmenu()

def installpkg():
    os.system("npm install -g pkg")
    os.system("cls")
    os.system("color 0b")
    y = input("Back To List Menu? (y/n): ")
    if y == "y":
        listmenu()

def pyinstalls():
    os.system("pip install pyinstaller")
    os.system("cls")
    os.system("color 0b")
    y = input("Back To List Menu? (y/n): ")
    if y == "y":
        listmenu()

listmenu()
