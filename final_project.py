import pygame
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((1100,600))

class mainscreen(Sprite):
    def __init__(self, imagefile):
        Sprite.__init__(self)
        self.display = pygame.display.set_mode((1100,600))
        pygame.display.set_caption('Shooter')
        self.image = pygame.image.load(imagefile)
        self.display.blit(self.image, (0,0))
        pygame.mixer.music.load('resident_evil.wav')
        pygame.mixer.music.play()


class zombie(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('zombie.png')
        self.rect = self.image.get_rect()
        self.rect.center = (450,450)

    def change(self):
        self.rect.left = randint(0,900)
        self.rect.top = randint(0,400)

class score(Sprite):
    def __init__(self, score):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont("Times New Roman", 30)
        self.image = self.font.render("%d"%score, 1, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.top = 10
        self.rect.left = 10


class gunsound(Sprite):
    def __init__(self,suara_pistol):
        Sprite.__init__(self)
        pygame.mixer.Sound(suara_pistol).play()

class weapon(Sprite):
    def __init__(self, gun, xpos, ypos):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont("Times New Roman", 30)
        self.image = self.font.render(gun, False, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class menulis1(Sprite):
    def __init__(self,tulisan,xpos,ypos):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render(tulisan,1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class aim(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('target.png')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = mouse.get_pos()


def afterstory():
    text1 = menulis1('for now the enemies have been been pushed back',300,100)
    text2 = menulis1('you must gathered all the people to defeated them',300,250)
    text3 = menulis1('good luck on your next battle',300,400)
    appear = Group()
    text = 0

    while True:
        screen.fill((0,0,0))
        appear.draw(screen)
        display.update()

        e = pygame.event.wait()
        if e.type == MOUSEBUTTONDOWN:
            text += 1
        if text == 1:
            appear.add(text1)
        if text == 2:
            appear.add(text2)
        if text == 3:
            appear.add(text3)
        if e.type == QUIT:
            exit()


suara_pistol = 'handgun.wav'
def mainstart():
    mainscreen("kuburan1.jpg")
    aim1 = aim()
    zombie1 = zombie()
    zombies = Group(zombie1)
    zombies.update(Sprite)
    shoot = 0
    while True:
        screen.fill((0,0,0))
        aim2 = Group(aim1)
        aim2.draw(screen)
        aim2.update()
        mouse.set_visible(0)

        for e in event.get():
            if e.type == QUIT:
                pygame.quit()
                break
            if e.type == MOUSEBUTTONDOWN:
                shoot +=1
                gun = gunsound(suara_pistol)
                if zombie1.rect.collidepoint(mouse.get_pos()):
                    zombie1.change()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    wepselectstart()
        if shoot >= 20:
            afterstory()

        screen.fill((0,0,0))
        mainscreen("kuburan1.jpg")
        zombies.draw(screen)
        aim2.draw(screen)
        pygame.mixer.music.stop()
        pygame.display.update()


def mainarcade():
    mainscreen("kuburan1.jpg")
    skor = 0
    aim1 = aim()
    score1 = score(skor)
    zombie1 = zombie()
    zombies = Group(zombie1,score1)
    zombies.update(Sprite)
    shoot = 0

    while True:
        screen.fill((0,0,0))
        aim2 = Group(aim1)
        aim2.draw(screen)
        aim2.update()
        mouse.set_visible(0)

        for e in event.get():
            if e.type == QUIT:
                pygame.quit()
                break
            if e.type == MOUSEBUTTONDOWN:
                shoot +=1
                gun = gunsound(suara_pistol)
                if zombie1.rect.collidepoint(mouse.get_pos()):
                    skor += 1

                    zombie1.change()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    wepselectarcade()

        screen.fill((0,0,0))
        mainscreen("kuburan1.jpg")
        score1 = score(skor)
        zombies = Group(zombie1, score1)
        zombies.draw(screen)
        pygame.mixer.music.stop()
        pygame.display.update()


def wepselectstart():
    screen = pygame.display.set_mode((1100, 600))
    pygame.display.set_caption('Shooter')
    global suara_pistol
    while True:
        screen.fill((0, 0, 0))
        mouse.set_visible(1)
        weaponmenu = weapon("Weapons :", 0, 0)
        handgun = weapon("Handgun", 100, 100)
        shotgun = weapon("Shotgun", 300, 100)
        sniper = weapon("Sniper",500,100)
        rocket = weapon("Rocket",700,100)
        kopasus = weapon('Bare Hand',900,100)
        exit = weapon("Exit", 0, 500)
        appear = Group(weaponmenu, handgun, shotgun, exit, sniper, rocket, kopasus)
        appear.draw(screen)
        e = event.wait()

        if handgun.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'handgun.wav'
                mainstart()
        if shotgun.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'shotgun2.wav'
                mainstart()
        if sniper.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'sniper.wav'
                mainstart()
        if rocket.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'roket.wav'
                mainstart()
        if kopasus.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'pukul.wav'
                mainstart()
        if exit.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                mainstart()

def wepselectarcade():
    screen = pygame.display.set_mode((1100, 600))
    pygame.display.set_caption('Shooter')
    global suara_pistol
    while True:
        screen.fill((0, 0, 0))
        mouse.set_visible(1)
        weaponmenu = weapon("Weapons :", 0, 0)
        handgun = weapon("Handgun", 100, 100)
        shotgun = weapon("Shotgun", 300, 100)
        sniper = weapon("Sniper",500,100)
        rocket = weapon("Rocket",700,100)
        kopasus = weapon('Bare Hand',900,100)
        exit = weapon("Exit", 0, 500)
        appear = Group(weaponmenu, handgun, shotgun, exit, sniper, rocket, kopasus)
        appear.draw(screen)
        e = event.wait()

        if handgun.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'handgun.wav'
                mainarcade()
        if shotgun.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'shotgun2.wav'
                mainarcade()
        if sniper.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'sniper.wav'
                mainarcade()
        if rocket.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'roket.wav'
                mainarcade()
        if kopasus.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                suara_pistol = 'pukul.wav'
                mainarcade()
        if exit.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                mainarcade()



        display.update()

