import os
import pygame
import time
import random
from font import ProtoFont
from PIL import Image


FA_LEFT = "fa_left"
FA_MIDDLE = "fa_middle"
FA_RIGHT = "fa_right"
FA_TOP = "fa_top"
FA_BOTTOM = "fa_bottom"

ALIGN = {
    "fa_left": lambda size: 0,
    "fa_right": lambda size: -size,
    "fa_middle": lambda size: -int(size/2),
    "fa_top": lambda size: 0,
    "fa_right": lambda size: -size,
    "fa_middle": lambda size: -int(size/2)
    }

    
class Scope :
    screen = None
    
    def __init__(self, testmode):
        self.halign = FA_LEFT
        self.valign = FA_TOP
        
        if not testmode:
            os.putenv('SDL_FBDEV', '/dev/fb1')
            
            drivers = ['fbcon', 'directfb', 'svgalib']
            found = False
            for driver in drivers:
                # Make sure that SDL_VIDEODRIVER is set
                if not os.getenv('SDL_VIDEODRIVER'):
                    os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    print(f'Driver: {driver} failed.')
                    continue
                found = True
                break
        
            if not found:
                raise Exception('No suitable video driver found!')
        
            size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            print(f"Framebuffer size: {size[0]} x {size[1]}")
            self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        else:
            self.screen = pygame.display.set_mode((480, 320))
            
        pygame.display.update()
 
    def __del__(self):
        pygame.quit()

    @staticmethod
    def numfmt(raw):
        return int(round(raw))
    
    def update(self):
        pygame.display.update()

    def draw_pixel(self, coor, col):
        self.screen.set_at(tuple(self.numfmt(i) for i in coor), col)

    def draw_set_halign(self, mode):
        self.halign = mode

    def draw_set_valign(self, mode):
        self.valign = mode
        
    def draw_text(self, x, y, size, text):
        text = str(text)
        
        x_align = ALIGN[self.halign](self.get_text_width(size, text))
        y_align = ALIGN[self.valign](self.get_text_height(size))
        
        char_space = size * 5 + max(1, size - 2)

        for char in range(len(text)):
            for yi in range(5):
                for xi in range(5):
                    if ProtoFont[text[char].upper()][yi*5+xi] == "1":
                        self.draw_rectangle(x + x_align + (char * char_space) + (xi * size),
                                            y + y_align + (yi * size),
                                            x + x_align + (char * char_space) + ((xi + 1) * size),
                                            y + y_align + ((yi + 1) * size),
                                            (0, 0, 0))

    def draw_image(self, x, y, imgpath):
        img = Image.open(imgpath)
        img = img.convert("RGBA")
        pix = img.load()

        for yi in range(img.size[1]):
            for xi in range(img.size[0]):
                r, g, b, *a = pix[(xi, yi)]
                if a != [0]:
                    self.draw_pixel((x+xi, y+yi), (r, g, b))

        img.close()

    def draw_rectangle(self, x1, y1, x2, y2, col):
        for y in range(self.numfmt(y1), self.numfmt(y2)):
            for x in range(self.numfmt(x1), self.numfmt(x2)):
                self.draw_pixel((x, y), col)

    def get_text_width(self, size, text):
        char_space = size * 5 + max(1, size - 2)

        return (len(text) - 1) * char_space + 5 * size

    def get_text_height(self, size):
        return 5 * size


if __name__ == "__main__":
    s = Scope(True)
    s.draw_rectangle(0, 0, 480, 320, (0, 100, 0))

    text = "test string"
    tests = [10, 20, 40, 60, 100, 140]

    for i, test in enumerate(tests):
        s.draw_rectangle(10, test,
                         10 + s.get_text_width(i, text),
                         test + s.get_text_height(i),
                         (0, 200 ,0))
        
        s.draw_text(10, test, i, text)

    s.draw_set_halign(FA_MIDDLE)
    s.draw_set_valign(FA_MIDDLE)
    s.draw_pixel((200, 170), (255, 0, 0))
    s.draw_pixel((300, 200), (255, 0, 0))
    s.draw_text(200, 200, 3, text)
    s.update()

    
