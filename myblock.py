import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
## バーデータ
barrect = pg.Rect(400, 500, 100, 20)
## ボール
ballrect = pg.Rect(400, 450, 10, 10)
## ブロック
blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50+xx*100, 40+yy*50, 80, 30))

def gamestage():
    # 背景
    screen.fill(pg.Color("NAVY"))
    # マウスの位置
    (mx, my) = pg.mouse.get_pos()
    # バーを表示
    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
    # ボールを表示
    pg.draw.circle(screen, pg.Color("CYAN"), [ballrect.x, ballrect.y], ballrect.width)
    # ブロックを表示
    n = 0
    for block in blocks:
        pg.draw.rect(screen, pg.Color("GOLD"), block)


while True:
    gamestage()
    # 画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
