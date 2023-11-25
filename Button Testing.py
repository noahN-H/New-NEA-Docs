import pygame, os
import Button

pygame.init()


screen = pygame.display.set_mode((970,646))
pygame.display.set_caption("Main Menu")

#buttons

startImage = pygame.image.load("NEA Documents/Images/Start_Button.png").convert_alpha() 
quitImage = pygame.image.load("NEA Documents/Images/Exit_button.png").convert_alpha()
instructionsImage = pygame.image.load("NEA Documents/Images/Instructions_Button.png").convert_alpha()
spaceBG = pygame.image.load("NEA Documents/Images/space-background.jpg").convert_alpha()


#making the buttons work
startButton = Button.button(200, 200, startImage,7)
instructionsButton = Button.button(200, 300, instructionsImage,7)    
quitButton = Button.button(200, 400,quitImage,7)
        
        

#game loop
run = True
while run:
    
    screen.blit(spaceBG,(0,0))
    
    if startButton.draw(screen) == True:
        print("START")
        screen.blit(7,68,102)
    if quitButton.draw(screen) == True:
        run = False
        print("EXIT")
    if instructionsButton.draw(screen) == True:
        print("Instructions")
    
  #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()