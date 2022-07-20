import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
## バーデータ
barrect = pg.Rect(400, 500, 100, 20)
## ボール
ballrect = pg.Rect(400, 450, 10, 10)
vx = random.randint(-10, 10)
vy = -5
## ブロック
blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50+xx*100, 40+yy*50, 80, 30))
## game status
page = "play"

## データのリセット
def gamereset():
    global vx, vy
    global score
    global blocks
    vx = random.randint(-10, 10)
    vy = -5
    ballrect.x = 400
    ballrect.y = 450
    score = 0
    blocks = []
    for yy in range(4):
        for xx in range(7):
            blocks.append(pg.Rect(xx*100+50, yy*50+40, 80, 30))

def gamestage():
    global vx, vy
    global page
    # 背景
    screen.fill(pg.Color("NAVY"))
    # マウスの位置
    (mx, my) = pg.mouse.get_pos()
    # バーを表示
    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)
    # ボールを表示
    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > 800 - 10:
        vx = -vx
    if barrect.colliderect(ballrect):
        vy = -vy
    if ballrect.y > 600:
        page = "gameover"
    ballrect.x += vx
    ballrect.y += vy
    pg.draw.circle(screen, pg.Color("CYAN"), [ballrect.x, ballrect.y], ballrect.width)
    # ブロックを表示
    n = 0
    for block in blocks:
        pg.draw.rect(screen, pg.Color("GOLD"), block)

## ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    # btn1 = screen.blit(replay_img,(320, 480))
    # 5.絵を描いたり、判定したりする
    # button_to_jump(btn1, 1)

while True:
    if page == "play":
        gamestage()
    elif page == "gameover":
        gameover()
    else:
        gameclear()
    # 画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
