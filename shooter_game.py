#Создай собственный Шутер!
#ок создаю!

from pygame import *

from random import *

from time import time as timer

window = display.set_mode((700, 500))
display.set_caption('MOTHERFUCKEEEEEEEEEER')
background = transform.scale(image.load('galaxy.jpg'),
             (700, 500))

lost = 0

win_height = 410
win_width = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,
                 player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    
    def shoot(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, -15)
        bullets.add(bullet)
        bullet2 = Bullet2('bullet.png', self.rect.centerx-60, self.rect.top, -15)
        bullets2.add(bullet2)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width-80) 
            self.rect.y = 0 
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Bullet2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

her = Player('rocket.png', 350, 415, 10)

motherfuckers = sprite.Group()

cherti = sprite.Group()

bullets = sprite.Group()

bullets2 = sprite.Group()

for i in range(1, 6):
    motherfucker = Enemy('ufo.png', 10, 10, 1)
    motherfuckers.add(motherfucker)

for i in range(1, 3):
    chert = Enemy('asteroid.png', 10, 10, 1)
    cherti.add(chert)


run = True
finish = False

font.init()
font1 = font.Font(None, 36)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)
fire = mixer.Sound('fire.ogg')

penis = 0

num_fire = 0
rearm = False

while run:
    window.blit(background, (0, 0))



    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rearm == False:
                    num_fire += 1    
                    her.shoot()
                if num_fire >= 5 and rearm == False:
                    jatsa = timer()
                    rearm = True

    if finish != True:
        her.update()  
        her.reset()
        bullets.update()
        bullets.draw(window)
        bullets2.update()
        bullets2.draw(window)
        if rearm == True:
            null_time = timer()
            if null_time - jatsa < 3:
                txt_reload =font1.render('perezaryadka', 1, (255, 0, 0))
                window.blit(txt_reload, (325, 300))
            else:
                num_fire = 0
                rearm = False 
        motherfuckers.update()
        motherfuckers.draw(window)
        cherti.update()
        cherti.draw(window)
        text_lose = font1.render('Пропущено' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        text = font1.render('Счёт' + str(penis), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        sprites_list = sprite.groupcollide(motherfuckers, bullets, True, True)
        for i in sprites_list:
            penis += 1
            motherfucker = Enemy('ufo.png', randint(5, 480), 10, 1)
            motherfuckers.add(motherfucker)
        sprites_list2 = sprite.groupcollide(motherfuckers, bullets2, True, True)
        for i in sprites_list2 :
            penis += 1
            motherfucker = Enemy('ufo.png', randint(5, 480), 10, 1)
            motherfuckers.add(motherfucker)
        
        if penis > 100:
            break
        if sprite.spritecollide(her, motherfuckers, False):
            finish = True
            
        if sprite.spritecollide(her, cherti, False):
            finish = True

    else:
        break

    display.update()