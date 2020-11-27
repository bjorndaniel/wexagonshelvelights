# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306

# ESP32 Pin assignment
# i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))  # 5==D1 4==D2

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.write_cmd(0xa1)
oled.write_cmd(0xc8)


def printap():
    clear()
    oled.text("AP mode:", 0, 0)
    oled.text("192.168.4.1", 0, 22)
    oled.text("WexagonLights", 0, 37)
    oled.text("M1n1Dud3", 0, 52)
    oled.show()


def print(line1, line2, line3):
    clear()
    oled.text(line1, 0, 0)
    oled.text(line2, 0, 22)
    oled.text(line3, 0, 37)
    oled.show()


def printip(ip):
    clear()
    oled.text(ip, 0, 30)
    oled.show()


def clear():
    oled.fill(0)
    oled.show()
