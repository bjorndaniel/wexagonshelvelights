# Wexagon shelve lights
A micropython server for [Weksters](https://www.patreon.com/wekster/posts) wexagon shelves and his minidudes.

Parts used:
* Wemos D1 mini
* 0.96" IIC Oled display (SSD1306)
* D-SUN 3A STEP DOWN SWITCHING VOLTAGE REGULATOR
* 54 WS2812 Leds

Enclosed is the source code and the .stl's for the electronics box and the led holders. For the shelves please refer to Weksters patreon site.
The leds should be wired from bottom left (seen from the front). Each shelve has 3 WS2812 leds.

On first run the Wemos will start up in AP-mode with the SSID WexagonLights, password M1n1Dud3 and IP 192.168.4.1. Connect and then open a browser and you will be able to connect to a WIFI, which will then be saved.
