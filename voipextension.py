#!/usr/bin/env python
import os

os.system("clear")
#ingresando una extension
print("Bienvenido por favor ingrese la extension que gusta agregar")
extension=input()

print("ingrese su password que guste /nota deve ser mayor de 9 caracteres")
password=input()
#directory="/etc/asterisk/sip.conf"
os.system("clear")

adding=open("/etc/asterisk/sip.conf", "a+")
adding.write("\n["+extension+"](ramal-void)\nsecret="+password)
adding.close()

#agregar la extension en el archivo /etc/asterisk/extensions.conf

file=open("/etc/asterisk/extensions.conf", "a+")
file.write("\nexten => "+extension+",1,Dial(SIP/"+extension+")")
file.close()
os.system("sudo systemctl restart asterisk")
#nota
os.system("clear")
print("su extension a sido agregada en el archivo /etc/asterisk/sip.conf")
print("sus ajustes tambien estan /etc/asterisk/extensions.conf")

