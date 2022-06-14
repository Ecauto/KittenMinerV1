import os
import sys
from colorama import Fore
import time
import secrets
from random import randint

    
if sys.platform.lower() == "win32": 
    os.system('color')

os.system("title Kitten Miner")

continuing = True

btcval = 1872.03

while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(1,70)
    if ranInt <= 1:
      randomBTC = randint(10,40)/100
      print(Fore.BLUE + "[" + Fore.GREEN + "Checking Hash" + Fore.BLUE + "] "+ Fore.GREEN + secrets.token_hex(22) + Fore.BLUE + " > " + str(randomBTC) + " ETH ($" + str("{:,}".format(round(btcval*randomBTC,2))) + ")")
      answer = input(Fore.WHITE + "> Would you like to continue? (" + Fore.GREEN + "Y" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + ")")
      if answer.lower() == "y":
        continuing = True
      else:
       continuing = False
    else:
      print(Fore.BLUE + "[" + Fore.WHITE + "Checking Hash" + Fore.BLUE + "] " + Fore.RED + secrets.token_hex(22) + Fore.WHITE + " =" + Fore.RED + " 0.00 ETH ($0.00)")
  else:
    break
  

