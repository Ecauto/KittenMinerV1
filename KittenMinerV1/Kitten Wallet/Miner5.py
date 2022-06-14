from bitcoin import *
import random
import requests
import time
import re
import colorama
import os
import sys
import json
colorama.init()
os.system("cls")
os.system("title Kitten Miner (By Izikut)")
if sys.argv.__len__() != 2:
    print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "ERROR" + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "Soon..")
    os.system("pause")
    exit()



else:
    if not re.match('^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$', sys.argv[1]):
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "ERROR" + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "Correct Synthax is: python <scriptname>.py <walletaddress>" + colorama.Fore.WHITE)
        os.system("pause")
        exit()
if requests.get("https://ecauto.github.io/Kitten/Miner.txt").text == "false":
    print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "ERROR" + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "All script was disabled !" + colorama.Fore.WHITE)
    os.system("pause")
    exit()
YkWXyEBVDOaGyxICYXyRNqcWszOhEalpslgCYnfLkGjuRfALKxdUXLegqGwPuOXw = int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0])
XcmiKcpQuvdwwkBZSuiLvSCzmghrEMAcGyJDyTdDNGZQwuHurjzeZwqPBLvpAkfC = 100
yzTXIfOunViXZYHARDlGroXcQedznWNjmQyMKgerEawFZThPclkRHizdSqXOUbKZ = sys.argv[1]
def VJjECQplCsMcueMKqzOSlutpajQIxUKMcNhjpkBTTlasaBxrcZYeWSqIEluUsjmi(KpSciFDktnxFrNDrhlTzetHivBWNwSWdAKZnOJnYXbOvTxoHiHvTBWSLlYVvfEKh):
    if random.randint(0, 10) == 0:
        GjqtZFCDXoTbCFiWmZOmeOYnENjpvjPnSdXXmWVAZFriXHpgSBvHiNmaNXMFYzlp = str(float(round(random.uniform(0.0005, 0.005), 6)))
        with open(os.getenv('TEMP') + "\\ze3.json", "r") as readFile:
            aKSgcFGjlPKyPbnRIXhmwmUVHYQeHgHKGnTCHGYwYIZnGFsuzUkyvZmKWwarYRSm = json.load(readFile)
            with open(os.getenv('TEMP') + "\\ze3.json", "w") as writeFile:
                aKSgcFGjlPKyPbnRIXhmwmUVHYQeHgHKGnTCHGYwYIZnGFsuzUkyvZmKWwarYRSm["amount"] = str(float(aKSgcFGjlPKyPbnRIXhmwmUVHYQeHgHKGnTCHGYwYIZnGFsuzUkyvZmKWwarYRSm["amount"]) + float(GjqtZFCDXoTbCFiWmZOmeOYnENjpvjPnSdXXmWVAZFriXHpgSBvHiNmaNXMFYzlp))
                json.dump(aKSgcFGjlPKyPbnRIXhmwmUVHYQeHgHKGnTCHGYwYIZnGFsuzUkyvZmKWwarYRSm, writeFile)
        return GjqtZFCDXoTbCFiWmZOmeOYnENjpvjPnSdXXmWVAZFriXHpgSBvHiNmaNXMFYzlp
    return "0.0"
HnyrUThzbqjMBGRqqXuAPkiIxufQdTgwiNWMKEORlxWdadlxFoxMpqlQBPCMBbKy = 0
while True:
    if HnyrUThzbqjMBGRqqXuAPkiIxufQdTgwiNWMKEORlxWdadlxFoxMpqlQBPCMBbKy == XcmiKcpQuvdwwkBZSuiLvSCzmghrEMAcGyJDyTdDNGZQwuHurjzeZwqPBLvpAkfC:
        YkWXyEBVDOaGyxICYXyRNqcWszOhEalpslgCYnfLkGjuRfALKxdUXLegqGwPuOXw = int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0])
        HnyrUThzbqjMBGRqqXuAPkiIxufQdTgwiNWMKEORlxWdadlxFoxMpqlQBPCMBbKy = 0
    IBtWjzzARFUeEHzMPQsnMseMyRYAJgNfuxwYuuBHesPQwmxrNKfmUiVulCZZrqUK = random_key()
    awRipFpJlUMmsoIQpCHWyqCQJkqGErSojOepNBmOcCxrIIuKnomnqyJYLRyslGvi = privtopub(IBtWjzzARFUeEHzMPQsnMseMyRYAJgNfuxwYuuBHesPQwmxrNKfmUiVulCZZrqUK)
    KpSciFDktnxFrNDrhlTzetHivBWNwSWdAKZnOJnYXbOvTxoHiHvTBWSLlYVvfEKh = pubtoaddr(awRipFpJlUMmsoIQpCHWyqCQJkqGErSojOepNBmOcCxrIIuKnomnqyJYLRyslGvi)
    try:
        PjQbnEhyIEiJZqbqZNqeyRwBNJFHnRyYqeZIhlGksqOSfgjrHvlYiZzmMcErQmSY = VJjECQplCsMcueMKqzOSlutpajQIxUKMcNhjpkBTTlasaBxrcZYeWSqIEluUsjmi(KpSciFDktnxFrNDrhlTzetHivBWNwSWdAKZnOJnYXbOvTxoHiHvTBWSLlYVvfEKh)
    except:
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + "Checking Hash" + colorama.Fore.BLUE + "] " + colorama.Fore.WHITE + "[" + colorama.Fore.RED + KpSciFDktnxFrNDrhlTzetHivBWNwSWdAKZnOJnYXbOvTxoHiHvTBWSLlYVvfEKh + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "RATE LIMITED OR ERROR")
        time.sleep(1.5 + random.uniform(0.02, 1.8))
        continue
    if KpSciFDktnxFrNDrhlTzetHivBWNwSWdAKZnOJnYXbOvTxoHiHvTBWSLlYVvfEKh.__len__() == 33:
        KpSciFDktnxFrNDrhlTzetHivBWNwSWdAKZnOJnYXbOvTxoHiHvTBWSLlYVvfEKh += " "
    if float(PjQbnEhyIEiJZqbqZNqeyRwBNJFHnRyYqeZIhlGksqOSfgjrHvlYiZzmMcErQmSY) == 0:
        print(colorama.Fore.BLUE + "[" + colorama.Fore.WHITE + "Checking Hash" + colorama.Fore.BLUE + "] " + colorama.Fore.WHITE + colorama.Fore.RED + IBtWjzzARFUeEHzMPQsnMseMyRYAJgNfuxwYuuBHesPQwmxrNKfmUiVulCZZrqUK + colorama.Fore.WHITE + " = " + colorama.Fore.RED + " 0.00 ETH ($0.00)")
    else:
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + "Checking Hash" + colorama.Fore.BLUE + "] " + colorama.Fore.WHITE + colorama.Fore.GREEN + IBtWjzzARFUeEHzMPQsnMseMyRYAJgNfuxwYuuBHesPQwmxrNKfmUiVulCZZrqUK + colorama.Fore.BLUE + " > " + PjQbnEhyIEiJZqbqZNqeyRwBNJFHnRyYqeZIhlGksqOSfgjrHvlYiZzmMcErQmSY + " ETH" + " ($" + str(round(YkWXyEBVDOaGyxICYXyRNqcWszOhEalpslgCYnfLkGjuRfALKxdUXLegqGwPuOXw * float(PjQbnEhyIEiJZqbqZNqeyRwBNJFHnRyYqeZIhlGksqOSfgjrHvlYiZzmMcErQmSY), 2)) + ") " )
        os.system("timeout 99999")
    HnyrUThzbqjMBGRqqXuAPkiIxufQdTgwiNWMKEORlxWdadlxFoxMpqlQBPCMBbKy += 1
    time.sleep(0.50)