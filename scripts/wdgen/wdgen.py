

import sys


try:
  base=sys.argv[1]
except:
  print("\npython wdgen.py victiname\n")
  exit()
arq=open(base+".txt","a")

#If you think the number of passwords generated is too much
#decrease the 10000 in this while loop

cont=0
while not cont == 1000:
  arq.write(base+str(cont)+"\n")
  arq.write(base+str(cont)+"@\n")
  arq.write(base+str(cont)+"#\n")
  arq.write(base+str(cont)+"&\n")
  arq.write(base+str(cont)+"$\n")
  arq.write(base+str(cont)+"*\n")
  arq.write(base+"@"+str(cont)+"\n")
  arq.write(base+"#"+str(cont)+"\n")
  arq.write(base+"&"+str(cont)+"\n")
  arq.write(base+"$"+str(cont)+"\n")
  arq.write(base+"*"+str(cont)+"\n")
  arq.write(base+"_"+str(cont)+"\n")
  cont+=1

arq.close()
