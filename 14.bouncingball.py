import pygame
import random
import sys
#Define color
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
orange = (255,113,0)


winx,winy = 300,300
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Bouncing Ball")

# ball info
bwidth, bheight = 20, 20
bpx, bpy = random.randint(0,winx-bwidth),0


#display score
score = 0
level = int(input("Enter the level\n Easy: 20\nMedium: 40\nHard:60\nKhatarnak: 80"))

#padle size
pwidth = 70
pheight = 10
move = 40
x, y = int(winx/2),winy-pheight
run = True

#main loop 
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x >= 10:
        	x -= move
    if keys[pygame.K_RIGHT]:
        if x <=220:
        	x += move
    if bpy < 279:
    	#speed of ball 40
    	bpy = bpy + level
    else:
    	bpy = 0
    	bpx = random.randint(0,winx-bwidth)
    # check and update for score
    if (bpx+bwidth) >= x and bpx <= (x+pwidth):
    	if (bpy+bheight) >= y:
    		score = score + 1
    		print("Your Score: ",score)
    win.fill(white)
    pygame.draw.rect(win,orange,(bpx,bpy,bwidth,bheight))
    pygame.draw.rect(win,black,(x,y,pwidth,pheight))
    pygame.display.update()
pygame.quit()



