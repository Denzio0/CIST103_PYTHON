import pygame
pygame.init()

#SETS UP THE DISPLAY (WIDTH HEIGHT AND ITS WINDOW NAME)
win = pygame.display.set_mode((350, 350)) #surface/window
pygame.display.set_caption("DENZIO FIRST GAME") #window name

#ATTRIBUTES OF THE CHARACTER FIRST
x = 30
y = 30
width = 35
height = 40
vel = 4
rad = 60

#MAIN LOOP - ALL PYGAME STARTS WITH A MAIN LOOP (TO DETECT MAIN EVENTS LIKE COLLISION, MOVEMENTS, ETC)
#EVENTS ARE EVERYTHING THE USER DO IN THE GAME

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #FOR THE CHARACTER TO MOVE WE NEED TO USE THE KEY PYGAME FUNCTION
    #KEY = K.DIRECTION
    #PYTHON COORDINATES (0,0) STARTS AT THE UPPER LEFT AND NOT AT THE CENTER LIKE THE USUAL CARTESIAN PLANE
    #LEFT TO RIGHT = X COORDS
    #UP TO DOWN = Y COORDS

        keys = pygame.key.get_pressed() #main key function
            #vel = x, y, height, & width variables
            #delay also plays a role here
            #pygame.K_"KEYS YOU WANT TO TOGGLE"
        if keys [pygame.K_a]:
            x -= vel
        if keys [pygame.K_d]:
            x += vel
        if keys [pygame.K_w]:
            y -= vel
        if keys [pygame.K_s]:
            y += vel

    #CHARACTER DRAWING: DRAWING YOU CHARACTER REQUIRES THE SURFACE (IN THIS CASE ThE SURFACE IS "win" aboce the codes)
    #THE COLORS USES RGB COORDINATES
    #THEN DECLARE THE X, Y, WIDTH, HEIGHT INITIALIZED ON THE ATTRIBUTES ABOVE
    #THE CHARACTER WONT  SHOW UP NOT UNLESS YOU REFRESH IT
    #CIRCLE HEIGTH = RADIUS
        #)SURFACE, COLOR, ATTRIBUTES)

    win.fill((0,0,0)) #fill the leftover trail in the surface with black 
    pygame.draw.rect(win, (235, 152, 52), (x, y, width, height))
    pygame.display.update()
            
pygame.quit()

