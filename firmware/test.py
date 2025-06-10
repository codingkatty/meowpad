import displayio
import keyboard
from blinka_displayio_pygamedisplay import PyGameDisplay

display = PyGameDisplay(width=128, height=32)
splash = displayio.Group()
display.show(splash)

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

while True:
    if display.check_quit():
        break

    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        cat_sprite.bitmap = catuwu
    else:
        cat_sprite.bitmap = cat00