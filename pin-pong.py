from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((255, 255, 255))  # Цвет ракетки - белый
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

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

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player(30, 200, 4, 50, 150)
racket2 = Player(520, 200, 4, 50, 150)
ball = GameSprite(200, 200, 4, 50, 50)
ball.image = transform.scale(image.load('tenis_ball.png'), (50, 50))  # Загружаем изображение мяча

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

score1 = 0
score2 = 0

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
      
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x, ball.rect.y = win_width // 2, win_height // 2  # Сброс мяча в центр
            speed_x *= -1  # Меняем направление мяча

        if ball.rect.x > win_width:
            score1 += 1
            ball.rect.x, ball.rect.y = win_width // 2, win_height // 2  # Сброс мяча в центр
            speed_x *= -1  # Меняем направление мяча

        # Отображаем текстовые элементы
        player1_text = font.render(f'Игрок 1: {score1}', True, (0, 0, 0))
        player2_text = font.render(f'Игрок 2: {score2}', True, (0, 0, 0))
        window.blit(player1_text, (10, 10))
        window.blit(player2_text, (win_width - player2_text.get_width() - 10, 10))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
