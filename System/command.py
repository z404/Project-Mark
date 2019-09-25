##run commands on the system's shell
l = '''

  _____           _           _     __  __          _____  _  __
 |  __ \         (_)         | |   |  \/  |   /\   |  __ \| |/ /
 | |__) | __ ___  _  ___  ___| |_  | \  / |  /  \  | |__) | ' / 
 |  ___/ '__/ _ \| |/ _ \/ __| __| | |\/| | / /\ \ |  _  /|  <  
 | |   | | | (_) | |  __/ (__| |_  | |  | |/ ____ \| | \ \| . \ 
 |_|   |_|  \___/| |\___|\___|\__| |_|  |_/_/    \_\_|  \_\_|\_\\
                _/ |                                            
               |__/                                             
'''

def get_platform():
    with open("System/preferences.txt","r") as f:
        line = f.readline()
        garbage, platform = line.split('=')
        platform = platform.strip().replace('"','')
        return platform

import os, time
from colorama import init as i, Fore, deinit as di
i(autoreset = True)

pf = get_platform()

def execute(code, params=None):
    #from colorama import init as i, Fore, deinit as di
    #log the code in
    print(code)
    
    if code == 'l' or code == 'logo':
        if pf == "Windows":
            os.system("cls")
        elif pf == "Linux":
            os.system("clear")
        print(Fore.CYAN+l)
        return [0]
    
    elif code == 'cmd' or code == 'terminal' or code == 'command':
        os.system(params)
        return [0]
    
    elif code == 'install':
        try:
            os.system("pip3 install -r requirements.txt")
        except:
            os.system("pip install -r requirements.txt")
        print("Done!")
        time.sleep(2)
        if pf == "Windows":
            os.system("cls")
        elif pf == "Linux":
            os.system("clear")
        return [0]
    
    elif code == 'clear' or code == 'cls':
        if pf == "Windows": os.system('cls')
        elif pf == "Linux": os.system('clear')
        return [0]

    elif code == 'input' or code == 'inp' or code == 'nlp' or code == 'nlpu':
        string = ''
        for i in params:
            string+=i+' '
        string.rstrip(' \n')
        return ['nlpu',string]

    else:
        print(Fore.RED+'Error: Command not recognized')
        return [1]
    
    