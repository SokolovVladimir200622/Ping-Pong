#класс-родитель для спрайтов 
life = 0
start = font.SysFont('Corbel', 50).render('Нажми цифру чтобы начать', True, (255, 255, 255))  # сообщение о старте
start_diff = font_subtitles.render('1 - Легко, 2 - Норм, 3 - Капец', True, (0, 255, 255))  # выбор сложности
class Difficult():
    """Класс отвечает за сложность в игре. 
    Кстати, данная подсказка будет показываться 
    каждый раз при объявлении класса. Попробуй
    навести указатель на имя класса в любом 
    месте программы."""
    def __init__(self, goal=3, max_lost=3, max_life=3, ):
        self.goal = goal # столько кораблей нужно сбить для победы
        self.max_lost = max_lost # проиграли, если пропустили столько
        self.max_life = max_life # нужно для рестарта, тут храним максимальное количество жизней
        # храним через сколько набранных очков придёт босс
class GameSprite(sprite.Sprite):
    #конструктор класса
       #конструктор класса
    def _init_(self, player_image, player_x, player_y, player_speed, wight, height): # добавить еще два параметра при создании и задавать размер прямоугольгника для картинки самим
        super()._init_()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height)) # вместе 55,55 - параметры
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#Игровая сцена:
#back = (143, 233, 222) # цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
#window.fill(back)
background = transform.scale(image.load('ack.jpg'),(win_width,win_height))

#флаги отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
show_hud = True
#создания мяча и ракетки    
racket1 = Player('hero.png', 30, 200, 4, 50, 150) # при созданни спрайта добавляется еще два параметра
racket2 = Player('hero.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball1.png', 200, 200, 4, 50, 50)

font.init()
font = font.SysFont('Times New Roman', 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 2
speed_y = 2
def make_frame():
    if show_hud or finish: # отрисовка худа будет производиться принудительно при конце игры
        window.blit(font2.render("Счет: " - str(max_life) + "/" + str(difficult.goal), 1, (255, 255, 255)), (10, 20))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:

        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        # если мяч достигает границ экрана меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        # если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        elif e.key == K_1 and first_start:
                difficult = Difficult() # стандартные значения соответсвуют легкой сложности
                life = max_life
                
                select_sound.play()
                mixer.music.play() # воспроизводим музыку только при начале игры
                first_start = False
                make_ememies()
                
            # средний уровень сложности
            elif e.key == K_2 and first_start:
                difficult = Difficult(3, 3,)
                speed_x = +2
                speed_y = +2
                player_speed = +1
                 # воспроизводим музыку только при начале игры
                first_start = False
                make_ememies()
                
            # сложный уровень сложности
            elif e.key == K_3 and first_start:
                difficult = Difficult(300, 5, 3, 10, 3, 10)
                speed_x = +3
                speed_y = +3
                player_speed = +2
                 # воспроизводим музыку только при начале игры
                first_start = False
                make_ememies()
                
            # рестарт - клавиша R, сработает только если игра закончена
            if show_hud:
                    # задаем разный цвет в зависимости от кол-ва жизней
                    if life >= max_life or life > 2:
                        life_color = (0, 150, 0)
                    elif life == 2:
                        life_color = (150, 150, 0)
                    else:
                        life_color = (150, 0, 0)

                    text_life = font2.render("♥ " + str(life), 1, life_color)
                    window.blit(text_life, (730, 10))

                
                
                
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
