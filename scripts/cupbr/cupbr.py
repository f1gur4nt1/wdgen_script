import hashlib

nomes=[]
nome=""
while not len(nome) >=1:
  nome=input("Primeiro nome: ")
  if len(nome) <1:
    print("[!] NOME NAO PODE FICAR VAZIO!")
sobrenome=input("SobreNome: ")
apelido=input("Apelido: ")

aniverssario="0"
while not len(aniverssario) == 8:
  aniverssario=input("Aniverssario(DDMMAAAA): ")
  if len(aniverssario) <1:
    break
  if aniverssario.isnumeric() != True:
    aniverssario="0"
    print("[!]COLOQUE UM VALOR VALIDO!")
  if len(aniverssario) < 8:
    print("[!]COLOQUE UM VALOR VALIDO!")

ano=aniverssario[+4:]


#OBS: DEVO BAIXAR WORDLISTS PRA CADA TORCEDOR DE CADA TIME
print("[1]Flamengo")
print("[2]Corinthians")
print("[3]Vasco")
print("[4]Cruzeiro")
print("[5]Sao Paulo")
print("[6]Santos")
print("[7]Bota-fogo")

time=input("Qual o time que {} torce?[enter nenhum]: ".format(nome))

tm="flamengo"

if time == "1":
  tm="flamengo"
elif time == "2":
  tm ="corinthians"
elif time == "3":
  tm="vasco"
elif time == "4":
  tm="cruzeiro"
elif time == "5":
  tm ="sao paulo"
elif time == "6":
  tm="santos"
elif time == "7":
  tm ="bota-fogo"


"""
#Baixar wordlist para cada tipo de pessoa
print("[1]Religioso (cristao/catolico)")
print("[2]Otaku")
print("[3]Jogador de FF")
print("[4]Admin site")
print("[5]Bolsonarista")
print("[6]Petista")
tipo=input("qual tipo de pessoal {} é?: ".format(nome))

anime=""
if tipo == "2":
  print("[1]Naruto")
  print("[2]Dragon ball")
  print("[3]Death Note")
  print("[4]One Puch Man")
  print("[5]Nanatsu no Taizai")
  anime=input("Coloque o Anime que {} assiste[Enter Nenhum Destes]: ".format(nome))
"""



parentes=[]
parente=""
cont=1
while not parente == "p":
  parente=input("{}° Parente ([p] parar): ".format(cont))
  if not parente in parentes:
    if not parente == "p":
      parentes+=[parente]
  cont+=1



filhos=[]
"""
cont=1
filho=""
while not filho == "p":
  filho=input("{}° Filho ([p] parar): ".format(cont))
  cont+=1
  if not filho in filhos:
    if not filho == "p":
      filhos+=[filho]
"""

"""
aniver_filhos=[]
fih=""
cont=1
while not fih == "p":
  fih=input("Aniverssario do {}° Filho ([p] parar): ".format(cont))
  cont+=1
  if not fih in aniver_filhos:
    if not fih == "p":
      aniver_filhos+=[fih]
"""


#pet=input("Animal de Estimacao:" )

#impresa=input("impressa ou estabelecimento: ")




#OPCOES
print("[1]lite (cont == 99)")
print("[2]media (cont == 999)")
tamanho=input("Tamanho da wordlist: ")

if tamanho == "1":
  tam=99
if tamanho == "2":
  tam =999
if tamanho == "3":
  tam = 9999


cars_especial=input("Deseja add caracteries especiais no fim de algumas senhas?[s/N]: ")
underline=input("Deseja add underline (_) em algumas senhas?[s/N]: ")
reverse=input("Deseja add nomes invertidos nas senhas?[s/N]: ")
nmt=nome+".txt"
#ABRINDO ARQUIVO
arq=open(nmt,"a")

#CRIANDO AS SENHAS
print("\nCriando Senhas...")
#primeiras mais manuais
senhas=[]
tm=""
if len(aniverssario)==8:
  arq.write(nome+aniverssario+"\n")
  arq.write(nome+ano+"\n")
  if cars_especial == "s":
    arq.write(nome+ano+"@"+"\n")
    arq.write(nome+ano+"#"+"\n")
    arq.write(nome+ano+"$"+"\n")
    arq.write(nome+ano+"&"+"\n")
    if underline == "s":
      arq.write(nome+"_"+aniverssario+"\n")
      arq.write(nome+"_"+aniverssario+"@"+"\n")
      arq.write(nome+"_"+aniverssario+"#"+"\n")
      arq.write(nome+"_"+aniverssario+"#"+"\n")
      arq.write(nome+"_"+aniverssario+"$"+"\n")
      arq.write(nome+"_"+aniverssario+"&"+"\n")




arq.write(nome+"2000"+"\n")
arq.write(nome+"2001"+"\n")
arq.write(nome+"2002"+"\n")
arq.write(nome+"2003"+"\n")
arq.write(nome+"2004"+"\n")
arq.write(nome+"2005"+"\n")
arq.write(nome+"2006"+"\n")
arq.write(nome+"2007"+"\n")
arq.write(nome+"2008"+"\n")
arq.write(nome+"2009"+"\n")
arq.write(nome+"2010"+"\n")
arq.write(nome+"2011"+"\n")
arq.write(nome+"2012"+"\n")
arq.write(nome+"2013"+"\n")
arq.write(nome+"2014"+"\n")
arq.write(nome+"2015"+"\n")
arq.write(nome+"2016"+"\n")
arq.write(nome+"2017"+"\n")
arq.write(nome+"2018"+"\n")
arq.write(nome+"2019"+"\n")
arq.write(nome+"2020"+"\n")


cars=["@","#","$","%"]
anos=["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
if cars_especial == "s":
  for a in cars:
    for b in anos:
      if not nome+b+a in senhas:
        arq.write(nome+b+a+"\n")

cris=["jesus","cristo","jesuscristo","deus","Deus","Deusefiel","deusefiel","jeova","deussejalouvado"]

"""
if tipo == "1":
  for a in cris:
    arq.write(a+"\n")

if tipo == "1":
  for a in cris:
    for b in anos:
      arq.write(a+b+"\n")

"""


if len(tm) >=1:
  arq.write(tm+"\n")
  arq.write(tm.upper()+"\n")
s=nome[0].upper()
if len(apelido) >=1:
  arq.write(apelido+"\n")
  arq.write(apelido.upper()+"\n")
if len(sobrenome) >=1:
  s2=sobrenome[0].upper()
up=s+nome[+1:]
if len(sobrenome) >=1:
  up2=s2+sobrenome[+1:]

if len(aniverssario) == 8:
  arq.write(up+aniverssario+"\n")
if len(sobrenome) >=1:
  if len(aniverssario) == 8:
    arq.write(up2+aniverssario+"\n")
    arq.write(up+up2+aniverssario+"\n")
    arq.write(nome.upper()+sobrenome.upper()+aniverssario+"\n")
    arq.write(nome.upper()+aniverssario+sobrenome.upper()+"\n")
    arq.write(nome.upper()+aniverssario+"\n")
    arq.write(nome+sobrenome+aniverssario+"\n")
    arq.write(nome+aniverssario+sobrenome+"\n")
if cars_especial == "s":
  if len(aniverssario) == 8:
    arq.write(nome+aniverssario+"@"+"\n")
    arq.write(nome+aniverssario+"#"+"\n")
    arq.write(nome+aniverssario+"%"+"\n")
    arq.write(nome+aniverssario+"$"+"\n")
    arq.write(nome+aniverssario+"&"+"\n")

if cars_especial == "s":
  if len(aniverssario) == 8:
    arq.write(nome+"@"+aniverssario+"\n")
    arq.write(nome+"#"+aniverssario+"\n")
    arq.write(nome+"%"+aniverssario+"\n")
    arq.write(nome+"$"+aniverssario+"\n")
    arq.write(nome+"&"+aniverssario+"\n")



cont=0
while not cont == tam:
  if not nome+str(cont) in senhas:
    senhas+=[nome+str(cont)]
    arq.write(nome+str(cont)+"\n")
  if not nome+ano+str(cont) in senhas:
    senhas+=[nome+ano+str(cont)]
    arq.write(nome+ano+str(cont)+"\n")
  if reverse == "s":
    if not nome[::-1]+str(cont) in senhas:
      senhas+=[nome[::-1]+str(cont)]
      arq.write(nome[::-1]+str(cont)+"\n")
  if not nome+sobrenome+str(cont) in senhas:
    senhas+=[nome+sobrenome+str(cont)]
    arq.write(nome+sobrenome+str(cont)+"\n")
  if cars_especial == "s":
    if not nome+str(cont)+"@" in senhas:
      senhas+=[nome+str(cont)+"@"]
      arq.write(nome+str(cont)+"@"+"\n")
  if cars_especial == "s":
    if not nome+str(cont)+"#" in senhas:
      senhas+=[nome+str(cont)+"#"]
      arq.write(nome+str(cont)+"#"+"\n")
  if underline == "s":
    if not nome+"_"+str(cont) in senhas:
      senhas+=[nome+"_"+str(cont)]
      arq.write(nome+"_"+str(cont)+"\n")
    if cars_especial == "s":
      if not nome+"_"+"@" in senhas:
        senhas+=[nome+"_"+"@"]
        arq.write(nome+"_"+"@"+"\n")
      if not nome+"_"+"#" in senhas:
        senhas+=[nome+"_"+"#"]
        arq.write(nome+"_"+"#"+"\n")
      if not nome+"_"+str(cont)+"@" in senhas:
        senhas+=[nome+"_"+str(cont)+"@"]
        arq.write(nome+"_"+str(cont)+"@"+"\n")
      if not nome+"_"+str(cont)+"#" in senhas:
        senhas+=[nome+"_"+str(cont)+"#"]
        arq.write(nome+"_"+str(cont)+"#"+"\n")
      if not nome+"_"+str(cont)+"$" in senhas:
        senhas+=[nome+"_"+str(cont)+"$"]
        arq.write(nome+"_"+str(cont)+"$"+"\n")
      if not nome+"_"+str(cont)+"%" in senhas:
        senhas+=[nome+"_"+str(cont)+"%"]
        arq.write(nome+"_"+str(cont)+"%"+"\n")
  cont+=1
#PARENTES
cont=0
if len(parentes) >=1:
  for a in parentes:
    if not nome+"&"+a in senhas:
      senhas+=[nome+"&"+a]
      arq.write(nome+"&"+a+"\n")
    while not cont == tam:
      if not nome+"&"+a+str(cont) in senhas:
        senhas+=[nome+"&"+a+str(cont)]
        arq.write(nome+"&"+a+str(cont)+"\n")
      cont+=1
    for b in parentes:
      if not nome+"&"+a+"&"+b in senhas:
        if not a == b:
          senhas+=[nome+"&"+a+"&"+b]
          arq.write(nome+"&"+a+"&"+b+"\n")
      cont=0
      while not cont == tam:
        if not nome+"&"+a+"&"+b+str(cont) in senhas:
          if not a==b:
            senhas+=[nome+"&"+a+"&"+b+str(cont)]
            arq.write(nome+"&"+a+"&"+b+str(cont)+"\n")
        cont+=1

#FILHOS

if len(filhos) >=1:
  for a in filhos:
    if not nome+"&"+a in senhas:
      senhas+=[nome+"&"+a]
      arq.write(nome+"&"+a+"\n")
    for b in filhos:
      if not nome+"&"+a+"&"+b in senhas:
        senhas+=[nome+"&"+a+"&"+b]
        arq.write(nome+"&"+a+"&"+b+"\n")


arq.close()


dsj_hash=input("Deseja criar wordlist de hash md5 das senhas geradas?[s/N]\n>> ")


if dsj_hash == "s":
  arq=open(nmt,"r")
  ark=open(nome+"_hashed.txt","a")
  for a in arq:
    original=a[:-1]
    t=bytes(original.encode("utf-8"))
    k1=hashlib.md5(t)
    hash=k1.hexdigest()
    print(hash+" = "+original)
    ark.write(hash+" = "+original+"\n")
