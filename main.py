import pygame
import random
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
 
img_path = os.path.join('Paddle.png')

class Paddle(object):
  def __init__(self)
   pygame.sprite.Sprite.__int__(self)
   Paddle.image = pygame.imagel.load("Paddle.png")
   self.image = Paddle.image
   self.imagle = pygame.transform.scale(self,imagle,(15,100))
   self.x = 15
   self.y = 100
   self.hitbox = (self.x self.y)

  def draw(self, surface):
    surface.blit(self.image, (self.x, self,y))

  def movement(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]
     self.y += 1
    if key[pygame.K_UP]:
      self.y -= 1
class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ball
 
 
def main():
    """
    This is our main program.
    """
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing Balls")
 
    done = False
 
    clock = pygame.time.Clock()
 
    ball_list = []
 
    ball = make_ball()
    ball_list.append(ball)
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)
 
        for ball in ball_l
            ball.x += ball.change_x
            ball.y += ball.change_y
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
 
        screen.fill(BLACK)
 
      
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)
 
        
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
def main()
pygame.display.set_caption('Pong') screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
	
	paddle_width = 15
	paddle_height = 100
	
	paddle = pygame.Surface((paddle_width, paddle_height))
 self.image = Paddle.image

	clock = pygame.time.Clock()
	play = True
	screen.fill(WHITE)

	while play:
	 	pygame.event.get()
	 	
		clock.tick
		pygame.display.flip()	

