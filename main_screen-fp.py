import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from pygame.mixer import *
from final_project import *

pygame.init()

screen = pygame.display.set_mode((1100,600))

class weapon(Sprite):
    def __init__(self, gun, xpos, ypos):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont("Times New Roman", 30)
        self.image = self.font.render(gun, False, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class menulis(Sprite):
    def __init__(self,tulisan,xpos,ypos):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render(tulisan,1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (xpos,ypos)

def story():
    screen.fill((0,0,0))
    text1 = menulis('you survive the last zombie attack',300,100)
    text2 = menulis('now you have to defend yourself now',300,250)
    text3 = menulis('you will be given some weapon',300,400)
    text4 = menulis('*press spacebar to choose your weapon*',300,550)
    appear = Group()
    text = 0


    while True:
        screen.fill((0,0,0))
        appear.draw(screen)
        display.update()


        e = pygame.event.wait()
        if e.type == MOUSEBUTTONDOWN:
            text += 1

        if e.type == QUIT:
            exit()
        if text == 1:
            appear.add(text1)
        elif text == 2:
            appear.add(text2)
        elif text == 3:
            appear.add(text3)
        elif text == 4:
            appear.add(text4)
        elif text == 5:
            mainstart()

def menu():
    menuscreen = mainscreen("main-screen.jpg")

    while True:
        startmenu = weapon('Start',700,150)
        exitmenu = weapon('Exit',700,450)
        arcademenu = weapon('Arcade',700,300)
        appear = Group(startmenu,exitmenu,arcademenu)
        appear.draw(menuscreen.display)
        e = event.wait()

        display.update()

        e = pygame.event.wait()
        if e.type == QUIT:
            pygame.quit()
            break
        if startmenu.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                story()
        if arcademenu.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                mainarcade()
        if exitmenu.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break

        pygame.display.update()
menu()
