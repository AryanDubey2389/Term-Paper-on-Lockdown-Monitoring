screen = [1, 1, 2, 2, 2, 1]
print screen
[1, 1, 2, 2, 2, 1]
screen[3] = 8
print screen
[1, 1, 2, 8, 2, 1]
background = [1, 1, 2, 2, 2, 1]
screen = [0]*6                         #a new blank screen
for i in range(6):
    screen[i] = background[i]
print screen
[1, 2, 2, 2, 1]
playerpos = 3
screen[playerpos] = 8
print screen
[1, 1, 2, 8, 2, 1]
print screen
[1, 2, 8, 2, 1]
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print screen
[1, 1, 8, 2, 2, 1]
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print screen
[1, 8, 2, 2, 2, 1]
background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
screen = create_graphics_screen()
for i in range(6):
    screen.blit(background[i], (i*10, 0))
playerpos = 3
screen.blit(playerimage, (playerpos*10, 0))
screen.blit(background[playerpos], (playerpos*10, 0))
playerpos = playerpos - 1
screen.blit(playerimage, (playerpos*10, 0))
screen = create_screen()
player = load_player_image()
background = load_background_image()
screen.blit(background, (0, 0))        #draw the background
position = player.get_rect()
screen.blit(player, position)          #draw the player
pygame.display.update()                #and show it all
for x in range(100):                   #animate 100 frames
    screen.blit(background, position, position) #erase
    position = position.move(2, 0)     #move player
    screen.blit(player, position)      #draw new player
    pygame.display.update()            #and show it all
    pygame.time.delay(100)             #stop the program for 1/10 second
player = pygame.image.load('player.bmp').convert()
background = pygame.image.load('liquid.bmp').convert()
screen = pygame.display.set_mode((640, 480))
while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    move_and_draw_all_game_objects()
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('player.bmp').convert()
background = pygame.image.load('background.bmp').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(10):                    #create 10 objects</i>
    o = GameObject(player, x*40, x)
    objects.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)