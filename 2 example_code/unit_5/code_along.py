import pygame, sys, random

# --- Global Variables ---
screen_width = 1280
screen_height = 960

'''---------------------------------SPRITES/CLASSES---------------------'''

class Player(pygame.sprite.Sprite):
    def __init__(self, initial_pos, size, color):
        super().__init__() # Important: Initialize the parent Sprite class

        # Appearance
        self.image = pygame.Surface([size, size]) # Create a square surface
        self.image.fill(color) # Fill it with the chosen color

        # Position and Movement
        self.rect = self.image.get_rect(center = initial_pos) # Get the rectangle hitbox, positioned at initial_pos

        # Speed - random initial direction
        self.speed_x = 5 * random.choice((1, -1)) # Pixels per frame horizontally
        self.speed_y = 5 * random.choice((1, -1)) # Pixels per frame vertically

    def update(self):
        """Called once per frame. Handles movement and bouncing."""
        # Move the sprite
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off screen edges
        # Left edge
        if self.rect.left <= 0:
            self.rect.left = 0 # Prevent getting stuck slightly off-screen
            self.speed_x *= -1 # Reverse horizontal speed
        # Right edge
        if self.rect.right >= screen_width:
            self.rect.right = screen_width # Prevent getting stuck
            self.speed_x *= -1
        # Top edge
        if self.rect.top <= 0:
            self.rect.top = 0 # Prevent getting stuck
            self.speed_y *= -1 # Reverse vertical speed
        # Bottom edge
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height # Prevent getting stuck
            self.speed_y *= -1

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


'''----------------------------------LOOP-------------------------------'''
while True:
    # --- Handling input (EVENTS) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Add other event handling here later (like key presses)

    # --- Game Logic Updates ---
    # Call the update() method on ALL sprites in the group
    all_sprites.update() # This automatically calls player_sprite.update()

    # --- Drawing ---
    screen.fill('grey20') # Fill screen with a dark grey color

    # Draw ALL sprites in the group onto the screen surface
    all_sprites.draw(screen)

    # --- Updating the window ---
    pygame.display.flip() # Show the newly drawn frame
    clock.tick(60)       # Limit frame rate to 60 FPS