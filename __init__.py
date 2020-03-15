from scope import Scope

try:
    
    s = Scope()

    for y in range(100):
        for x in range(100):
            s.draw_pixel((100+x, 100+y), (0, 255, 0))

    s.update()
    time.sleep(2)
    print("done")

except Exception as e:
    print(e)
