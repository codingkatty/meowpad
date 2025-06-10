import board
import displayio
import adafruit_displayio_ssd1306
import busio
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D1, board.D2, board.D4, board.D3]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# for games :3
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D]
]

displayio.release_displays()

# no clue how to do this one
i2c = busio.I2C(board.GP7, board.GP6)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

splash = displayio.Group()
cat00 = displayio.OnDiskBitmap("firmware/00cat.bmp")
catuwu = displayio.OnDiskBitmap("firmware/uwucat.bmp")

cat_sprite = displayio.TileGrid(
    cat00,
    pixel_shader=cat00.pixel_shader,
    width=4,
    height=1,
    tile_width=128,
    tile_height=32,
    x=0,
    y=0
)

splash.append(cat_sprite)
display.show(splash)

pixels = neopixel.NeoPixel(board.GP29, 1)
pixels[0] = (204, 153, 255)

if __name__ == '__main__':
    keyboard.go()

while True:
    if keyboard.keys:
        cat_sprite.bitmap = catuwu
    else:
        cat_sprite.bitmap = cat00