

import sys
import time

base=sys.argv[1]

wordlist=open(base+".txt","a")
global wdbase
wdbase=[]

def leet_lite():
  baseleet=base.replace("a","4")
  baseleet=baseleet.replace("e","3")
  baseleet=baseleet.replace("o","0")
  global baseleetlite
  baseleetlite=baseleet





def leet_medio():
  baseleet=base.replace("a","4")
  baseleet=baseleet.replace("e","3")
  baseleet=baseleet.replace("o","0")
  baseleet=baseleet.replace("t","7")
  baseleet=baseleet.replace("l","1")
  baseleet=baseleet.replace("s","5")
  global baseleetmedio
  baseleetmedio=baseleet


def leet_foda():
  baseleet=base.replace("a","4")
  baseleet=baseleet.replace("e","3")
  baseleet=baseleet.replace("o","0")
  baseleet=baseleet.replace("t","7")
  baseleet=baseleet.replace("s","5")
  global leetfoda
  leetfoda=baseleet.replace("g","6")
  leetfoda=leetfoda.replace("i","1")




def base_parcial_upper():
  global leters
  leters=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
  global baseupper
  baseupper=""
  for a in base:
    if a in leters:
      baseupper+=a.upper()
    else:
      baseupper+=a

def vogalupper():
  let=["a","e","i","o","u"]
  global vogalup
  vogalup=""
  for a in base:
    if a in let:
      vogalup+=a.upper()
    else:
      vogalup+=a



def base_upper():
  global baseup
  baseup=base.upper()

def leet_parcialupper():
  global bleetpacial
  bleetpacial=""
  for a in base:
    if a in leters:
      bleetpacial+=a.upper()
    else:
      bleetpacial+=a
  baseleet=bleetpacial.replace("a","4")
  baseleet=baseleet.replace("e","3")
  bleetpacial=baseleet.replace("o","0")

def especial_substituir():
  global esp1
  global esp2
  global esp3
  global esp4
  global esp5
  global esp6
  global esp7
  global esp8
  global esp9
  global esp10
  esp1=base.replace("a","@")
  esp2=base.replace("e","&")
  esp3=base.replace("e","€")
  esp4=base.replace("s","$")
  esp5=base.replace("c","¢")
  esp6=esp1.replace("e","&")
  esp7=esp1.replace("e","€")
  esp8=esp7.replace("c","¢")
  esp9=esp4.replace("a","@")
  esp10=esp8.replace("s","$")

def youiscomplicated():
  global comp1
  global comp2
  global comp3
  global comp4
  global comp5
  global comp6
  global comp7
  global comp8
  global comp9
  global comp10
  global comp11
  global comp12
  comp1=base.replace("a","A")
  comp2=comp1.replace("e","3")
  comp3=comp2.replace("o","0")
  comp4=comp3.replace("s","5")
  comp5=base.replace("e","E")
  comp6=comp5.replace("a","4")
  comp7=comp6.replace("o","0")
  comp8=comp7.replace("s","5")
  comp9=base.replace("o","O")
  comp10=comp9.replace("a","4")
  comp11=comp10.replace("e","3")
  comp12=comp11.replace("s","5")

def up_fist():
  global first_letter
  first_letter = base.replace(base[0],base[0].upper())

def up_up():
  global fim
  fim=""
  cont=0
  for a in base:
    if cont%2 == 0:
      fim+=a.replace(a,a.upper())
    else:
      fim+=a
    cont+=1


def parcial_upper_leet():
  global leters
  leters=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
  global baseupperleet
  baseupperleet=""
  for a in base:
    if a in leters:
      baseupperleet+=a.upper()
    else:
      if a == "a":
        baseupperleet+=a.replace("a","4")
      elif a == "e":
        baseupperleet+=a.replace("e","3")
      elif a == "o":
        baseupperleet+=a.replace("o","0")
      elif a == "i":
        baseupperleet+=a.replace("i","!")

leet_lite()
leet_medio()
leet_foda()
base_parcial_upper()
vogalupper()
base_upper()
leet_parcialupper()
especial_substituir()
youiscomplicated()
up_fist()
up_up()
parcial_upper_leet()

if not baseleetlite in wdbase:
  wdbase+=[baseleetlite]
if not baseleetmedio in wdbase:
  wdbase+=[baseleetmedio]
if not baseupper in wdbase:
  wdbase+=[baseupper]
if not baseup in wdbase:
  wdbase+=[baseup]
if not bleetpacial in wdbase:
  wdbase+=[bleetpacial]

wdbase+=[first_letter]

wdbase+=[base]

wdbase+=[esp1,esp2,esp3,esp4,esp5,esp6,esp7,esp8,esp9,esp10]

wdbase+=[esp1.upper(),esp2.upper(),esp3.upper(),esp4.upper(),esp5.upper(),esp6.upper(),esp7.upper(),esp8.upper(),esp9.upper(),esp10.upper()]

wdbase+=[comp1,comp2,comp3,comp4,comp5,comp6,comp7,comp8,comp9,comp10,comp11]

wdbase+=[fim,baseupperleet]

def rm_repete():
  for a in wdbase:
    if wdbase.count(a) > 1:
      while not wdbase.count(a) == 1:
        wdbase.remove(a)

rm_repete()

for a in wdbase:
  wordlist.write(a+"\n")
  wordlist.write(a+"@\n")
  wordlist.write(a+"#\n")
  wordlist.write(a+"$\n")
  wordlist.write(a+"%\n")
  wordlist.write(a+"&\n")
  wordlist.write(a+"_\n")
  wordlist.write(a+"_@\n")
  wordlist.write(a+"_#\n")
  wordlist.write(a+"_$\n")
  wordlist.write(a+"_%\n")
  wordlist.write(a+"_&\n")

cont=0
for a in wdbase:
  cont=0
  while not cont == 100:
    wordlist.write(a+str(cont)+"\n")
    #if you need,Put "#" (comment) in one of these two lines below
    wordlist.write(a+"_"+str(cont)+"\n")
    wordlist.write(a+"-"+str(cont)+"\n")
    cont+=1


#if you wanna edit for decrease or increase the number of wordlist,
#edit the var cont1.

cont1=1970
for a in wdbase:
  cont1=1970
  while not cont1 == 2021:
    wordlist.write(a+str(cont1)+"\n")
    wordlist.write(a+"_"+str(cont1)+"\n")
    wordlist.write(a+"-"+str(cont1)+"\n")
    cont1+=1


for a in wdbase:
  contf=100
  while not contf == 999:
    wordlist.write(a+str(contf)+"\n")
    #wordlist.write(a+"_"+str(contf)+"\n")
    #wordlist.write(a+"-"+str(contf)+"\n")
    contf+=1

cont=100
while not cont == 1000:
  #wordlist.write(base+str(cont)+"\n")
  cont+=1


print("\n\nIf you think tht the wordlists gerated is very big, please, edit de source code of the wdgen++ in script/wdgen++/wdgen++.py\n\n")

time.sleep(2)
