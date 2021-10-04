import pygame
pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()
screen.blit(background_image,[0,0])
BLUE=(0,0,255)
player=pygame.Rect(200,200,30,30)
pygame.draw.rect(screen,BLUE,player)
WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
pygame.draw.rect(screen,WHITE,enemy)

# Create a variable 'xvel' and assign the value '2' to it


# Game loop
while True:
    # Code to close the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Inside the loop - Start coding here
    # Increment 'enemy.x' with 'xvel'
    
    
    # Checking for condition 1 or condition 2
    
    
    # Adding the background image and drawing the rectangles
    
    
    # Updating the screen display
    pygame.display.update()
    
    # Setting the maximum number of frames
    

    

 
