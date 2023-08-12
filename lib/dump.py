import datetime
from pystyle import *
from colorama import Fore, Back, Style
from ventus import *
from phlib import PornHub
import time


class Banner():
    def banner():
        date = datetime.datetime.now()
        print(Center.XCenter(f"""{Fore.LIGHTMAGENTA_EX}
            ⣀⣠⣤⣶⣶⣾⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣷⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⡴⠾⠟⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠷⢦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠋⠁⠀⠀⢀⣀⣤⣶⣖⣒⣒⡲⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⢖⣒⣒⣲⣶⣤⣀⡀⠀⠀⠈⠙⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⢖⣫⣷⣿⣿⣿⣿⣿⣿⣶⣤⡙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢋⣤⣾⣿⣿⣿⣿⣿⣿⣾⣝⡲⣄⠀⠀⠀⠀⠀⠀⠀        {Fore.MAGENTA}[Author: BabyDoll]{Fore.LIGHTMAGENTA_EX}
⠀⠀⠀⣄⣀⣠⢿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠻⢿⣿⣿⣦⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣟⣴⣿⣿⡿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⡻⣄⣀⣤⠀⠀⠀   {Fore.MAGENTA}[date: {date}]{Fore.LIGHTMAGENTA_EX}
⠀⠀⠀⠈⠟⣿⣿⣿⡿⢻⣿⣿⣿⠃⠀⠀⠀⠀⠙⣿⣿⣿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣿⣿⣿⠋⠀⠀⠀⠀⠘⣿⣿⣿⡟⢿⣿⣿⣟⠻⠁⠀⠀⠀    {Fore.MAGENTA}[PornHub Dump]{Fore.LIGHTMAGENTA_EX}
⠤⣤⣶⣶⣿⣿⣿⡟⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡏⠀⠀⠀⠀⠀⠀⣹⣿⣿⣷⠈⢻⣿⣿⣿⣶⣦⣤⠤
⠀⠀⠀⠀⠀⢻⣟⠀⠀⣿⣿⣿⣿⡀⠀⠀⠀⠀⢀⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⡀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠀⠀⣿⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣆⠀⢹⣿⠟⢿⣿⣦⣤⣤⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡿⢷⣤⣤⣤⣴⣿⣿⣿⣿⡇⠀⣰⠟⠀⠀⠀⠀⠀⠀{Fore.MAGENTA}[Discord: https://discord.gg/fRyxsYtK7C]{Fore.LIGHTMAGENTA_EX}
⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠙⢀⣀⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠁⠀⣻⣿⣿⣿⣿⣿⣿⠏⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡈⠻⠿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⠿⠛⢁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⣶⣦⣤⣤⣤⡤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢤⣤⣤⣤⣶⣾⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                                                                    {Fore.RESET}"""))




class Google:
    def Pornhub():
        try:
            
            query = input(f"{Fore.LIGHTMAGENTA_EX}Insert People Name or Category: {Fore.RESET}")
            ph = PornHub()
            ph.categories
            ph[query]
            results = ph.search(query,max=500)
            for p in results:
                time.sleep(1)
                print(f"[PORNHUB]: NAME: {Fore.LIGHTMAGENTA_EX}{p.title}{Fore.RESET} URL: {Fore.LIGHTMAGENTA_EX}{p.url}{Fore.RESET}")
            print(f"{Fore.LIGHTMAGENTA_EX}--------------------------------------{Fore.RESET}")
        
        except Exception as a:
            print(f"{Fore.RED}Does not exist{Fore.RESET}")