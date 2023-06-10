# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_stts22h import stts22h

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
stts = stts22h.STTS22H(i2c)

while True:
    temp = stts.temperature
    print("Temperature :{:.2f}C".format(temp))
    time.sleep(0.5)
