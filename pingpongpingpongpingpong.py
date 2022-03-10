import os
import shutil

os.system('title made by bazooka#0001')

os.system('mode con: cols=80 lines=22')

os.system("cls" if os.name == "nt" else "clear")
def purple(text):
    os.system("")
    faded = ""
    down = False
    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded
banner0 = """█       ▄   ▄█▄    ▄█ ▄████  ▄███▄   █▄▄▄▄ """
banner1 = """█        █  █▀ ▀▄  ██ █▀   ▀ █▀   ▀  █  ▄▀ """
banner2 = """█     █   █ █   ▀  ██ █▀▀    ██▄▄    █▀▀▌  """
banner3 = """███▄  █   █ █▄  ▄▀ ▐█ █      █▄   ▄▀ █  █  """
banner4 = """    ▀ █▄ ▄█ ▀███▀   ▐  █     ▀███▀     █   """
banner5 = """       ▀▀▀              ▀             ▀    """

fullbanner = """
█       ▄   ▄█▄    ▄█ ▄████  ▄███▄   █▄▄▄▄ 
█        █  █▀ ▀▄  ██ █▀   ▀ █▀   ▀  █  ▄▀ 
█     █   █ █   ▀  ██ █▀▀    ██▄▄    █▀▀▌  
███▄  █   █ █▄  ▄▀ ▐█ █      █▄   ▄▀ █  █  
    ▀ █▄ ▄█ ▀███▀   ▐  █     ▀███▀     █   
       ▀▀▀              ▀             ▀    
"""
smop = "-t"

def center(x):
    columns = shutil.get_terminal_size().columns
    print(purple(x.center(columns)))

def banner():
    print()
    center(banner0)
    center(banner1)
    center(banner2)
    center(banner3)
    center(banner4)
    center(banner5)
    print()
    print()
    print()
banner()

ip = ('                                 Skids IP => ')
ip = input(purple(ip))

os.system('title ping pong ping pong ping pong ping pong ping pong ping pong ping')

os.system(f'ping {ip} {smop}')