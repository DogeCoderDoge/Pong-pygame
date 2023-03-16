import pygame

pygame.init()
screen = pygame.display.set_mode((900,600))
screen_rect = screen.get_rect()
pygame.display.set_caption('Pong - DogeCoderDoge')

WHITE = (255,255,255)
GRAY = (155,155,155)
BLUE = (0,100,255)
RED = (255,0,50)
FONT = pygame.font.Font('American Captain.ttf', 50)

clock = pygame.time.Clock()
background = pygame.image.load('background.png')

paddle1_move = 0
paddle2_move = 0

paddleTouched = False
paddle1_score = 0
paddle2_score = 0

class Ball:
    def __init__(self, x, y, velY, velX, radius):
        self.x = x
        self.y = y
        self.velY = velY
        self.velX = velX
        self.radius = radius

    def move(self, velY, velX):
        self.y += velY
        self.x += velX

    def draw(self):
        ball = pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def reset(self):
        self.x = 443
        self.y = 275

class Paddle:
    def __init__(self, x, y, color):
        self.y = y
        self.x = x
        self.color = color

    def move(self, velY):
        self.y += velY

    def draw(self):
        rect = pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 10, 120))
        
paddle1 = Paddle(20, 230, BLUE)
paddle2 = Paddle(880, 230, RED)

ball = Ball(443, 275, 4, 4, 15) #x,y,vely,velx


while True:
    ballRect = pygame.Rect(ball.x-15, ball.y-15, 30, 30)

    paddle1_Rect = pygame.Rect(paddle1.x, paddle1.y, 10, 120)
    paddle2_Rect = pygame.Rect(paddle2.x, paddle2.y, 10, 120)

    clock.tick(100)
    screen.blit(background, (0,0))
    
    paddle1_score_text = FONT.render(str(paddle1_score), False, WHITE)
    paddle2_score_text = FONT.render(str(paddle2_score), False, WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                paddle1_move = -1
            elif event.key == pygame.K_w:
                paddle1_move = 1

            if event.key == pygame.K_DOWN:
                paddle2_move = -1
            elif event.key == pygame.K_UP:
                paddle2_move = 1

    if paddle1_move == -1: paddle1.move(4)
    elif paddle1_move == 1: paddle1.move(-4)
    
    if paddle2_move == -1: paddle2.move(4)
    elif paddle2_move == 1: paddle2.move(-4)

    if ball.y <= 15 or ball.y >= 585: 
        ball.velY *= -1
        #print("ball is touching horizontal walls")
        
    if pygame.Rect.colliderect(ballRect, paddle1_Rect) :
        middle = paddle1.y + 60 #paddle1.y + paddle1.height/2 to find the middle of paddle
        reduction_factor = 12
        y_vel = (middle - ball.y) / reduction_factor
        ball.velY = -1 * y_vel
        ball.velX *= -1
        #print("ball and paddle collide")

    elif pygame.Rect.colliderect(ballRect, paddle2_Rect):
        middle = paddle2.y + 60 #paddle1.y + paddle1.height/2 to find the middle of paddle
        reduction_factor = 12
        y_vel = (middle - ball.y) / reduction_factor
        ball.velY = -1 * y_vel
        ball.velX *= -1

    if ball.x <= 20:
        paddle2_score += 1
        ball.reset()
        #print("paddle2 gets point")

    elif ball.x >= 880:
        ball.reset()
        paddle1_score += 1
        #print("paddle1 gets point")

    if paddle1.y <= 0 or paddle1.y >= 480:
        paddle1_move *= -1
    if paddle2.y <= 0 or paddle2.y >= 480:
        paddle2_move *= -1  

    paddle1.draw()
    paddle2.draw()
    ball.draw()

    ball.move(ball.velY, ball.velX)

    screen.blit(paddle1_score_text, (200, 20))
    screen.blit(paddle2_score_text, (700, 20))

    pygame.display.update()

