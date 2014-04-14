#!/usr/bin/python

LIRC_DEVICE = "NEC"

import sys
import time

sys.path.append("lirc-python/")
import lirc

RED = [50, 0, 0, 0]
GREEN = [0, 50, 0, 0]
BLUE = [0, 0, 50, 0]

PRETTY = [25, 12, 50, 10]

class LEDFixture:
    def __init__(self, initialize = False):
        self.ir = lirc.Lirc()

        if initialize:
            self.initialize()

        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 0

        self.dark()

    def toPreset(self, preset):
        self.ir.send_once(preset)
        
    def dark(self):
        self.ir.send_once(LIRC_DEVICE, "codeM4Custom")
        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 0

    def fullBright(sef):
        pass

    def setPreset(self, preset):
        print "set preset", preset
        self.ir.send_start(LIRC_DEVICE, preset)
        time.sleep(5)
        self.ir.send_stop(LIRC_DEVICE, preset)

    def initialize(self):
        """Record some presets"""

        self.ir.send_once("NEC", "codeFullSpec")
        time.sleep(0.1)
        # go dark
        for colorDown in ["codeWhiteDown", "codeRedDown", "codeBlueDown", "codeGreenDown"]:
            print "sending", colorDown
            for x in range(64):
                self.ir.send_once(LIRC_DEVICE, colorDown)
            time.sleep(0.1)

        # record dark as M4
        self.dark()
        self.setPreset("codeM4Custom")

    def toColor(self, newR, newG, newB, newW):
        while (self.r != newR) or \
              (self.g != newG) or \
              (self.b != newB) or \
              (self.w != newW):
            print "current color", [self.r, self.g, self.b, self.w]
            print "target color", [newR, newG, newB, newW]
            if self.r > newR:
                led.ir.send_once(LIRC_DEVICE, "codeRedDown")
                self.r -= 1
            elif self.r < newR:
                led.ir.send_once(LIRC_DEVICE, "codeRedUp")
                self.r += 1

            if self.g > newG:
                led.ir.send_once(LIRC_DEVICE, "codeGreenDown")
                self.g -= 1
            elif self.g < newG:
                led.ir.send_once(LIRC_DEVICE, "codeGreenUp")
                self.g += 1

            if self.b > newB:
                led.ir.send_once(LIRC_DEVICE, "codeBlueDown")
                self.b -= 1
            elif self.b < newB:
                led.ir.send_once(LIRC_DEVICE, "codeBlueUp")
                self.b += 1

            if self.w > newW:
                led.ir.send_once(LIRC_DEVICE, "codeWhiteDown")
                self.w -= 1
            elif self.w < newW:
                led.ir.send_once(LIRC_DEVICE, "codeWhiteUp")
                self.w += 1




if __name__ == "__main__":
    led = LEDFixture(initialize = False)
    time.sleep(2)

    led.toColor(*RED)
    led.toColor(*GREEN)
    led.toColor(*BLUE)
    led.toColor(*PRETTY)