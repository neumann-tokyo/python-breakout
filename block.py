import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
barrect = pg.Rect(400, 500, 100, 20)

def gamestage():
    screen.fill(pg.Color("NAVY"))
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

while True:
    gamestage()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
