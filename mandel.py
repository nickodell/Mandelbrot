from PIL import Image
from PIL import ImageDraw
import cmath

WIDTH = 1920
HEIGHT = 1080

def mandel(c):
    z = 0
    for h in xrange(20):
        z = z**2 + c
        if abs(z) > 2:
            break
    if abs(z) >= 2:
        return False, h
    else:
        return True, h
    
def sin_fract(c):
    z = 0
    try:
        for h in xrange(20):
            z = cmath.sin(z)/(z**2) + c
            if abs(z) > 10:
                break
    except ZeroDivisionError:
        pass
    if abs(z) >= 10:
        return False, z
    else:
        return True, z

def iteration_to_color(it):
    return (255-it * 10, 255-it * 5, 255-it * 5)

#Returns a function remaping an old range to a new one
def remap(o1, o2, n1, n2):
    old_range = o1 - o2
    new_range = n1 - n2
    mult = new_range/old_range
    return lambda arg: (arg - o1) * mult + n1

im = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
pix = im.load()
draw = ImageDraw.Draw(im)

# Mandelbrot remaps
xmap = remap(0, WIDTH, -2.0, 1.5)
ymap = remap(0, HEIGHT, -1.5, 1.5)

# sin fractal remaps
#xmap = remap(0, WIDTH, -1000, 1000)
#ymap = remap(0, HEIGHT, -1000, 1000)

for x in xrange(WIDTH):
    real = xmap(x)
    for y in range(HEIGHT):
        img = ymap(y)
        c = complex(real, img)
        part_of_set, h = mandel(c)
        if not part_of_set:
            pix[x, y] = iteration_to_color(h)
        else:
            pix[x, y] = (0,0,0)
print "Rendered, saving..."
im.save("out.bmp")
print "Done."
