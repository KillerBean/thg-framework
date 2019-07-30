import distro
from os import system
from colorama import Fore
import apt,sys
def deb_ubu():
    #lista de programas
    listt= ['fish',"postgresql","nmap","postgresql-all",'postgresql-contrib']
    #procura no cache
    cache = apt.cache.Cache()
    #atualiza o cache
    cache.update()
    cache.open()
    banner = '''
████████╗██╗  ██╗ ██████╗       ██╗   ██╗██████╗ ██╗   ██╗███╗   ██╗████████╗██╗   ██╗      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
╚══██╔══╝██║  ██║██╔════╝       ██║   ██║██╔══██╗██║   ██║████╗  ██║╚══██╔══╝██║   ██║      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
   ██║   ███████║██║  ███╗█████╗██║   ██║██████╔╝██║   ██║██╔██╗ ██║   ██║   ██║   ██║█████╗██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
   ██║   ██╔══██║██║   ██║╚════╝██║   ██║██╔══██╗██║   ██║██║╚██╗██║   ██║   ██║   ██║╚════╝██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
   ██║   ██║  ██║╚██████╔╝      ╚██████╔╝██████╔╝╚██████╔╝██║ ╚████║   ██║   ╚██████╔╝      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝    ╚═════╝       ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                                                                  
    '''
    print(Fore.BLUE+banner)
    #faz o check dos programas
    for i in listt:
        pkg = cache[i]
        if pkg.is_installed:
            print("{colorp}{i} =>{color} already installed".format(colorp=Fore.RED,color=Fore.CYAN,i=i))
        else:
            #instala
            print(pkg.mark_install())
        try:
            cache.commit()
        except Exception as  arg:
            print("Sorry, package installation failed [{err}]".format(err=str(arg)))

def check():
    linux = distro.linux_distribution()[0]
    if linux == "ubuntu" or "debian":
        deb_ubu()

check()