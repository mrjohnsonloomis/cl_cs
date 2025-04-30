import pygame, sys, random

# --- Global Variables ---
screen_width = 1280
screen_height = 960

'''---------------------------------SPRITES/CLASSES---------------------'''
class Background(pygame.sprite.Sprite):
    def __init__(self, which):
        super().__init__()
        self.image = pygame.image.load('assets/cityclose.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (which*self.rect.width, 0)
        self.speed = -5

    def update(self):
        
        self.rect.x += self.speed

        if self.rect.right < 0:
            self.rect.x += self.rect.width*2

class Player(pygame.sprite.Sprite):
    def __init__(self, initial_pos, size, color):
        super().__init__() # Important: Initialize the parent Sprite class

        # Appearance
        self.image = pygame.image.load('assets/coin.png')
        #self.image.fill(color) # Fill it with the chosen color

        # Position and Movement
        self.rect = self.image.get_rect(center = initial_pos) # Get the rectangle hitbox, positioned at initial_pos

        # Speed
        self.speed = 5

    def change_look(self):
        costume_list = ['assets/necklace_green.png', 'assets/necklace_green.png', 'assets/potion_red.png']
        self.image = pygame.image.load(random.choice(costume_list))


    def update(self):
        """Called once per frame. Handles player movement based on key presses."""
        # Get a dictionary of all currently pressed keys
        keys = pygame.key.get_pressed()

        # Move left/right
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Move up/down
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # --- Keep Player On Screen ---
        # Use clamp_ip() to modify the rect *in-place* so it stays within screen bounds
        self.rect.clamp_ip(screen.get_rect())

'''---------------------------------SETUP-------------------------------'''
# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Bouncing Box')

# Define Custom Events
# (None needed for this simple example)

# Instantiate objects and groups
# Create the player sprite instance
player_sprite = Player(initial_pos=(screen_width // 2, screen_height // 2), size=50, color='red')

# Create a sprite group (essential for managing sprites)
# 'GroupSingle' is efficient if you know you'll only ever have one sprite of this type.
# 'Group' is more general if you plan to add more later. Let's use Group for good practice.
all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite) # Add our player instance to the group

bg_group = pygame.sprite.Group()
bg_group.add(Background(0), Background(1))

'''----------------------------------LOOP-------------------------------'''
while True:
    # --- Handling input (EVENTS) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Add other event handling here later (like key presses)
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 # Change image on spacebar press
                 for sprite in all_sprites:
                     sprite.change_look()

    # --- Game Logic Updates ---
    # Call the update() method on ALL sprites in the group
    bg_group.update()
    all_sprites.update() # This automatically calls player_sprite.update()

    # --- Drawing ---
    screen.fill('orange') # Fill screen with a dark grey color

    # Draw ALL sprites in the group onto the screen surface
    bg_group.draw(screen)
    all_sprites.draw(screen)
    
    # --- Updating the window ---
    pygame.display.flip() # Show the newly drawn frame
    clock.tick(60)       # Limit frame rate to 60 FPS