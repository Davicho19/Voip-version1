#!/usr/bin/env python
import os

os.system("clear")
#ingresando una extension
print("Bienvenido por favor ingrese el nombre de la troncal")
print("ejmplo trunkempresaB")
empresa=input()

print("ingrese su la direccion ip del servidor remoto")
ip=input()
#directory="/etc/asterisk/sip.conf"
os.system("clear")

trunk=open("/etc/asterisk/sip.conf", "a+")
trunk.write("\n["+empresa+"]\ntype=peer\nhost="+ip+"\ncontext=INTERNO\nallow=ulaw\nallow=alaw\ndtmfmode=info")
trunk.close()

os.system("sudo clear")
#agregar la extension en el archivo /etc/asterisk/extensions.conf
print("ingrese el rango del que puede llamar ejemplo /1XXXX")
rango=input()
interno=open("/etc/asterisk/extensions.conf", "a+")
interno.write("\nexten => "+rango+",1,Dial(SIP/${EXTEN}@"+empresa+")")
interno.close()
os.system("sudo systemctl restart asterisk")
#nota
os.system("clear")
print("su troncal ha sido ajustada en /etc/asterisk/sip.conf")
print("sus ajustes extras estan /etc/asterisk/extensions.conf")

