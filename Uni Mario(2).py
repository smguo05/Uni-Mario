import pygame
import sys
import pygame.sprite as sprite
pygame.init()

pygame.display.set_caption("Uni Mario")


m_x = 100
m_y = 350
width = 40
height = 60
vel = 5

left=False
right=False
walk_cousnt = 0
walkRight = []
walkLeft = []

theClock = pygame.time.Clock()

background_image = pygame.image.load('Sprites/bg1.png')
background_size = background_image.get_size()
background_rect = background_image.get_rect()
sw = 840
sh = 464
win = pygame.display.set_mode((sw, sh))
w,h = background_size

bg_x1 = 0
bg_y1 = 0

bg_x2 = w
bg_y2 = 0

def load_img(file_name): # loads the image, makes the pure white background transparent
    img = pygame.image.load(file_name).convert()
    img.set_colorkey((255,255,255))

    return img

for i in range(1,7):
    walkLeft.append( load_img("Sprites/L" + str(i) + ".png" ) ) #loads in lists of images
    walkRight.append( load_img("Sprites/R" + str(i) + ".png") ) 

player_image = walkRight[0]

pygame.mixer.music.load('Music/bensound-summer.mp3')
pygame.mixer.music.play(-1)

isJump = False
jumpCount = 10

left_idx=0
right_idx=0

run = True #main loop
while run:
    pygame.time.delay(50)
    
    win.blit(background_image,(sw, sh)) #makes a scrolling background 
    pygame.display.update()
    
    bg_x2 -= 5
    bg_x1 -= 5
    if bg_x1 < sw - 2*w:
       bg_x1 = 0
    if bg_x2 < sw - w:
       bg_x2 = w

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                                             
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and m_x > vel: 
        m_x -= vel
        if not isJump:
            player_image = walkLeft[left_idx]
            left_idx += 1
            if left_idx >= len(walkLeft):
                left_idx=0
        
    if keys[pygame.K_RIGHT] and m_x < sw - width - vel:
        m_x += vel
        if not isJump:
            player_image = walkRight[right_idx]
            right_idx += 1
            if right_idx >= len(walkRight):
                right_idx=0
        
    if not(isJump):      
        if keys[pygame.K_UP]:
            isJump = True
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            m_y -= (jumpCount ** 2)* 0.25 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

            
    win.blit(background_image,(bg_x1,bg_y1))
    win.blit(background_image,(bg_x2,bg_y2))
    win.blit(player_image, (m_x,m_y))
  
    pygame.display.update()
    theClock.tick(500)


        




pygame.quit()
