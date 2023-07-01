import pygame
import sys
import random
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIME = (0,255,0)
CYAN = (0,255,255)
LIGHTBLUE=(173,216,230)
MAGENTA = (255,0,255)
PURPLE = (128,0,128)
GOLD  = (255,215,0)
SILVER = (192,192,192)

idx = 0
tmr = 0
start_up = 0
pl_x = 1
pl_y = 1
dx = 0
dy = 0
pl_d = 0
pl_a = 0
maze_h = 0
maze_w = 0
dungeon_h = 0
dungeon_w = 0
command_key = 0
com_mag = 0
treasure = 0
get_num = 0
boss_flag = 0
pl_hp = 0
pl_hp_max = 0
pl_attack = 0
pl_mp = 0
enemy_lv = 0
enemy_hp = 0
enemy_hp_max = 0
enemy_attack = 0
num_magic = 8
btl_cmd = 0
mouseX = 0
mouseY = 0
mBtn1 = 0
mBtn2 = 0
mBtn3 = 0

TRE_NAME = ["Branch","Stone","Iron","Gold","Jewel"]
MAG_NAME = ["Fire","Ice","Heal","Steal","ATK UP","DEF UP","T ATK","Explosion"]
imgItem = []
for i in range(1,6):
    imgItem.append(pygame.image.load("image/Item/item ("+str(i)+").png"))
    imgItem[i-1] = pygame.transform.scale(imgItem[i-1],[32,32])
imgWeapon = []
for i in range(1,6):
    imgWeapon.append(pygame.image.load("image/weapon/weapon ("+str(i)+").png"))
    imgWeapon[i-1] = pygame.transform.scale(imgWeapon[i-1],[32,32])
maze = []
dungeon = []

imgYusha = []
for i in range(1,13):
    imgYusha.append(pygame.image.load("image/yusha/yusha ("+str(i)+").png"))
    imgYusha[i-1] = pygame.transform.scale(imgYusha[i-1],[32,32])
imgRoad = pygame.image.load("image/road.png")
imgRoad = pygame.transform.scale(imgRoad,[32,32])
imgWall = pygame.image.load("image/kabe.png")
imgWall = pygame.transform.scale(imgWall,[32,32])
imgTakarabako = []
for i in range(1,5):
    imgTakarabako.append(pygame.image.load("image/takarabako/takarabako ("+str(i)+").png"))
    imgTakarabako[i-1] = pygame.transform.scale(imgTakarabako[i-1],[32,32])
imgEnemyShadow = pygame.image.load("image/enemy_shadow.png")
imgBossShadow = pygame.image.load("image/boss_shadow.png")
imgEnemy = pygame.image.load("image/enemy/enemy (1).png")
imgBtlBG = pygame.image.load("image/BtlBG.jpg")
imgBtlBG = pygame.transform.scale(imgBtlBG,[1200,900])
imgKey = [
    pygame.image.load("image/key/key_up.png"),
    pygame.image.load("image/key/key_down.png"),
    pygame.image.load("image/key/key_right.png"),
    pygame.image.load("image/key/key_left.png"),
    pygame.image.load("image/key/key_z.png")
    ]
for i in range(5):
    imgKey[i] = pygame.transform.scale(imgKey[i],[50,50])
imgAttack = []
for i in range(1,6):
    imgAttack.append(pygame.image.load("image/anime/attack/attack ("+str(i)+").png"))
imgUp = []
for i in range(1,11):
    imgUp.append(pygame.image.load("image/anime/up/up ("+str(i)+").png"))
    imgUp[i-1] = pygame.transform.scale(imgUp[i-1],[300,300])
imgIce = []
for i in range(1,9):
    imgIce.append(pygame.image.load("image/anime/ice/ice ("+str(i)+").png"))
    imgIce[i-1] = pygame.transform.scale(imgIce[i-1],[400,400])
imgFire = []
for i in range(1,9):
    imgFire.append(pygame.image.load("image/anime/fire/fire ("+str(i)+").png"))
    imgFire[i-1] = pygame.transform.scale(imgFire[i-1],[400,400])
imgExplosion = []
for i in range(1,9):
    imgExplosion.append(pygame.image.load("image/anime/explosion/explosion ("+str(i)+").png"))
    imgExplosion[i-1] = pygame.transform.scale(imgExplosion[i-1],[400,400])
imgHeal = []
for i in range(1,9):
    imgHeal.append(pygame.image.load("image/anime/heal/heal ("+str(i)+").png"))
    imgHeal[i-1] = pygame.transform.scale(imgHeal[i-1],[400,400])

#セーブデータの設定
num_save = 22
line_save = 29
idx_save =[1,3,5,7,9,10,11,12,13,15,16,17,18,19,21,22,23,24,25,26,27,28]
save_lines = [""]*line_save

#セーブデータの読み取り
with open("save.txt",encoding="utf-8") as f:
    i = 0
    while True:
        line = f.readline()
        if line:
            save_lines[i] = line
            save_lines[i] = save_lines[i].strip()
            i += 1
        else:
            break

#セーブデータの代入
pl_lv = int(save_lines[1])
dungeon_lib = int(save_lines[3])
start_up = int(save_lines[5]) + 1
exp = int(save_lines[7])

Item_num = [0]*5
for i in range(0,5):
    Item_num[i] = int(save_lines[9+i])
Weapon_num = [0]*5
for i in range(0,5):
    Weapon_num[i] = int(save_lines[15+i])
Magic_num = [0]*num_magic
for i in range(0,num_magic):
    Magic_num[i] = int(save_lines[21+i])

def save():
    global save_lines
    for i in range(num_save):
        save_lines[idx_save[i]] = [""]
    
    save_lines[1] = str(pl_lv)
    save_lines[3] = str(dungeon_lib)
    save_lines[5] = str(start_up)
    save_lines[7] = str(exp)
    for i in range(5):
        save_lines[9+i] = str(Item_num[i])
    for i in range(5):
        save_lines[15+i] = str(Weapon_num[i])
    for i in range(8):
        save_lines[21+i] = str(Magic_num[i])

def status():
    global pl_attack, pl_hp_max
    pl_attack = int(pl_lv * 10 * (1 + Weapon_num[0]*0.1))
    pl_hp_max = int(pl_lv * 100 * (1 + Weapon_num[4]*0.5))

#フォントサイズ
def font(size):
    return pygame.font.Font(None, size)

def pl_exp(bg,x):   #経験値処理
    global pl_lv, exp, pl_hp_max, pl_hp, pl_attack
    exp += int(x * (1+Weapon_num[3]))
    while True:
        if exp > pl_lv*10:
            exp -= pl_lv*10
            draw_text(bg, "Level UP!!",400,600,font(100),WHITE)
            pl_lv += 1
        else:
            break

def make_dungeon(DUN_LV): # ダンジョンの自動生成
    global maze, dungeon, maze_h, maze_w, dungeon_h, dungeon_w

    maze = []
    XP = [0,1,0,-1]
    YP = [-1,0,1,0]
    maze_h = DUN_LV*2 + 3
    maze_w = DUN_LV*2 + 5
    
    for y in range(maze_h):
        maze.append([0]*maze_w)
    for x in range(maze_w):
        maze[0][x] = 1
        maze[maze_h - 1][x] = 1
    for y in range(maze_h):
        maze[y][0] = 1
        maze[y][maze_w-1] = 1

    for y in range(1,maze_h-1):
        for x in range(1,maze_w-1):
            maze[y][x] = 0

    for y in range(2,maze_h-2,2):
        for x in range(2,maze_w-2,2):
            maze[y][x] = 1

    for y in range(2,maze_h-2,2):
        for x in range(2,maze_w-2,2):
            d = random.randint(0,3)
            if x > 2:
                d = random.randint(0,2)
            maze[y+YP[d]][x+XP[d]] = 1
    

def draw_dungeon(bg, fnt, DUN_LV): # ダンジョンを描画する
    global maze, dungeon, maze_h, maze_w, dungeon_h, dungeon_w
    bg.fill(BLACK)
    for y in range(maze_h):
        for x in range(maze_w):
            w = 32
            h = 32
            DX = dx*w
            DY = dy*h
            X = x*w
            Y = y*h
            if maze[y][x] == 0:
                bg.blit(imgRoad,[X-DX,Y-DY])
            if maze[y][x] == 1:
                bg.blit(imgWall,[X-DX,Y-DY])
            if maze[y][x] == 2:
                bg.blit(imgTakarabako[0],[X-DX,Y-DY])
            if maze[y][x] == 3:
                bg.blit(imgRoad,[X-DX,Y-DY])
                bg.blit(imgEnemyShadow,[X-DX,Y-DY])
            if maze[y][x] == 4:
                bg.blit(imgRoad,[X-DX,Y-DY])
                bg.blit(imgBossShadow,[X-DX,Y-DY])
            if maze[y][x] == 21:
                bg.blit(imgTakarabako[3],[X-DX,Y-DY])

def put_event(DUN_LV): #イベントの配置
    global maze, maze_h, maze_w

    for i in range(int(DUN_LV**1.5)):  #宝箱
        x = random.randint(1, maze_w-2)
        y = random.randint(1, maze_h-2)
        if(maze[y][x] == 0):
            maze[y][x] = 2
    for i in range(DUN_LV**2):   #敵
        x = random.randint(1, maze_w-2)
        y = random.randint(1, maze_h-2)
        if(maze[y][x] == 0 or maze[y][x] == 2):
            maze[y][x] = 3
    while True:
        x = random.randint(int(maze_w/2), maze_w-2)
        y = random.randint(int(maze_h/2), maze_h-2)
        if maze[y][x] != 1:
            if x != 1 or y != 1:
                maze[y][x] = 4
                break
    maze[1][1] = 0

def move_player(bg,key):
    global pl_x, pl_y, pl_d, pl_a, idx, tmr, treasure, enemy_lv, boss_flag, btl_cmd, dx, dy
    global maze_h, maze_w, imgEnemy, Item_num, get_num
    
    if maze[pl_y][pl_x] == 2:   #宝箱に乗る
        maze[pl_y][pl_x] = 21
        tre = random.randint(0,1000)
        if tre == 0:
            treasure = 4
        elif tre < 5:
            treasure = 3
        elif tre < 50:
            treasure = 2
        elif tre < 400:
            treasure = 1
        else:
            treasure = 0
        get_num = 1 + int(random.randint(0,Item_num[2]*10)/10)
        Item_num[treasure] += get_num
        tmr = 0
        idx = 5
        return
    
    if maze[pl_y][pl_x] == 3:   #敵の影に乗る
        maze[pl_y][pl_x] = 0
        enemy_lv = random.randint(1,dungeon_dis)
        ene = random.randint(0,dungeon_dis)
        tmr = 0
        idx = 40
        return

    if maze[pl_y][pl_x] == 4:
        maze[pl_y][pl_x] = 0
        boss_flag = 1
        tmr = 0
        idx = 40
        return
    
    if btl_cmd == 1 and pl_y != 0:
        pl_d = 3
        if maze[pl_y-1][pl_x] != 1:
            pl_y = pl_y - 1
    if btl_cmd == 2 and pl_y != maze_h - 1:
        pl_d = 0
        if maze[pl_y+1][pl_x] != 1:
            pl_y = pl_y + 1
    if btl_cmd == 4 and pl_x != 0:
        pl_d = 1
        if maze[pl_y][pl_x-1] != 1:
            pl_x = pl_x - 1
    if btl_cmd == 3 and pl_x != maze_w - 1:
        pl_d = 2
        if maze[pl_y][pl_x+1] != 1:
            pl_x = pl_x + 1
    pl_a = pl_d
    if pl_x > 18:
        dx = pl_x - 18
    else:
        dx = 0
    if pl_y > 14:
        dy = pl_y - 14
    else:
        dy = 0

def init_battle():
    global imgEnemy, enemy_hp, enemy_hp_max, enemy_lv, enemy_attack
    typ = random.randint(1, dungeon_dis)
    if dungeon_dis >= 9:
        typ = random.randint(1,9)
    if dungeon_dis < 5:
        enemy_lv = random.randint(1, dungeon_dis)
    else:
        enemy_lv = random.randint(dungeon_dis-4, dungeon_dis)
    enemy_hp_max = int((enemy_lv*dungeon_dis)**1.5)*3
    enemy_hp = enemy_hp_max
    enemy_attack = int(enemy_lv*dungeon_dis*typ*0.5)
    imgEnemy = pygame.image.load("image/enemy/enemy (" + str(typ) + ").png")
    imgEnemy = pygame.transform.scale(imgEnemy,[400,400])
    if boss_flag == 1:
        enemy_lv = dungeon_dis
        enemy_hp_max = int(dungeon_dis**2.5)*20
        enemy_hp = enemy_hp_max
        enemy_attack = int(dungeon_dis**2)*20
        imgEnemy = pygame.image.load("image/enemy/enemy (10).png")
        imgEnemy = pygame.transform.scale(imgEnemy,[400,400])

def draw_battle(bg, fnt):   #"戦闘の描画"
    bg.blit(imgBtlBG,[0,0])
    bg.blit(imgEnemy,[400,50])
    hp_ratio = pl_hp / pl_hp_max
    hp_ratio_emy = enemy_hp / enemy_hp_max
    draw_text(bg,"Lv: "+str(enemy_lv),200,50,font(40),WHITE)
    pygame.draw.rect(bg,WHITE,[398,598,404,24])
    draw_text(bg,"HP: "+str(pl_hp)+" / "+str(pl_hp_max),400,650,font(40),WHITE)
    pygame.draw.rect(bg,GREEN,[400,600,400*hp_ratio,20])
    if hp_ratio < 1:
        pygame.draw.rect(bg,BLACK,[400+400*hp_ratio,600,400-400*hp_ratio,20])
    draw_text(bg,"MP: ",400,700,font(40),WHITE)
    for i in range(0,5):
        pygame.draw.circle(bg,BLACK,[500+40*i,710],15)
    for i in range(0,pl_mp):
        pygame.draw.circle(bg,MAGENTA,[500+40*i,710],15)
    pygame.draw.rect(bg,WHITE,[398,48,404,24])
    draw_text(bg,"HP: "+str(enemy_hp)+" / "+str(enemy_hp_max),850,50,font(40),WHITE)
    pygame.draw.rect(bg,GREEN,[400,50,400*hp_ratio_emy,20])
    if hp_ratio_emy < 1:
        pygame.draw.rect(bg,BLACK,[400+400*hp_ratio_emy,50,400-400*hp_ratio_emy,20])
    for i in range(16):
        draw_text(bg, message[i],850,100+i*50,font(40),WHITE)

magic_msg = ["---"]*num_magic
def draw_command(bg,fnt):
    global idx, tmr, command_key, com_mag
    pygame.draw.polygon(bg, RED,[[252,400+command_key*100],[200,430+command_key*100],[252,460+command_key*100]])
    if idx == 41:
        draw_text(bg, "Attack",0,400,font(80),WHITE)
        draw_text(bg, "Magic",0,500,font(80),WHITE)
        draw_text(bg, "DEFENCE",0,600,font(80),WHITE)
        draw_text(bg, "Run",0,700,font(80),WHITE)
    if idx == 43:
        for i in range(0,num_magic):
            if Magic_num[i] > 0:
                magic_msg[i] = MAG_NAME[i]
        if tmr == 2:
            com_mag = 0
        for i in range(4):
            draw_text(bg, magic_msg[com_mag+i],0,400+100*i,font(80),WHITE)
            draw_text(bg, "MP : "+str(int((com_mag+i)/2)+2),50,470+100*i,font(40),WHITE)
        

message = [""]*16
def init_message():
    for i in range(16):
        message[i] = ""
def set_message(msg):
    for i in range(16):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(15):
        message[i] = message[i+1]
    message[15] = msg

def draw_text(bg,txt,x,y,fnt,col):
    sur = fnt.render(txt,True,BLACK)
    bg.blit(sur,[x+1,y+2])
    sur = fnt.render(txt,True,col)
    bg.blit(sur,[x,y])

def mouse(bg):
    global mouseX, mouseY, btl_cmd
    global mBtn1, mBtn2, mBtn3
    bg.blit(imgKey[0],[1050,700])
    if mouseX >= 1050 and mouseX <1100 and mouseY >= 700 and mouseY < 750 and mBtn1 == 1:
        btl_cmd = 1
    bg.blit(imgKey[1],[1050,800])
    if mouseX >= 1050 and mouseX <1100 and mouseY >= 800 and mouseY < 850 and mBtn1 == 1:
        btl_cmd = 2
    bg.blit(imgKey[2],[1100,750])
    if mouseX >= 1100 and mouseX <1150 and mouseY >= 750 and mouseY < 800 and mBtn1 == 1:
        btl_cmd = 3
    bg.blit(imgKey[3],[1000,750])
    if mouseX >= 1000 and mouseX <1050 and mouseY >= 750 and mouseY < 800 and mBtn1 == 1:
        btl_cmd = 4
    bg.blit(imgKey[4],[1050,750])
    if mouseX >= 1050 and mouseX <1100 and mouseY >= 750 and mouseY < 800 and mBtn1 == 1:
        btl_cmd = 5

def main():
    global idx, tmr, start_up, treasure, command_key, com_mag, boss_flag, get_num
    global mouseX, mouseY, mBtn1, mBtn2, mBtn3, btl_cmd
    global num_save, save_lines
    global pl_x, pl_y, pl_a, pl_d, pl_hp, pl_hp_max, enemy_hp, pl_mp
    global pl_lv, exp, pl_attack, dungeon_lib, dungeon_dis
    tmp_idx = 0
    speed = 1
    dungeon_dis = 1
    dmg = 0
    heal = 0
    pl_mp = 5
    sp_magic = 0
    magic_flag = [0]*8
    DEF_flag = 0

    pygame.mixer.init()
    se = [
        pygame.mixer.Sound("sound/se/attack.mp3"),
        pygame.mixer.Sound("sound/se/damage.mp3"),
        pygame.mixer.Sound("sound/se/defence.mp3"),
        pygame.mixer.Sound("sound/se/run.mp3"),
        pygame.mixer.Sound("sound/se/critical.mp3")
    ]
    
    pygame.init()
    pygame.display.set_caption("強くなりたい勇者")
    screen = pygame.display.set_mode((1200,900))
    clock=pygame.time.Clock()

    while True:
        tmr = tmr + 1
        key = pygame.key.get_pressed()
        status()
        i = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_m:
                    tmp_idx = idx
                    idx = 10
        
        btl_cmd = 0
        if key[K_w] == 1 or key[K_UP] == 1:
            btl_cmd = 1
        if key[K_s] == 1 or key[K_DOWN] == 1:
            btl_cmd = 2
        if key[K_d] == 1 or key[K_RIGHT] == 1:
            btl_cmd = 3
        if key[K_a] == 1 or key[K_LEFT] == 1:
            btl_cmd = 4
        if key[K_z] == 1:
            btl_cmd = 5

        #マウスカーソル
        mouseX, mouseY = pygame.mouse.get_pos()
        mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed()

        if idx == 0:    #タイトル画面
            screen.fill(BLACK)
            draw_text(screen,"A HERO",300,100,font(200),GOLD)
            draw_text(screen,"WHO WANTS TO BE STRONG",100,300,font(100),WHITE)
            if int(tmr/5)%4 == 0 or int(tmr/5)%4 == 2:
                screen.blit(pygame.transform.scale(imgYusha[4],[200,200]),[500,400])
            elif int(tmr/5)%4 == 1:
                screen.blit(pygame.transform.scale(imgYusha[0],[200,200]),[500,400])
            else:
                screen.blit(pygame.transform.scale(imgYusha[8],[200,200]),[500,400])
            if tmr == 1:
                pygame.mixer.music.load("sound/bgm/bgm_title.ogg")
                pygame.mixer.music.play(-1)
            if tmr%60 <= 50:
                draw_text(screen,"press space key to start!",200,700,font(100),WHITE)
            if key[K_SPACE] == 1:
                tmr = 0
                if start_up == 1:
                    start_up += 1
                    idx = 20
                else:
                    idx = 1
        elif idx == 1:    #HOME画面
            pl_hp = pl_hp_max
            pl_mp = 5
            screen.fill(BLACK)
            draw_text(screen,"Level " + str(pl_lv),0,0,font(40),WHITE)
            draw_text(screen,"[D]ungeon",0,50,font(80),WHITE)
            draw_text(screen,"[S]tatus",0,150,font(80),WHITE)
            draw_text(screen,"[G]acha",0,250,font(80),WHITE)
            draw_text(screen,"s[Y]nthetic",0,350,font(80),WHITE)
            if tmr == 1:
                pygame.mixer.music.load("sound/bgm/bgm_home.ogg")
                pygame.mixer.music.play(-1)
            for i in range(5):
                screen.blit(imgItem[i],[800,500+50*i])
                screen.blit(imgWeapon[i],[600,500+50*i])
                draw_text(screen,": "+str(Item_num[i]),850,500+50*i,font(40),WHITE)
                draw_text(screen,": "+str(Weapon_num[i]),650,500+50*i,font(40),WHITE)
            if key[K_s] == 1:
                tmr = 0
                idx = 2
            if key[K_d] == 1:
                tmr = 0
                idx =3
            if key[K_y] == 1:
                tmr = 0
                idx = 14
            if key[K_g] == 1:
                tmr = 0
                idx = 30
        elif idx == 2:    #ステータス画面
            screen.fill(BLACK)
            draw_text(screen,"Level : "+str(pl_lv),0,0,font(80),CYAN)
            draw_text(screen,"Attack : "+str(pl_attack),0,100,font(40),CYAN)
            draw_text(screen,"HP : "+str(pl_hp)+" / "+str(pl_hp_max),0,150,font(40),CYAN)
            draw_text(screen,"Critical : "+str(Weapon_num[1]/100)+" %",0,200,font(40),CYAN)
            draw_text(screen,"Treasure : "+str(Weapon_num[2]/10)+" %",0,250,font(40),CYAN)
            draw_text(screen,"Exp : "+str(Weapon_num[3]*100+100)+" %",0,300,font(40),CYAN)
            for i in range(0,num_magic):
                if Magic_num[i] > 0:
                    draw_text(screen,MAG_NAME[i],0,350+50*i,font(40),MAGENTA)
                    draw_text(screen,"Lv "+str(Magic_num[i]),350,350+50*i,font(40),MAGENTA)
                else:
                    draw_text(screen,"---",0,350+50*i,font(40),MAGENTA)
                
            if key[K_b] == 1:
                tmr = 0
                idx = 1
        elif idx == 3:    #ダンジョン選択画面
            screen.fill(LIGHTBLUE)
            pygame.draw.polygon(screen,BLACK,[[270,dungeon_dis*50 - 35],[300,dungeon_dis*50 - 50],[300,dungeon_dis*50 - 20]])
            mouse(screen)
            if btl_cmd == 2 and dungeon_dis < dungeon_lib:
                dungeon_dis += 1
            if btl_cmd == 1 and dungeon_dis > 1:
                dungeon_dis -= 1
            if btl_cmd == 5:
                pl_x = 1
                pl_y = 1
                make_dungeon(dungeon_dis)
                put_event(dungeon_dis)
                tmr = 0
                idx = 4
            if key[K_b] == 1:
                idx = 1
            for i in range(1,19):
                if dungeon_lib >= i:
                    draw_text(screen,"dungeon "+str(i),100,i*50 - 50,font(40),BLACK)
                else:
                    draw_text(screen,"dungeon "+str(i),100,i*50 - 50,font(40),SILVER)
        elif idx == 4:  #ダンジョン画面
            for i in range(0,8):
                magic_flag[i] = 0
            screen.fill(BLACK)
            if tmr == 1:
                pygame.mixer.music.load("sound/bgm/bgm_dungeon.ogg")
                pygame.mixer.music.play(-1)
            mouse(screen)
            move_player(screen,key)
            draw_dungeon(screen,font(40),dungeon_dis)
            screen.blit(imgKey[0],[1050,700])
            screen.blit(imgKey[1],[1050,800])
            screen.blit(imgKey[2],[1100,750])
            screen.blit(imgKey[3],[1000,750])
            screen.blit(imgKey[4],[1050,750])
            screen.blit(imgYusha[pl_a],[pl_x*32-dx*32,pl_y*32-dy*32])
        elif idx == 5:  #宝箱に乗る
            draw_text(screen,"GET "+TRE_NAME[treasure] + str(get_num),200,500,font(100),WHITE)
            if tmr == 15:
                idx = 4
        elif idx == 10: #MENU画面
            screen.fill(BLACK)
            draw_text(screen,"[S]ave",100,0,font(40),WHITE)
            draw_text(screen,"[T]itle",100,50,font(40),WHITE)
            draw_text(screen,"[I]tem",100,100,font(40),WHITE)
            draw_text(screen,"s[P]eed",100,150,font(40),WHITE)
            if key[K_s] == 1:
                tmr = 0
                idx = 11
            if key[K_t] == 1:
                tmr = 0
                idx = 0
            if key[K_i] == 1:
                tmr = 0
                idx = 13
            if key[K_p] == 1:
                speed += 1
                if speed > 4:
                    speed = 1
            if key[K_b] == 1:
                tmr = 0
                idx = tmp_idx
        elif idx == 11: #セーブ画面
            screen.fill(BLACK)
            draw_text(screen,"Do you want to save?",100,0,font(40),WHITE)
            draw_text(screen,"[Y]es or [N]o",100,200,font(40),WHITE)
            if key[K_y] == 1:
                save()
                with open("save.txt",mode='w',encoding="utf-8_sig") as f:
                    for i in range(line_save):
                        f.write(save_lines[i])
                        f.write('\n')
                tmr = 0
                idx = tmp_idx
            if key[K_n] == 1:
                tmr = 0
                idx = tmp_idx
        elif idx == 13: #アイテム画面
            screen.fill(BLACK)
            for i in range(5):
                screen.blit(imgItem[i],[800,500+50*i])
                screen.blit(imgWeapon[i],[600,500+50*i])
                draw_text(screen,": "+str(Item_num[i]),850,500+50*i,font(40),WHITE)
                draw_text(screen,": "+str(Weapon_num[i]),650,500+50*i,font(40),WHITE)
            if key[K_b] == 1:
                tmr = 0
                idx = 1
        elif idx == 14: #合成
            screen.fill(BLACK)
            draw_text(screen,"[1]",0,300,font(80),WHITE)
            draw_text(screen,"[2]",0,400,font(80),WHITE)
            draw_text(screen,"[3]",0,500,font(80),WHITE)
            draw_text(screen,"[4]",0,600,font(80),WHITE)
            draw_text(screen,"[5]",0,700,font(80),WHITE)
            for i in range(5):
                screen.blit(pygame.transform.scale(imgWeapon[i],[100,100]),[100,300+100*i])
                screen.blit(pygame.transform.scale(imgItem[i],[50,50]),[200+200*i,100])
                draw_text(screen,str(Item_num[i]),200+200*i,150,font(40),WHITE)
            screen.blit(imgItem[0],[300,350])
            draw_text(screen,str((Weapon_num[0]+1)*2),350,350,font(40),LIME)
            screen.blit(imgItem[2],[600,350])
            draw_text(screen,str(Weapon_num[0]+1),650,350,font(40),LIME)
            if Item_num[0] >= (Weapon_num[0]+1)*2 and Item_num[2] >= Weapon_num[0]+1:
                pygame.draw.rect(screen,LIME,[900,350,100,40])
                draw_text(screen,"make",900,350,font(50),WHITE)
                if key[K_1] == 1:
                    Item_num[0] -= (Weapon_num[0]+1)*2
                    Item_num[2] -= Weapon_num[0]+1
                    Weapon_num[0] += 1
            screen.blit(imgItem[1],[300,450])
            draw_text(screen,str((Weapon_num[1]+1)*2),350,450,font(40),LIME)
            screen.blit(imgItem[2],[600,450])
            draw_text(screen,str(Weapon_num[1]+1),650,450,font(40),LIME)
            if Item_num[1] >= (Weapon_num[1]+1)*2 and Item_num[2] >= Weapon_num[1]+1:
                pygame.draw.rect(screen,LIME,[900,450,100,40])
                draw_text(screen,"make",900,450,font(50),WHITE)
                if key[K_2] == 1:
                    Item_num[1] -= (Weapon_num[0]+1)*2
                    Item_num[2] -= Weapon_num[0]+1
                    Weapon_num[1] += 1
            screen.blit(imgItem[1],[300,550])
            draw_text(screen,str((Weapon_num[2]+1)*2),350,550,font(40),LIME)
            screen.blit(imgItem[3],[600,550])
            draw_text(screen,str(Weapon_num[2]+1),650,550,font(40),LIME)
            if Item_num[1] >= (Weapon_num[2]+1)*2 and Item_num[3] >= Weapon_num[2]+1:
                pygame.draw.rect(screen,LIME,[900,550,100,40])
                draw_text(screen,"make",900,550,font(50),WHITE)
                if key[K_3] == 1:
                    Item_num[1] -= (Weapon_num[2]+1)*2
                    Item_num[3] -= Weapon_num[2]+1
                    Weapon_num[2] += 1
            screen.blit(imgItem[0],[300,650])
            draw_text(screen,str((Weapon_num[3]+1)*2),350,650,font(40),LIME)
            screen.blit(imgItem[3],[600,650])
            draw_text(screen,str(Weapon_num[3]+1),650,650,font(40),LIME)
            if Item_num[0] >= (Weapon_num[3]+1)*2 and Item_num[3] >= Weapon_num[3]+1:
                pygame.draw.rect(screen,LIME,[900,650,100,40])
                draw_text(screen,"make",900,650,font(50),WHITE)
                if key[K_4] == 1:
                    Item_num[0] -= (Weapon_num[3]+1)*2
                    Item_num[3] -= Weapon_num[3]+1
                    Weapon_num[3] += 1
            screen.blit(imgItem[0],[300,750])
            draw_text(screen,str((Weapon_num[4]+1)*3),350,750,font(40),LIME)
            screen.blit(imgItem[1],[600,750])
            draw_text(screen,str((Weapon_num[4]+1)*3),650,750,font(40),LIME)
            if Item_num[0] >= (Weapon_num[4]+1)*3 and Item_num[1] >= (Weapon_num[4]+1)*3:
                pygame.draw.rect(screen,LIME,[900,750,100,40])
                draw_text(screen,"make",900,750,font(50),WHITE)
                if key[K_5] == 1:
                    Item_num[0] -= (Weapon_num[4]+1)*3
                    Item_num[1] -= (Weapon_num[4]+1)*3
                    Weapon_num[4] += 1
            if key[K_b] == 1:
                tmr = 0
                idx = 1
        elif idx == 20: #説明画面
            screen.fill(BLACK)
            draw_text(screen,"MENU   : [M]",100,200,font(60),WHITE)
            draw_text(screen,"BACK   : [B]",100,300,font(60),WHITE)
            draw_text(screen,"SELECT : [Z]",100,400,font(60),WHITE)
            draw_text(screen,"UP     : [W]",400,200,font(60),WHITE)
            draw_text(screen,"DOWN   : [S]",400,300,font(60),WHITE)
            draw_text(screen,"RIGHT  : [D]",400,400,font(60),WHITE)
            draw_text(screen,"LEFT   : [A]",400,500,font(60),WHITE)
            if tmr > 30:
                if tmr%60 <= 50:
                    draw_text(screen,"press [Z]",100,700,font(100),WHITE)
                if key[K_z] == 1:
                    tmr = 0
                    idx = 1
        elif idx == 30: #ガチャ画面
            screen.fill(BLACK)
            draw_text(screen,"Let's Gacha !! [SPACE]: need 10",100,500,font(80),GOLD)
            screen.blit(pygame.transform.scale(imgItem[4],[60,60]),[970,500])
            draw_text(screen,str(Item_num[4]),1050,100,font(40),WHITE)
            screen.blit(imgItem[4],[1000,100])
            if key[K_SPACE] == 1:
                if Item_num[4] >= 10:
                    Item_num[4] -= 10
                    tmr = 0
                    idx = 31
                else:
                    draw_text(screen,"Not enough Jewel",100,100,font(80),WHITE)
            if key[K_b] == 1:
                tmr = 0
                idx = 1
        elif idx == 31: #ガチャ結果
            screen.fill(BLACK)
            if tmr == 1:
                gacha_Item = random.randint(0,1)
                get_num = 0
                get_kind = 0
                if gacha_Item == 0:
                    gacha_Item = random.randint(1,3)
                    get_num = random.randint(10,30)
                    Item_num[gacha_Item] += get_num
                else:
                    gacha_Item = random.randint(0,7)
                    get_num = random.randint(1,3)
                    Magic_num[gacha_Item] += get_num
                    get_kind = 1
            if tmr > 1:
                if get_kind == 0:
                    draw_text(screen,"Get "+TRE_NAME[gacha_Item]+" : "+str(get_num),100,100,font(80),GOLD)
                else:
                    draw_text(screen,"Get "+MAG_NAME[gacha_Item]+" : "+str(get_num),100,100,font(80),MAGENTA)
            if tmr >= 30:
                draw_text(screen,"press [Z]",100,700,font(100),WHITE)
                if key[K_z] == 1:
                    tmr = 0
                    idx = 30
        elif idx == 40: #戦闘画面
            if tmr == 1:
                init_battle()
                init_message()
                if boss_flag == 1:
                    pygame.mixer.music.load("sound/bgm/bgm_battle.ogg")
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.load("sound/bgm/bgm_boss.ogg")
                    pygame.mixer.music.play(-1)
            elif tmr <= 15:
                bx = (15-tmr)*300
                by = 0
                screen.blit(imgBtlBG, [bx,by])
            elif tmr <= 30:
                draw_battle(screen, font(80))
            else:
                tmr = 0
                idx = 41
        elif idx == 41: #プレイヤーのターン
            mouse(screen)
            if tmr == 1:
                DEF_flag = 0
                freeze_flag = 0
                command_key = 0
                set_message("Your turn.")
            if btl_cmd == 2 and command_key != 3:
                command_key += 1
            if btl_cmd == 1 and command_key != 0:
                command_key -= 1
            if btl_cmd == 5:
                tmr = 0
                idx = 42 + command_key
                if command_key == 2:
                    if pl_mp < 5:
                        pl_mp += 1
                    DEF_flag = 1
                    se[2].play()
                    idx = 46
            draw_battle(screen, font(80))
            draw_command(screen,font(80))
            mouse(screen)
        elif idx == 42: #攻撃
            draw_battle(screen, font(80))
            dmg = pl_attack
            if magic_flag[4] == 1:
                dmg = int(dmg*(1.5+0.01*Magic_num[4]))
            if tmr == 1:
                se[0].play()
                if pl_mp < 5:
                    pl_mp += 1
                cri_flag = 0
                if Item_num[1] >= random.randint(1,10000) and boss_flag == 0:
                    se[4].play()
                    cri_flag = 1
                    enemy_hp = 0
                else:
                    if enemy_hp - dmg <= 0:
                        enemy_hp = 0
                    else:
                        enemy_hp -= dmg
            if tmr < 15:
                screen.blit(imgAttack[int(tmr/3)],[500,100])
            if tmr == 15:
                if cri_flag == 1:
                    set_message("Crirical!!")
                else:
                    set_message(str(dmg)+"damage!")
            if tmr > 60:
                tmr = 0
                if enemy_hp == 0:
                    idx = 49
                else:
                    idx = 46
        elif idx == 43: #魔法
            draw_battle(screen, font(80))
            mouse(screen)
            if tmr == 1:
                command_key = 0
            if btl_cmd == 2:
                if command_key != 3:
                    command_key += 1
                elif com_mag < num_magic - 4:
                    com_mag += 1
            if btl_cmd == 1:
                if command_key != 0:
                    command_key -= 1
                elif com_mag > 0:
                    com_mag -= 1
            sp_mag = com_mag + command_key
            if btl_cmd == 5 and Magic_num[sp_mag] > 0 and pl_mp >= int(sp_mag/2)+2:
                pl_mp -= int(sp_mag/2)+2
                magic_flag[sp_mag] = 1 
                tmr = 0
                idx = 44
            if key[K_b] == 1:
                tmr = 0
                idx = 41
            draw_battle(screen,font(80))
            draw_command(screen,font(80))
        elif idx == 44: #魔法の発動
            draw_battle(screen,font(80))
            if tmr == 1:
                if sp_mag == 0:
                    dmg = int(pl_attack*(8+random.randint(0,7))*0.1*(1+0.1*Magic_num[0]))
                elif sp_mag == 1:
                    dmg = pl_attack
                elif sp_mag == 6:
                    dmg = pl_attack
                    tmp = int(random.randint(0,Magic_num[6]+1000)/1000)
                elif sp_mag == 7:
                    dmg = int(pl_attack*8*(1+0.02*Magic_num[7]))
                if magic_flag[4] == 1:
                    dmg = int(dmg*(1.5+0.01*Magic_num[4]))
            if tmr < 15:
                if sp_mag == 0:
                    screen.blit(imgFire[int(tmr/2)],[400,100])
                if sp_mag == 1:
                    screen.blit(imgIce[int(tmr/2)],[400,100])
                if sp_mag == 2:
                    screen.blit(imgHeal[int(tmr/2)],[400,400])
                if sp_mag == 3 or sp_mag == 4 or sp_mag == 5:
                    screen.blit(imgUp[int(tmr/1.5)],[550,500])
                if sp_mag == 6:
                    for i in range(tmp+3):
                        if i < 4:
                            screen.blit(imgAttack[int(tmr/3)],[300+100*i,100])
                        elif i < 8:
                            screen.blit(imgAttack[int(tmr/3)],[300+100*(i-4),200])
                        elif i < 12:
                            screen.blit(imgAttack[int(tmr/3)],[300+100*(i-8),300])
                        else:
                            screen.blit(pygame.transform.scale(imgAttack[int(tmr/3)],[400,400]),[300,100])
                if sp_mag == 7:
                    screen.blit(imgExplosion[int(tmr/2)],[400,100])
            if tmr == 15:
                set_message("Invoke "+MAG_NAME[sp_mag])
                if sp_mag == 0 or sp_mag == 1 or sp_mag == 7:
                    if enemy_hp - dmg <= 0:
                        enemy_hp = 0
                    else:
                        enemy_hp -= dmg
                    set_message(str(dmg)+" damage!")
                if sp_mag == 1:
                    if random.randint(1,10000) < 3000 + Magic_num[1]:
                        set_message("Enemy freezed")
                        freeze_flag = 1
                if sp_mag == 2:
                    heal = int((pl_hp_max/4)*(1+0.01*Magic_num[2]))
                    if pl_hp + heal > pl_hp_max:
                        pl_hp = pl_hp_max
                    else:
                        pl_hp += heal
                    set_message(str(heal)+" healed!")
                if sp_mag == 3:
                    set_message("Increased exp gained!")
                if sp_mag == 4:
                    set_message("Increased damage!")
                if sp_mag == 5:
                    set_message("Increased defence!")
                if sp_mag == 6:
                    for i in range(0,tmp+3):
                        if enemy_hp - dmg <= 0:
                            enemy_hp = 0
                        else:
                            enemy_hp -= dmg
                        set_message(str(dmg)+" damage!")
                        if enemy_hp == 0:
                            break
                    set_message(str(tmp+3)+" times!!")
                if sp_mag == 7:
                    dmg = int(pl_hp_max*0.3)
                    if pl_hp - dmg <= 0:
                        pl_hp = 0
                    else:
                        pl_hp -= dmg
                    set_message(str(dmg)+" damage!")
            if tmr == 60:
                tmr = 0
                if enemy_hp == 0:
                    idx = 49
                elif pl_hp == 0:
                    idx = 47
                elif freeze_flag == 1:
                    idx = 41
                else:
                    idx = 46
                            
        elif idx == 45: #逃げる
            draw_battle(screen,font(40))
            if tmr == 1:
                set_message("...")
            if tmr == 15:
                if random.randint(0,9) > 7 or boss_flag == 1:
                    set_message("You failed to flee")
                    tmr = 0
                    idx = 46
                else:
                    se[3].play()
                    set_message("Running!")
            if tmr == 30:
                tmr = 0
                idx = 4
        elif idx == 46: #敵の攻撃
            draw_battle(screen,font(40))
            if tmr == 1:
                set_message("Enemy turn.")
                dmg = random.randint(enemy_attack,enemy_attack*2)
                if DEF_flag == 1:
                    dmg = int(dmg*0.2)
                if magic_flag[5] == 1:
                    dmg = int(dmg/(2+Magic_num[6]*0.1))
                if pl_hp - dmg <= 0:
                    pl_hp = 0
                else:
                    pl_hp -= dmg
            if tmr == 15:
                se[1].play()
                set_message(str(dmg)+" damaged")
            if tmr == 60:
                tmr = 0
                if pl_hp == 0:
                    idx = 47
                else:
                    idx = 41
        elif idx == 47: #敗北
            if boss_flag == 1:
                boss_flag = 0
            screen.fill(BLACK)
            draw_text(screen,"You losed...",400,500,font(100),WHITE)
            if tmr == 1:
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.stop()
            if tmr == 30:
                tmr = 0
                idx = 1
        elif idx == 49: #勝利
            draw_dungeon(screen,font(40),dungeon_dis)
            if tmr == 1:
                pygame.mixer.music.load("sound/bgm/bgm_win.ogg")
                pygame.mixer.music.play(-1)
            if boss_flag == 1:
                draw_text(screen,"Clear!",100,500,font(100),WHITE)
                if dungeon_lib == dungeon_dis:
                    draw_text(screen,"First Dungeon"+str(dungeon_lib)+" Conquered",100,600,font(100),WHITE)
                    draw_text(screen,"Get "+str(dungeon_lib*30)+" jewels",100,700,font(100),WHITE)
                    if tmr == 1:
                        Item_num[4] += dungeon_lib*30
                if tmr == 1:
                    if magic_flag[3] == 1:
                        pl_exp(screen,int(enemy_lv*10*(3+0.01*Magic_num[3])))
                    else:
                        pl_exp(screen,enemy_lv*10)
            else:
                draw_text(screen,"Defeated the Enemy!",100,500,font(100),WHITE)
                if tmr == 1:
                    if magic_flag[3] == 1:
                        pl_exp(screen,int(enemy_lv*3*(3+0.01*Magic_num[3])))
                    else:
                        pl_exp(screen,enemy_lv*3)
            if tmr > 30:
                draw_text(screen,"press [Z]",100,800,font(100),WHITE)
                if btl_cmd == 5:
                    if boss_flag == 1:
                        if dungeon_lib == dungeon_dis:
                            dungeon_lib += 1
                        boss_flag = 0
                        tmr = 0
                        idx = 1
                    else:
                        tmr = 0
                        idx = 4

        draw_text(screen, "speed "+str(speed), 1050, 0, font(40), WHITE)
        pygame.draw.circle(screen,GOLD,[mouseX,mouseY],4)
        
        pygame.display.update()
        clock.tick(10+5*speed)

if __name__ == '__main__':
    main()
