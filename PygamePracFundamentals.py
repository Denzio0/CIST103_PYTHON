import pygame
pygame.init()

#SETS UP THE DISPLAY (WIDTH HEIGHT AND ITS WINDOW NAME)
win = pygame.display.set_mode((350, 350)) #surface/window
pygame.display.set_caption("DENZIO FIRST GAME") #window name

winSize = 350 #Initialize to be used in Boundary Restriction

#ATTRIBUTES OF THE CHARACTER FIRST
x = 30
y = 30
width = 35
height = 40
vel = 4
rad = 60

isJump = False #initialize as NOT JUMPING
jumpCount = 10

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
            #THEN ADD THE BOUDARY RESTRICTIONS USING LOGICAL OPERATORS and THE COORDINATES
        
        if keys [pygame.K_a] and x > vel: #In this case vel is 4
            x -= vel
        if keys [pygame.K_d] and x < winSize - width - vel: #to restrict to the right THE X COORDS must not be bigger than THE DIFFERENCE OF WIN, THE WIDTH OF THE CHARACTER AND THE VELOCITY
            x += vel

        if not (isJump):
            if keys [pygame.K_w] and y > vel: #In this case vel is 4
                y -= vel
            if keys [pygame.K_s] and y < winSize - height - vel:#to restrict to the right THE Y COORDS must not be bigger than THE DIFFERENCE OF WIN, THE HEIGHT OF THE CHARACTER AND THE VELOCITY
                y += vel

            #KNOW WHEN THE USER WANT TO JUMP
                #JUMP = PARABOLA (FASTER TO SLOWER)
                    #PUT A RESTRICTION TO THE UP AND DOWN BUTTON WHEN JUMPING
            if keys [pygame.K_SPACE]:
                isJump = True #now the user wants to jump
    #THE EVENT WHEN THE USE ACTUALLY JUMPS
        else:
            if jumpCount >= -10: #negative to follow the parabola/quadratic fromula
                neg = 1 #THE CHARACTER IS STILL ABOVE THE AIR
                if jumpCount < 0: #THE CHARACTER IS NOW FALLING DOWN BACAUSE OF THE DECREMENT IN Y
                    neg = -1 #THE CHARACTER WILL NOW FALL DOWN
                y -= (jumpCount ** 2) * 0.5 * neg #moves the character UP
                jumpCount -= 1 #moves the jump up starting to slow
            else:
                isJump = False
                jumpCount = 10

    #CHARACTER DRAWING: DRAWING YOU CHARACTER REQUIRES THE SURFACE (IN THIS CASE ThE SURFACE IS "win" aboce the codes)
    #THE COLORS USES RGB COORDINATES
    #THEN DECLARE THE X, Y, WIDTH, HEIGHT INITIALIZED ON THE ATTRIBUTES ABOVE
    #THE CHARACTER WONT  SHOW UP NOT UNLESS YOU REFRESH IT
    #CIRCLE HEIGTH = RADIUS
        #(SURFACE, COLOR, ATTRIBUTES)

    win.fill((0,0,0)) #fill the leftover trail in the surface with black 
    pygame.draw.rect(win, (235, 152, 52), (x, y, width, height))
    pygame.display.update()
            
pygame.quit()

