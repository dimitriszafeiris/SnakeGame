#Snake Game by Dimitris Zafiris

#import modules
import pygame, sys, random, time

check_errors = pygame.init()

# Check errors is a tuple like (x,y)
if check_errors[1] > 0:
        print ("(!) Had {0} initializing errors, exit program...".format(check_errors[1]))
        sys.exit(-1)
else:
    print ("(+) PyGame successfully initialized!")
    
# Create game screen
mainScreen = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")

#Use colors
red = pygame.Color(255,10,10)  # game over
green = pygame.Color(10,255,10)  # snake
black = pygame.Color(0,0,0)   # score
white = pygame.Color(255,255,255)  # background
blue = pygame.Color(10,10,255)  # food

# Game controller (frames per second)
fpsController = pygame.time.Clock()

# Variables for snake and food
snakePos = [200,200] # snake initial position 
snakeBody = [[100,500],[90,500],[80,500]]  # Snake body

foodPosition = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodStatus = True

direction = 'RIGHT'
changeDirection = direction

score = 0
# Game over
def gameOver():
    myFont = pygame.font.SysFont('monaco',67)
    gameOverSurf = myFont.render('Ooops...Game Over!', True, red)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (360,15)
    mainScreen.blit(gameOverSurf,gameOverRect)
    showScore(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit() # exit pygame
    sys.exit() # exit from console

def showScore(choi=1):
    sFont = pygame.font.SysFont('monaco',20)
    scoreSurf = sFont.render('Score: {0}'.format(score), True, black)
    scoreRect = scoreSurf.get_rect()
    if choi == 1:
        scoreRect.midtop = (680,30)
    else:
        scoreRect.midtop = (360,80)
    mainScreen.blit(scoreSurf,scoreRect)
    
# Start game
while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'): # check if key is d
                changeDirection = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'): # check if key is a
                changeDirection = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'): # check if key is w
                changeDirection = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'): # check if key is s
                changeDirection = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
    # allowed change directions
    if changeDirection == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeDirection == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeDirection == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeDirection == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
        
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
        
    # Snake body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPosition[0] and snakePos[1] == foodPosition[1]:
        score += 1
        foodStatus = False
    else:
        snakeBody.pop()
    
    if foodStatus == False:
        foodPosition = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodStatus = True
        
    mainScreen.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(mainScreen, green,
        pygame.Rect(pos[0],pos[1],10,10))
 
    pygame.draw.rect(mainScreen, blue,
    pygame.Rect(foodPosition[0],foodPosition[1],10,10))
    
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    
    showScore()
    pygame.display.flip()
    fpsController.tick(22)