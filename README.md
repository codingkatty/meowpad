# meowpad
this is a macropad made for [hackpad](https://hackpad.hackclub.com/) / [highway](https://highway.hackclub.com/)! i followed the guide in hackpad to make the macropad. the macropad features 4 keys to type, an oled and a neopixel. the keys are for wasd because apparently i don't have much ideas, may as well use it for gaming!

![meowpad](https://github.com/user-attachments/assets/6cd59e9b-deb9-4e98-9e4a-2f876e041948)

### from pcb
here are the schematic and pcb pictures, this is the first time i used kicad and it was really easy to use, esspecially with the help of the guide.

![image](https://github.com/user-attachments/assets/df957d69-7eb4-47a4-be30-d359f82a0674)
![image](https://github.com/user-attachments/assets/ef5e0778-b021-442e-850c-801ee4fb136c)


### to case
i made the case in fusion360, it was my first time using it and i was pretty slow, took pretty long ~4 hours (at least longer than i expected it to take). there's a little translucent part for the neopixel, not sure exactly how would i make it tho i plan to print it with my translucent purple filament.

![image](https://github.com/user-attachments/assets/80ded525-0a7f-439f-8cf6-b38a3eb6db45)
![image](https://github.com/user-attachments/assets/cc5c08f2-d852-48c3-8883-08bd7dc3449b)

### and code
i have modified the code in the guide and added a few stuff for neopixel and the oled. for some, I wasn't able to find some answers online so I think I will fix it when i maybe get it. Right now the code written is really simple, what it (is supposed to do) does is to type wasd, neopixel shows purple and oled is a rainbow coloured (highway reference :3) cat thing that changes when typing.

<img src="firmware/00cat.bmp"> <img src="firmware/uwucat.bmp">

(i hope it works / i may or may not need to rotate the image)

> checkout `firmware/test.py` for what i want to make for the oled, (you can run it on your pc!)

### (& bom)
- Seeed XIAO RP2040 - x1
- MX-Style switches - x4
- 0.91 inch OLED displays - x1
- Blank DSA keycaps (White) - x4
- SK6812 MINI-E LEDs - x1
- M3x16mm screws - x6
- M3x5mx4mm heatset inserts - x6

---
in the future when its built imma tinker around with it- i'll try to make it able to type! hehe
