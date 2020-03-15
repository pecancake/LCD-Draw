from scope import Scope
import time
import traceback
import colorsys

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
        f.write(f"Time it took for function '{func.__name__}' to finish: {round(end-start, 4)} seconds")
    
err = "No error!\n"

try:  
    s = Scope()
    
    col_test(s)

    s.update()
    time.sleep(3)
    
    print("done")

except Exception:
    err = traceback.format_exc()

with open("error", "w") as f:
    f.write(f'\n{err}\n')
    
