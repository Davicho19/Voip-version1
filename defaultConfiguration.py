#!/usr/bin/env python
import os

os.system("clear")
os.system("sudo echo" ">/etc/asterisk/sip.conf")

print("En este momento se le esta ajustado las configuraciones necesarias")

setting=open("/etc/asterisk/sip.conf", "a+")
setting.write("[general]\nallowguest=no\nsrvlookup=no\nudpbindaddr=0.0.0.0\ntcpenable=no\ncanreinvite=no\ndtmfmode=auto\n\n[ramal-voip](!)\ntype=friend\ncontext=INTERNO\nhost=dynamic\ndisallow=all\nallow=ulaw\nallow=alaw\nallow=g729\n\n[100](ramal-voip)\nsecret=123456789\n[200](ramal-voip)\nsecret=123456789")
setting.close()

#agregar la extension en el archivo /etc/asterisk/extensions.conf

os.system("sudo echo" ">/etc/asterisk/extensions.conf")
extend=open("/etc/asterisk/extensions.conf", "a+")
extend.write("[general]\n\n[INTERNO]\n;\n;RAMAL 100\nexten => 100,1,Dial(SIP/100)\n;\n;RAMAL 200\nexten => 200,1,Dial(SIP/200)\n\nexten => 300,1,Answer()\nexten => 300,2,Playback(hello-world)\nexten => 300,3,Hangup()")
extend.close()
os.system("sudo systemctl restart asterisk")
#nota
os.system("clear")

print("Se le han ajustado las configuraciones necesarias para este directorio /etc/asterisk/sip.conf")
print("al igual que en este /etc/asterisk/extensions.conf")
print("las extensiones creadas son 100, 200, ambas copassword 123456789")
