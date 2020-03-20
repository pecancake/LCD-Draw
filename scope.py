import os
import pygame
import time
import random
from font import ProtoFont
from PIL import Image

class Scope :
    screen = None
    
    def __init__(self, testmode):
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

    def update(self):
        pygame.display.update()

    def draw_pixel(self, coor, col):
        self.screen.set_at(coor, col)
        
    def draw_text(self, x, y, size, text):
        frag_size = size
        char_space = frag_size * 5 + max(1, frag_size - 2)

        for char in range(len(text)):
            for yi in range(5):
                for xi in range(5):
                    if ProtoFont[text[char].upper()][yi*5+xi] == "1":
                        self.draw_rectangle(x + (char * char_space) + (xi * frag_size),
                                            y + (yi * frag_size),
                                            x + (char * char_space) + ((xi + 1) * frag_size),
                                            y + ((yi + 1) * frag_size),
                                            (0, 0, 0))

    def draw_image(self, x, y, imgpath):
        img = Image.open(imgpath)
        pix = img.load()

        for yi in range(img.size[1]):
            for xi in range(img.size[0]):
                r, g, b, *a = pix[(xi, yi)]
                if a != [0]:
                    self.draw_pixel((x+xi, y+yi), (r, g, b))

        img.close()

    def draw_rectangle(self, x1, y1, x2, y2, col):
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.draw_pixel((x, y), col)

    def get_text_width(self, size, text):
        char_space = size * 5 + max(1, size - 2)

        return len(text) * char_space + 6 * size

