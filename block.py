import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
barrect = pg.Rect(400, 500, 100, 20)
ballrect = pg.Rect(400, 450, 10, 10)
vx = 8
vy = -8
blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50+xx*100, 40+yy*50, 80, 30))

def gamestage():
    global vx, vy
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos()
    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > 800 - 10:
        vx = -vx
    if barrect.colliderect(ballrect):
        vy = -vy
    ballrect.x += vx
    ballrect.y += vy
    pg.draw.circle(screen, pg.Color("CYAN"), [ballrect.x, ballrect.y], ballrect.width)
    n = 0
    for block in blocks:
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ballrect):
            vy = -vy
            blocks[n] = pg.Rect(0,0,0,0)
        n += 1

while True:
    gamestage()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
