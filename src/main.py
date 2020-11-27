import wifimgr
import lights
import webserver
import display
import time

try:
    import usocket as socket
except:
    import socket
display.print("", "  Lights demo", "")
lights.demo()
display.print("  Wifi connect", "", "")
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D
print(wlan.ifconfig())

print('starting web server')
display.print("         Start", "     Web server", "")

webserver.start(wlan.ifconfig()[0])
