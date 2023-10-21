import pygame
from random import randint
pygame.init()
W= 700
H =550
fon = pygame.transform.scale(pygame.image.load('galaxy.jpg'),(W,H))
scr = pygame.display.set_mode((W,H))
pygame.mixer.init()
pygame.display.set_caption('Shooter')
#sp = pygame.mixer.Sound('fire.ogg')
#spase = pygame.mixer.Sound('fire.ogg')
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play(loops=-1)
fps = pygame.time.Clock()
class Astro():
    def __init__(self,x,y,w,h,img):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.image= pygame.transform.scale(pygame.image.load(self.img), (self.w, self.h))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = randint(5, 10)
    def update(self):
        self.rect.y += 1
        if self.rect.bottom >= 550:
            self.rect.y = -10
            self.rect.x = randint(30, 650)
astros = []
for el in range(2):
    astro = Astro(randint(30,650),-10,50,50,'ae.png')
    astros.append(astro)
class Player():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img),(self.w,self.h))
        self.rect = self.img_new.get_rect(center = (self.x,self.y))
        self.speed = randint(1,5)
    def control(self,W):
        global move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left >=0:
            self.rect.x -= move
        if key[pygame.K_RIGHT] and self.rect.right <= W:
            self.rect.x += move
class Create():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img),(self.w,self.h))
        self.rect = self.img_new.get_rect(center = (self.x,self.y))

    def update(self):
        self.rect.y += 1
        if self.rect.bottom >= 550:
            self.rect.y = -10
            self.rect.x = randint(30, 650)

class Bullet():
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img), (self.w, self.h))
        self.rect = self.img_new.get_rect(center=(self.x, self.y))
crate_added = False

player = Player(W//2,H - 50,70,100,'g1.png')
bul  = Bullet(player.rect.x,player.rect.y,10,31,'laser_bul.png')
bul_check = False
bul_list = []
enemy_list = []
create_list = []
def add_crate():

    for el in range(1):
        x = randint(10, 650)
        y = randint(50, 150)
        create = Create(x,y,50,50,'create.png')
        create_list.append(create)
        global crate_added
        crate_added = True




c =6
ki = 2
def add_enemy():
    for el in range(4):
        x = randint(50, 650)
        y = randint(50, 150)
        enemy=Player(x,y,50,50,'ufo.png')
        enemy_list.append(enemy)

add_enemy()
def add_enem():
    for el in range(10):
        x = randint(50, 650)
        y = randint(50, 150)
        enemy=Player(x,y,50,50,'enemy2.png')
        enemy_list.append(enemy)
run = True
s = 0
l = 0
health = 5
chek_text = False
chek_textw = False
def loose(enemy,bullets,scr):
    global chek_text
    text = pygame.font.Font(None,55).render('Ви програли',True,(155,95,55))
    global move
    global l
    global health
    for el in enemy:
        if   l>=100 or health<=0:
            enemy.clear()
            bullets.clear()
            astros.clear()
            move = 0
            chek_text =True
    if chek_text:
        scr.blit(text,(W//2 -95,H//2))

ji = 0
def won(enemy,bullets,scr):
    global chek_textw
    text = pygame.font.Font(None, 55).render('Ви Перемогли', True, (155, 95, 55))
    global move
    global s
    for el in enemy:
        if s >= 80:
            enemy.clear()
            bullets.clear()
            astros.clear()
            create_list.clear()
            move = 0
            chek_textw = True
    if chek_textw:
        scr.blit(text, (W // 2 - 95, H // 2))
move = 5
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bul_check = True
                #sp.play()
                bul_list.append(Bullet(player.rect.x, player.rect.y, 10, 31, 'laser_bul.png'))

    if s >= 5 and not crate_added:
        add_crate()
        crate_added = True
        if s >= 6:
            crate_added = False



    scr.blit(fon,(0,0))
    scr.blit(player.img_new, player.rect)
    player.control(W)

    for el in enemy_list:
        scr.blit(el.img_new,(el.rect.x,el.rect.y))
        el.rect.y+=el.speed
        if el.rect.bottom>=H:
            el.rect.x = randint(50,650)
            el.rect.y = randint(50,150)
            l = l+1
        for ell in bul_list:
            if bul_check == True:
                scr.blit(bul.img_new,(ell.rect.x + player.w//2,ell.rect.y))
                ell.rect.y -=1

            if ell.rect.colliderect(el.rect):
                el.rect.x = randint(50, 650)
                el.rect.y = randint(50, 150)
                s+=1
                bul_list.remove(ell)
            if c == 1:
                bul_list.append(bul)
    for el in astros:
        scr.blit(el.image,(el.rect.x,el.rect.y))
        el.update()
        if el.rect.colliderect(player.rect):
            el.rect.y = -10
            el.rect.x = randint(30, 650)
            health -= 1

    for cr in create_list:
        scr.blit(cr.img_new, cr.rect)
        cr.update()
        if cr.rect.colliderect(player.rect):
            fon = pygame.transform.scale(pygame.image.load('galaxy2.jpg'), (W, H))
            add_enem()




            create_list.clear()












    text = 'рахунок:' +str(s)
    text_score = pygame.font.Font(None,35).render(text,True,(77,11,155))
    text1 = 'пропущено:' +str(l)
    text_loose = pygame.font.Font(None, 32).render(text1, True, (77, 11, 155))
    text3 = 'життя: '+str(health)
    text_health = pygame.font.Font(None, 32).render(text3, True, (77, 11, 155))
    scr.blit(text_score,(50,50))
    scr.blit(text_loose,(50,100))
    scr.blit(text_health, (300, 10))
    #scr.blit(bul.img_new,(player.rect.x + player.w//2-bul.w//2,player.rect.y))
    #spase.play()


    fps.tick(30)
    loose(enemy_list,bul_list,scr)
    won(enemy_list, bul_list, scr)
    pygame.display.update()
