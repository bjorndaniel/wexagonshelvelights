from machine import Pin
import neopixel
import time
np = neopixel.NeoPixel(Pin(2), 54)  # 2==D4


def test():
    print('Turning on lights')
    np[0] = (64, 0, 0)  # set to red, full brightness
    np[1] = (0, 65, 0)  # set to green, half brightness
    np[2] = (0, 0, 64)
    np.write()


def light(nr, color):
    start = nr * 3
    np[start] = color
    np[start+1] = color
    np[start+2] = color
    np.write()


def all(color):
    for i in range(54):
        np[i] = color
    np.write()


def shut_off():
    for i in range(53):
        np[i] = (0, 0, 0)
    np.write()


def demo():
    print('starting lights demo')
    n = np.n

    # # cycle
    # for i in range(4 * n):
    #     for j in range(n):
    #         np[j] = (0, 0, 0)
    #     np[i % n] = (255, 255, 255)
    #     np.write()
    #     time.sleep_ms(25)

    # # bounce
    # for i in range(4 * n):
    #     for j in range(n):
    #         np[j] = (0, 0, 128)
    #     if (i // n) % 2 == 0:
    #         np[i % n] = (0, 0, 0)
    #     else:
    #         np[n - 1 - (i % n)] = (0, 0, 0)
    #     np.write()
    #     time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
