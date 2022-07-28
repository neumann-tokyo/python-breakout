import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))

def gamestage():
    screen.fill(pg.Color("NAVY"))

while True:
    gamestage()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
