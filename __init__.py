from scope import Scope
import time

def draw_square(scope, x1, y1, x2, y2, col):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            scope.draw_pixel((x, y), col)
try:  
    s = Scope()
    
    draw_square(s, 50, 50, 100, 100, (0, 255, 0))
    draw_square(s, 75, 75, 125, 125, (0, 0, 255))
    draw_square(s, 100, 100, 150, 150, (255, 0, 0))

    s.update()
    time.sleep(5)
    print("done")

except Exception as e:
    print(e)
