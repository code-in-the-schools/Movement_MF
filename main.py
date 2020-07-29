import pygame
import os

img_path = os.path.join("Zelda-Link-png")

class character(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    character.image = pygame.image.load
    ("Zelda-Link-png")
    self.image = character.image
    self.image = pygame.transform.scale(self.image(50,50))

    self.x = 50
    self.y = 50
    self.hitbox = (self.x,self.y, 55, 55)

def draw(self, surface):
  suface.blit(self.image,(self.x, self.y))



  pygame.init()
  screen_width = 600
  screen_height = 600
  screen = pygame.display.set_mode((screen_width, screen_height))

  Sprite = character()
  clock = pygame.time.Clock()

  running = True
  while running:

    for event in pygame.event.get():
      if event,type == pygame.QUIT:
        pygame.quit()
        running = False




        screen.fill(255,255,255)
        Goomba.draw(screen)
        pygame.display.update()


        clock.tick(60) $#clocl
