from scope import Scope
import time

def draw_square(scope, x1, y1, x2, y2, col):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            scope.draw_pixel((x, y), col)

def col_test(scope, chunk):
    """ Prerequsite: chunk can cleanly divide 320 and 480. """
    # create a generator for pixel choices
    gen = ((x*chunk, y*chunk) for x in range(52) for y in range(26))
    
    for r in range(0, 255, 10):
        for g in range(0, 255, 10):
            for b in range(0, 255, 10):
                coor = next(gen)
                draw_square(coor[0], coor[1],
                            coor[0]+chunk, coor[1]+chunk,
                            (r, g, b)
                
try:  
    s = Scope()
    
    col_test(s, 2)

    s.update()
    time.sleep(5)
    print("done")

except Exception as e:
    print(e)
