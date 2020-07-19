import colorsys
import time
from datetime import datetime

from lifxlan import LifxLAN, RGBtoHSBK
from PIL import Image, ImageGrab
from plyer import notification

lifx = LifxLAN()
light = lifx.get_device_by_name("Desk")
print(f"Selected {light.get_label()}")
sample_size = 1, 1

def ambient_light(light):
    while True:
        try:
            screenshot = ImageGrab.grab(include_layered_windows=True)
            scaled = screenshot.resize(sample_size)
            color = scaled.getpixel((0, 0))
            color = RGBtoHSBK(color, temperature=5000)
            color = color
            light.set_color(color, duration=1000)
            time.sleep(0.75)
        except Exception as e:
            notification.notify(
                title = 'An error occured!',
                message = f'{e}',
                app_name = 'Ambient Light',
                app_icon = r"C:\Users\Matt\Desktop\Shortcuts\Coding\.py\AmbientLight\icon.ico"
            )
            print(f"An error occured, retrying in 5 seconds: {e}")
            time.sleep(5)

ambient_light(light)
