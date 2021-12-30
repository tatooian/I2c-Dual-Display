import machine
from sh1106 import SH1106_I2C
import ssd1306

i2c0Clk = machine.Pin(9)  # brown 11
i2c0Da = machine.Pin(8)  # blue 12
i2c0 = machine.I2C(0, sda=i2c0Da, scl=i2c0Clk, freq=400000)

print('Scan i2c 0 bus...')
devices = i2c0.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:', len(devices))

    for device in devices:
        print("Decimal address: ", device, " | Hexa address: ", hex(device))

i2c1Clk = machine.Pin(27)  # orange 32
i2c1Da = machine.Pin(26)  # yellow 31
i2c1 = machine.I2C(1, sda=i2c1Da, scl=i2c1Clk, freq=400000)

print('Scan i2c 1 bus...')
devices = i2c1.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:', len(devices))

    for device in devices:
        print("Decimal address: ", device, " | Hexa address: ", hex(device))

#128 x 32
display0 = ssd1306.SSD1306_I2C(128, 32, i2c0, 0x3C)
display0.fill(1)
display0.text("display 0", 0, 0, 0)
display0.show()

display1 = SH1106_I2C(128, 64, i2c1, None, 0x3C, rotate=180)
display1.fill(1)
display1.text("display 1", 0, 0, 0)
display1.show()
