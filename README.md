# LIFX_Ambient_Light
A simple program designed to discover my LIFX Desk Light, and change the color based on the average color of my primary display.

Uses lifxlan library and PIL.

Works by first detecting my light and then connecting to it. After connecting, the script takes a screenshot and condenses it to 1 pixel, allowing for the average color to be shown. I then used converted the color from RGB to HSBK, and then sent the color to my light to be updated. The process is repeated every 3/4 of a second, allowing for an almost real time Ambient light.
