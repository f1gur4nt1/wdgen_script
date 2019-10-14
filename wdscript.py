

import os

esc_main=esc_scripts=None


print("""\033[1;33m                              _       _   
__      ____| | ___  ___ _ __(_)_ __ | |_ 
\ \ /\ / / _` |/ __|/ __| '__| | '_ \| __|
 \ V  V / (_| |\__ \ (__| |  | | |_) | |_ 
  \_/\_/ \__,_||___/\___|_|  |_| .__/ \__|
                                |_|        \033[1;32m

--> Created by @f1gur4nt1
--> A free and open source script
--> Version 1.0
\033[0;0m
""")


def main():
  print("\n\033[1;31m[\033[0;0m0\033[1;31m] EXIT\033[0;0m")
  print("\033[1;32m[\033[0;0msc\033[1;32m] SCRIPTS\033[0;0m")
  global esc_main
  esc_main = input("\n\033[1;33mmain_menu >> \033[0;0m")


def scripts():
  print("""\033[1;33m
    ___  ___ _ __(_)_ __ | |_ ___ 
   / __|/ __| '__| | '_ \| __/ __|
   \__ \ (__| |  | | |_) | |_\__ \
                                 
   |___/\___|_|  |_| .__/ \__|___/
                   |_|""")
  print("\n\033[1;32m[\033[0;0m1\033[1;32m] Wifi Auto Crunch (ANY)")
  print("[\033[0;0m2\033[1;32m] Cuppbr Wordlist Gerador (BR)")
  print("[\033[0;0m3\033[1;32m] Simple Wordlist Gerator (ANY)")
  print("[\033[0;0m4\033[1;32m] A good Wordlist Gerator++ (ANY)")
  print("[\033[0;0m5\033[1;32m] A Wordlist Gerator++ For hashes (ANY)")
  print("\033[1;31m[\033[0;0m0\033[1;31m] BACK")
  global esc_scripts
  esc_scripts=input("\n\033[1;33mscripts >> \033[0;0m")

main()

while True:
  if esc_main == "0":
    exit()
  if esc_main == "sc":
    esc_main = None
    scripts()
  if esc_scripts == "0":
    esc_scripts = None
    main()
  elif esc_scripts == "1":
    esc_scripts = None
    print("""\033[1;32m         WifiAutoCrunch is a Script Coded by @f1gur4nt1 that\n         make wordlists using a name base of the victim or a \n         place for help to crack a Wifi HandShake.\033[0;0m""")
    exec_autocrunch=input("\n\033[1;33mExecute?[Y/n] \033[0;0m")
    if exec_autocrunch == "n":
      scripts()
    else:
      os.system("python scripts/WifiAutoCrunch/WifiAutoCrunch.py")
      print("\n\033[1;32m[+] Wordlist gerated in this same directory\n\033[0;0m")
      scripts()
  elif esc_scripts == "2":
    esc_scripts = None
    print("\n\033[1;32m         Cuppbr é um script programado por @f1gur4nt1 que\n         faz perguntas como nome, sobrenome, parentes de\n         determinada pessoa e usa essas informacoes para\n         gerar uma wordlist.""")
    exec_cup=input("\n\033[1;33mExecutar?[S/n] \033[0;0m")
    if exec_cup == "n":
      scripts()
    else:
      print("\n\n\n")
      os.system("python scripts/cupbr/cupbr.py")
      print("\n\033[1;32m[+] Wordlist gerated in this same directory\n")
      scripts()
  elif esc_scripts == "3":
    esc_scripts = None
    print("\n\033[1;32m         Wdgen is a simple wordlist gerator Created by @f1gur4nt1.")
    exec_wdgen=input("\n\033[1;33mExecute?[Y/n] \033[0;0m")
    if exec_wdgen == "n":
      scripts()
    else:
      victim=input("\033[1;33mPut the middle word: \033[0;0m")
      os.system("python scripts/wdgen/wdgen.py {}".format(victim))
      print("\n \033[1;32m[+]Wordlist gerated in this same directory\033[0;0m\n")
      scripts()
  elif esc_scripts == "4":
    esc_scripts = None
    print("\033[1;32m           Wdgen++ is a simple wordlist gerator Created by \n           @f1gur4nt1 that create a useful wordlist for crack \n           the most hard passwords.\033[0;0m")
    exec_wdgenmoremore=input("\n\033[1;33mExecute[Y/n]: \033[0;0m")
    if exec_wdgenmoremore == "n":
      scripts()
    else:
      word=input("\n\033[1;33mPut any word: \033[0;0m")
      os.system("python scripts/wdgen++/wdgen++.py {}".format(word))
      print("\n \033[1;32m[+]Wordlist gerated in this same directory\n\033[0;0m")
      scripts()
  if esc_scripts == "5":
    esc_scripts = None
    word=input("\n\033[1;33mPut any word: \033[0;0m")
    os.system("python scripts/wdgen++_for_hasher/wdgen++for_hasher.py {}".format(word))
    scripts()

