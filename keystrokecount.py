#initialize

import pygame
pygame.init()

#initializing the count variables
count_m = 0
count_n = 0

# Making dictionaries with settings for everything.
display = {
    "width": 800,
    "height": 600
}
# creating a window, and launching our game
win = pygame.display.set_mode((display["width"], display["height"])) 
# 800 width, 600 height

# creating a font to write the score
myfont = pygame.font.SysFont('monospace', 20) 


#setting up the while loop 
while True:
  pygame.time.delay(50)
  win.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      break

#Get the pressed key
    keys = pygame.key.get_pressed()

    if keys[pygame.K_n]:
      count_n = count_n + 1
    if keys[pygame.K_m]:
      count_m = count_m + 1

#this portion is to write the score on to the screen
#defines the font and font color
    textsurface = myfont.render("score: Count of m {0}/ Count of n {1}".format(count_n, count_m), False, (255, 255, 255))
#defines the position of the score
    win.blit(textsurface, (10, 500))
    pygame.display.update()

pygame.quit()
