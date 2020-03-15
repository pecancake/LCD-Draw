from scope import Scope
import time

def draw_square(scope, x1, y1, x2, y2, col):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            scope.draw_pixel((x, y), col)

def col_test(scope):
    # create a generator for pixel choices
    gen = ((x, y) for y in range(320) for x in range(480))
    
    for r in range(0, 255, 10):
        for g in range(0, 255, 10):
            for b in range(0, 255, 10):
                scope.draw_pixel(next(gen), (r, g, b))
                
try:  
    s = Scope()
    
    col_test(s)

    s.update()
    time.sleep(5)
    print("done")

except Exception as e:
    print(e)
