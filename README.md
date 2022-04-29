В данном проэкте показана первая версия игры Пинг Понг 
-----------------------------------------------------------
----------------------------------------------------------
В этой игре главная цель создать полную игру пинг Понг но это только первая версия и в первой версии мы можем передвигать персонажей с помощью кнопок W,s и up,down 
---------------------------------------------------------------------------------------------------------------------------------------------------


![2022-04-29 (2)](https://user-images.githubusercontent.com/104199450/165937288-a37eb6a9-3d1c-48da-9dd4-7fa26144c8c2.png)

в данном коде мы импортировали данные pygame потом создали суперкласс и переменные для спрайтов после этого создали создали размеры окна и настройки персонажа после этого подключили все что нам нужно для экрана и создали игровой цикл в котором создали отрисовку персонажей,функцию для закрытия окна и обновление экрана
=================================================================================================================================================
from pygame import*

ing_hero = "hero.png"
ing_back = "ack.jpg"

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_height = 500
win_width = 700
Players = Player(ing_hero,550 , 120, 120, 120, 20)
Players2 = Player2(ing_hero,5, 120, 120, 120, 20)


win = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(image.load(ing_back), (win_width, win_height))
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e  in event.get():
        if e.type == QUIT:
            game = False
        
    if not finish:
        win.blit(background,(0,0))
        Players.reset()
        Players.update()
        Players2.reset()
        Players2.update()
            
        
        display.update()
        
                                                                                                                                                =
    time.delay(50)                                                                                                                              =
=================================================================================================================================================


