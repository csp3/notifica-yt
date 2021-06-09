import requests
from bs4 import BeautifulSoup
import re
import time 
import os 
import sys 

### solo por cantidad de videos, no por titulo de video que es lo correcto 
####################
listacan = [
    'Code, Tech, and Tutorials',
    'TAB Nation - AutoHotkey',
    'Jacob Sorber',
    'BOOKFILFACE',
    'Leifer Mendez'
    ]

listaurl = [
    'https://www.youtube.com/results?search_query=Code%2C+Tech%2C+and+Tutorials',
    'https://www.youtube.com/results?search_query=tab+nation+-+auto',
    'https://www.youtube.com/results?search_query=Jacob+Sorber',
    'https://www.youtube.com/results?search_query=BOOKFILFACE',
    'https://www.youtube.com/results?search_query=Leifer+Mendez'
    ]

listavid = [242, 90, 182, 38, 103]


###################
avance = 0
while avance <= len(listavid): 
    r = requests.get(listaurl[avance])
    p = r.text 
    soup = BeautifulSoup(r.text, "lxml")

    patron = re.compile(r'"videoCountText"\:\{"runs"\:\[\{"text"\:\"')
    #patron = re.compile(r'("label"\:"[a-zA-Z0-9¾n±\-,áéíóúÁÉÍÓÚñÑ ]*"\})')

    match = patron.search(r.text) 

    fin = match.span()[1] 

    numvideos = ""
    i = 0
    while 1:
        if (p[fin+i] == '0' or p[fin+i] == '1' or p[fin+i] == '2' or 
        p[fin+i] == '3' or p[fin+i] == '4' or p[fin+i] == '5' or p[fin+i] == '6' or 
        p[fin+i] == '7' or p[fin+i] == '8' or p[fin+i] == '9' or p[fin+i] == '10'):
            numvideos += p[fin + i]
            i+=1
        else:
            break 
    
    print(" ")
    print("------ ",listacan[avance]," ------")
    if int(numvideos) == int(listavid[avance]):
        print("permanece igual")
    else:
        if int(numvideos) > int(listavid[avance]):
            print("Se agrego videos")
        else:
            print("Se han quitado videos")
            listavid[avance] = int(numvideos)

    print("numero videos: ", numvideos) 
    time.sleep(7) #15 minutos
    
    avance+=1

    if avance == 5:
        avance = 0
        if sys.platform == 'win32':
            os.system('cls')
            
        if sys.platform == 'linux':
            os.system('clear')
