

import os


saida = os.popen("apt list | grep installed").read()

if not "crunch" in saida:
  print("[!] Please, Install the Crunch to continue!\n\napt-get install crunch\nIn the Termux: pkg install unstable-repo;pkg install crunch")
  exit()

nomes = []

for n in range(1,9999):
  print("\nOBS: type stop for break this loop!\n")

  nome = input("Name of the {}° Victim: ".format(n))

  if nome != "stop":
    nomes += [nome]

  else:
    break



def crunch(nome):
  cpm = ""
  for n in range(1,6):
    cpm += "@"
    leno = len(nome+cpm)
    if leno >= 8:
      a = os.popen("crunch {} {} @#$%_-0123456789 -t {}{} >> {}_wordlist.txt&".format(leno,leno,nome,cpm,pnome))


  leno = len(nome+"@@")
  if leno >= 8:
    a = os.popen("crunch {} {} @#$%-_0123456789 -t {}{}{} >> {}_wordlist.txt&".format(leno,leno,"@",nome,"@",pnome))

  leno = len(nome+"@@@@")
  if leno >= 8:
    a = os.popen("crunch {} {} @#$%-_0123456789 -t {}{}{} >> {}_wordlist.txt&".format(leno,leno,"@@",nome,"@@",pnome))



pnome = nomes[0]
for nome in nomes:
  nome = nome.lower()
  crunch(nome)
  crunch(nome.upper())
  crunch(nome[:1].upper()+nome[1:])

