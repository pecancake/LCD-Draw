from PIL import *
from tkinter import *
import tkinter as tk
from api import *

test_player = Player("cumlover69")
test_game = Game({})
test_game.add_player("cumlover69")
test_game.add_player("stacy_loves_cock")
test_game.add_player("penispenispenis")
test_page_draw = Page()
test_page_draw.is_text = False
test_page_text = Page()
test_page_text.is_text = True

# Master game window
root = Tk()
root.attributes('-fullscreen', True)

# Left-panel containing the names of the players

players = Frame(root, bg="red", width="6c")
players.pack(side=LEFT, fill=Y, expand=False)


# Functions to generate player names and option menus

def player_widget(p: Player, parent: Frame):
    widget = Menubutton(parent, text=p.username, padx=60, relief=RAISED)
    widget.pack(fill=X)
    return widget


for p in test_game.players:
    p_display = player_widget(p, players)
    # Creation of the drop-down menu
    p_display.menu = Menu(p_display)
    # TODO: fix menu buttons (they all show the same options when changed for one player)
    p_display['menu'] = p_display.menu
    p_display.menu.add_checkbutton(label='Add to Game')
    p_display.menu.add_checkbutton(label='Make Moderator')

# Right-side containing the other panels
page_display = Frame(root, bg="blue")
page_display.pack(side=RIGHT, fill=BOTH, expand=True)


def page_widget(page: Page):
    if page.is_text:
        t = tk.Text(page_display)
        t.pack(side=TOP)
        return t
    else:
        # TODO: delete pass
        c = Canvas(page_display, height="6c", width="6c")
        c.pack()
        return c


# TODO: paint event
def paint(event):
    x1, y1 = event.x, event.y
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2) fill="black", width=10)


# TODO: pp_canvas generator
def pp_canvas(page: Page, parent: Frame):
    c = Canvas(parent, height="6i", width="6i")

    return c

# code for generating a custom canvas for drawing

# test_text = page_widget(test_page_text)
test_canv = page_widget(test_page_draw)


# Closing the game
def close(event):
    root.destroy()


# Binds Esc key to close the game's window
root.bind("<Escape>", close)

root.mainloop()
