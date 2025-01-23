import rarfile
import os
import zipfile
import threading
import time

os.system("")
class style():
  RED = '\033[31m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  CYAN = "\033[1;36m"
  RESET = '\033[0m'

print(style.RED + "{0}".format('-----------------------------------------------------------------------') + style.RESET)
print(style.BLUE + "{0}".format('Welcome to ZIP & RAR Password Crack tool') + style.RESET)
print(style.RED + "{0}".format('-----------------------------------------------------------------------') + style.RESET)
time.sleep(1)

print(style.BLUE + "{0}".format('Add Password Path> ') + style.RESET)
pass_path = input(r'')[1:-1]

with open(pass_path, 'a') as file:
    file.write('\n Password Not found in this file!')
    file.close()

with open(pass_path, 'r') as file:
    lines = len(file.readlines())
    print('[!]' , style.BLUE + "{0}".format('Total Passwords to try:'), style.CYAN + "{0}".format(lines) + style.RESET)
    file.close()


def rar_f():
    global path
    with open(pass_path, 'rb') as text:
        for entery in text.readlines():
            password = entery.strip()
            try:
                with rarfile.RarFile(file=path, mode='r') as rf:
                    try:
                        if rf.needs_password():
                            rf.setpassword(pwd=password)
                    except rarfile.NoCrypto:
                        time.sleep(1)
                        clear = "\n" * 13
                        print(clear)
                        time.sleep(1)
                        print(style.BLUE + "{0}".format('----------PASSWORD SPOTED----------') + style.RESET)
                        print('Password Found >>', style.GREEN + "{0}".format(password.decode()) + style.RESET)
                        text.close()

                        break
                    except Exception as e:
                        print('Trying Password >', style.RED + "{0}".format(password.decode()) + style.RESET)
            except:
                pass
        else:
            with open(pass_path, 'r') as file:
                time.sleep(1)
                clear = "\n" * 13
                print(clear)
                time.sleep(1)
                print('-------------------', style.RED + "{0}".format(file.readlines()[-1]) + style.RESET,'-------------------')
                file.close()
                text.close()



def zip_f():
    global path
    with open(pass_path, 'rb') as text:
        for entery in text.readlines():
            password = entery.strip()
            try:
                with zipfile.ZipFile(file=path, mode='r') as zf:
                    zf.extractall(pwd=password)
                    time.sleep(1)
                    clear = "\n" * 13
                    print(clear)
                    time.sleep(1)
                    print(style.BLUE + "{0}".format('----------PASSWORD SPOTED----------') + style.RESET)
                    print('Password Found >>', style.GREEN + "{0}".format(password.decode()) + style.RESET)
                    text.close()
                    break
            except:
                print('Trying Password >', style.RED + "{0}".format(password.decode()) + style.RESET)
                pass
        else:
            with open(pass_path, 'r') as file:
                time.sleep(1)
                clear = "\n" * 13
                print(clear)
                time.sleep(1)
                print('-------------------', style.RED + "{0}".format(file.readlines()[-1]) + style.RESET,'-------------------')
                file.close()
                text.close()

def new_dell():
    with open(pass_path, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(pass_path, 'w') as fout:
        fout.writelines(data[:-1])
        fin.close()
        fout.close()





def main():
    global command
    if command == 'ZIP':
        zip_f()
    elif command == 'RAR':
        rar_f()
    else:
        print(style.RED + "{0}".format('Choose RAR or ZIP ONLY!') + style.RESET)


print(style.RED + "{0}".format('[!]') + style.RESET,'Choose Between a Zip or Rar ONLY!')
time.sleep(1)
command = input('Please Enter File Type > ').upper()

print('Add a path > ')
path = input(r'')[1:-1]

txt = 'Note that you are going to run the code multiple times and you have {} CPUs Please choose the number of the treads wisely'
print('[!]' ,style.RED + "{0}".format(txt.format(os.cpu_count())) + style.RESET)
ran = input("How many Threads would you like to run > ")
threads = list()
for i in range(int(ran)):
    x = threading.Thread(target=main)
    threads.append(x)
    x.start()


for index, thread in enumerate(threads):
    thread.join()


new_dell()