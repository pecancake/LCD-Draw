from scope import Scope
from font import ProtoFont
import time
import traceback
import colorsys


def draw_text(scope, x, y, text):
    with open("text", 'w') as f:
        for char in range(len(text)):
            for yi in range(5):
                for xi in range(5):
                    if ProtoFont[text[char].upper()][yi*5+xi] == "1":
                        f.write(f"writing {text[char]} to {x+char*5+xi}, {y+yi}")
                        draw_square(scope, x+char*6+xi, y+yi, x+char*6+xi, y+yi, (0,0,0))

        
def draw_square(scope, x1, y1, x2, y2, col):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            scope.draw_pixel((x, y), col)


def col_test(scope):
    for h in range(0, 320+1):
        for s in [1]:
            for v in range(0, 480+1):
                scope.draw_pixel((v, h), tuple(i*255 for i in colorsys.hsv_to_rgb(h/320, s/1, v/480)))


def timefunc(func, args):
    start = time.time()
    func(*args)
    end = time.time()

    with open("runtime", "w") as f:
        f.write(f"\nTime it took for '{func.__name__}' to finish:\n{round(end-start, 4)} seconds\n\n")

    
err = "No error!\n"

try:  
    s = Scope()
    
    #timefunc(col_test, (s,))
    draw_text(s, 30, 30, "This is a test string ~")
    s.update()
    time.sleep(3)
    
    print("done")

except Exception:
    err = traceback.format_exc()

with open("error", "w") as f:
    f.write(f'\n{err}\n')
    
