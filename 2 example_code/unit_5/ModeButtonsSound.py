import pygame, sys, random

#global variables
screen_width = 800
screen_height = 600

'''---------------------------------SPRITES/CLASSES---------------------'''
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/water-border.jpg')
        self.rect = self.image.get_rect()

class Message(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/message-start.png')
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width/2, screen_height/2)

class StarFish(pygame.sprite.Sprite): #button-ish
    click_sound = 0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/starfish.png')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width-self.rect.width)
        self.rect.y = random.randint(0, screen_height-self.rect.height)

        if StarFish.click_sound == 0:
            StarFish.click_sound = pygame.mixer.Sound('assets/smb_powerup.wav')
        if StarFish.click_sound == 1:
            StarFish.click_sound = pygame.mixer.Sound('assets/hit.mp3')



    def clicked(self, mouse):
        if self.rect.collidepoint(mouse):
            #print('clicked')
            pygame.mixer.Sound.play(StarFish.click_sound)
            self.kill()

def main():
    '''---------------------------------SETUP-------------------------------'''
    # General setup
    pygame.init()
    clock = pygame.time.Clock()
    mode = 0    #0:start screen, 1: gameplay

    # Setting up the main window
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Game Title')

    # Define Custom Events

    # Instantiate objects and groups
    bg_group = pygame.sprite.Group()
    bg_group.add(Background())
    open_message = Message()
    bg_group.add(open_message)

    star_group = pygame.sprite.Group()
    for i in range(5):
        star_group.add(StarFish())

    #Music
    pygame.mixer.music.load('assets/Super Mario Bros.mp3')
    pygame.mixer.music.play(-1) #number: play that many times, 0/1/empty: play once, -1: inf loop 
    
    '''----------------------------------LOOP-------------------------------'''
    while True:
        #print(mode)
        #Handling input (EVENTS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if mode == 0 and event.key == pygame.K_s:
                    mode = 1
                    open_message.kill()
                if event.key == pygame.K_p:
                    mode = 0
                    bg_group.add(open_message)
            if mode == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                for star in star_group:
                    star.clicked(pygame.mouse.get_pos())

        #Updating Sprites

        # Drawing
        screen.fill('black') #replace with image or whatever you use up top
        bg_group.draw(screen)
        if mode == 1:
            star_group.draw(screen)
            

        # Updating the window
        pygame.display.flip()
        clock.tick(60)

main()
