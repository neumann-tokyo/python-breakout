import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
barrect = pg.Rect(400, 500, 100, 20)
ballrect = pg.Rect(400, 450, 10, 10)
blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50+xx*100, 40+yy*50, 80, 30))

def gamestage():
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()
    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
    pg.draw.circle(screen, pg.Color("CYAN"), [ballrect.x, ballrect.y], ballrect.width)
    for block in blocks:
        pg.draw.rect(screen, pg.Color("GOLD"), block)

while True:
    gamestage()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
