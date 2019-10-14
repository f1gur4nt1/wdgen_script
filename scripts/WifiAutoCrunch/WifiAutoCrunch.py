import os


saida=os.popen("apt list | grep installed").read()

if not "crunch" in saida:
  print("[!] Please, Install the Crunch to continue!\n\napt-get install crunch\nIn the Termux: pkg install unstable-repo;pkg install crunch")
  exit()
else:
  nome=input("Name of the Victim: ")
  ano="2019"
  cars=("@")
  tam=len(nome)+len(cars)
  if tam >= 8:
    os.system("crunch {} {} @#$0123456789 -t {}{} >> {}.txt".format(tam,tam,nome,cars,nome))
  cars=("@@")
  tam=len(nome)+len(cars)
  if tam >= 8:
    os.system("crunch {} {} @#$0123456789 -t {}{} >> {}.txt".format(tam,tam,nome,cars,nome))
  cars=("@@@")
  tam=len(nome)+len(cars)
  if tam >= 8:
    os.system("crunch {} {} @#$0123456789 -t {}{} >> {}.txt".format(tam,tam,nome,cars,nome))
  cars=("@@@@")
  tam=len(nome)+len(cars)
  if tam >= 8:
    os.system("crunch {} {} @#$0123456789 -t {}{} >> {}.txt".format(tam,tam,nome,cars,nome))
  cars=("@@@@@")
  tam=len(nome)+len(cars)
  if tam >= 8:
    os.system("crunch {} {} @#$0123456789 -t {}{} >> {}.txt".format(tam,tam,nome,cars,nome))
  cars=("{}@".format(ano))
  tam=len(nome)+len(cars)
  if tam >= 8:
    os.system("crunch {} {} @#$0123456789 -t {}{} >> {}.txt".format(tam,tam,nome,cars,nome))

