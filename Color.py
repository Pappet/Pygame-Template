import random

# Color Codes for simpler use

# Use it with:
# Color.Black
# etc.

White = (255,255,255)
Black = (0,0,0)
BlackTransparent = (0,0,0,0)

DarkGray = (128,128,128)
LightGray = (211,211,211)

Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

Yellow = (255,255,0)
Cyan = (0,255,255)
Magenta = (255,0,255)

Brown = (210,105,30)
Purple = (128,0,128)

# Generates a Color
# use it with:
#   Color.GenerateColor(125,255,0)
def GenerateColor(r,g,b):
    return (r,g,b)

def RandomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
