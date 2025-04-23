import pygame
import sys
import random
import os # Used to help locate assets

# --- Global Variables ---
screen_width = 1280
screen_height = 720 # Adjusted for a more common aspect ratio

# --- Asset Filepaths ---
# !! IMPORTANT !!
# Create a folder named 'assets' in the same directory as your script.
# Place your image and sound files inside this 'assets' folder.
# If these files are missing, the program WILL crash.
# Images: player.png, collectible.png, obstacle.png (suggested size: ~30x30 to 50x50 pixels)
# Sound: background.mp3 (longer music file), collect.wav, hit.wav (short sound effects)
asset_folder = 'assets'

# Helper function to get asset paths (makes it easier if script/assets are moved)
def get_asset_path(filename):
    """Constructs the full path to an asset in the 'assets' folder."""
    return os.path.join(asset_folder, filename)

# --- Colors (Optional in our games - Can be useful for debugging rects) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

'''---------------------------------SPRITES/CLASSES---------------------'''

class Player(pygame.sprite.Sprite):
    """Represents the player character, controlled by arrow keys."""
    def __init__(self):
        super().__init__() # Initialize the parent Sprite class

        # --- Image Loading ---
        # Load the image from the assets folder. Program will crash if not found.
        # .convert_alpha() optimizes the image format for faster drawing, including transparency
        # I'm also doing a nifty scaling of the image...otherwise it would just be what's in parentheses
        self.image = pygame.transform.scale(pygame.image.load(get_asset_path('player.png')), (65, 65))
        
        # --- Position and Rectangle ---
        # Get the rectangle (hitbox) for the image
        self.rect = self.image.get_rect()
        # Set the initial position to the center of the screen
        self.rect.center = (screen_width // 2, screen_height // 2)

        # --- Movement ---
        self.speed = 6 # Player movement speed in pixels per frame

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


class Collectible(pygame.sprite.Sprite):
    """Represents items the player should collect."""
    def __init__(self):
        super().__init__()

        # Load image. Program will crash if not found.
        self.image = pygame.image.load(get_asset_path('collectible.png')).convert_alpha()

        self.rect = self.image.get_rect()
        # Spawn at a random position on the screen
        # Ensure spawn position accounts for image size to avoid immediate clipping issues
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, screen_height - self.rect.height)

    # No update needed for static collectibles


class Obstacle(pygame.sprite.Sprite):
    """Represents obstacles the player should avoid."""
    def __init__(self):
        super().__init__()

        # Load image. Program will crash if not found.
        self.image = pygame.image.load(get_asset_path('obstacle.png')).convert_alpha()

        self.rect = self.image.get_rect()
        # Spawn at a random position
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, screen_height - self.rect.height)

        # --- Movement (like the bouncing box example) ---
        self.speed_x = random.choice([-3, -2, 2, 3]) # Random initial speed/direction
        self.speed_y = random.choice([-3, -2, 2, 3])

    def update(self):
        """Called once per frame. Handles obstacle movement and bouncing."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off screen edges
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x *= -1
            self.rect.clamp_ip(screen.get_rect()) # Prevent getting stuck
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
            self.rect.clamp_ip(screen.get_rect()) # Prevent getting stuck

'''---------------------------------SETUP-------------------------------'''
# --- Pygame Initialization ---
pygame.init()
# --- Mixer Initialization (for sound) ---
# Needs to be initialized separately to use sound features.
# Program may crash here if sound drivers have issues.
pygame.mixer.init()

# --- Screen Setup ---
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collector Game Example')

# --- Clock (for controlling frame rate) ---
clock = pygame.time.Clock()

# --- Font Initialization (for displaying text) ---
# Use a default system font. Program may crash if fonts unavailable.
game_font = pygame.font.Font(None, 36) # Font object, size 36

# --- Sound Loading ---
# Program will crash if sound files are not found in 'assets' folder.
# Background music (.ogg is generally preferred for longer tracks)
pygame.mixer.music.load(get_asset_path('background.mp3'))
pygame.mixer.music.set_volume(0.4) # Set volume (0.0 to 1.0)

# Sound effects (.wav is good for short effects)
collect_sound = pygame.mixer.Sound(get_asset_path('collect.ogg'))
hit_sound = pygame.mixer.Sound(get_asset_path('hit.mp3'))
collect_sound.set_volume(0.6)
hit_sound.set_volume(0.8)

# Play background music (-1 makes it loop indefinitely)
pygame.mixer.music.play(-1)


# --- Sprite Groups ---
# Purpose: Organize different types of sprites.
# 'all_sprites': Used for efficiently updating and drawing ALL sprites at once.
# Specific groups ('collectibles', 'obstacles'): Used for collision detection.
all_sprites = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# --- Create Player ---
player = Player()
all_sprites.add(player) # Add player to the drawing/updating group

# --- Create Collectibles ---
for _ in range(10): # Create 10 collectible items
    c = Collectible()
    all_sprites.add(c)     # Add to the drawing/updating group
    collectibles.add(c)  # Also add to the specific 'collectibles' group

# --- Create Obstacles ---
for _ in range(5): # Create 5 obstacles
    o = Obstacle()
    all_sprites.add(o)    # Add to the drawing/updating group
    obstacles.add(o)      # Also add to the specific 'obstacles' group

# --- Game Variables ---
score = 0

'''-------------------------CUSTOM FUNCTIONS----------------------------'''

def check_collisions(player_sprite, collectible_group, obstacle_group):
    """
    Checks for collisions between the player and other sprite groups.
    Handles score updates and playing sounds.
    Returns the updated score.
    """
    global score # Access the global score variable

    # --- Check for collisions with Collectibles ---
    # pygame.sprite.spritecollide(sprite, group, dokill)
    #   sprite: The single sprite to check.
    #   group: The group of sprites to check against.
    #   dokill (boolean): If True, sprites in 'group' that collide are automatically removed
    #                     from ALL groups they belong to.
    # Returns a list of sprites from 'group' that collided with 'sprite'.
    collected_items = pygame.sprite.spritecollide(player_sprite, collectible_group, True)

    if collected_items: # If the list is not empty (a collision occurred)
        score += len(collected_items) # Increase score by the number of items collected
        print(f"Collected! Score: {score}") # Debug print
        collect_sound.play() # Play the collection sound effect

    # --- Check for collisions with Obstacles ---
    hit_obstacles = pygame.sprite.spritecollide(player_sprite, obstacle_group, True) # Remove obstacle on hit

    if hit_obstacles:
        print("Hit an obstacle!") # Debug print
        # Potential actions: decrease score, lose a life, end game, etc.
        # For now, just play a sound and remove the obstacle (handled by dokill=True).
        hit_sound.play()

    return score # Return the potentially updated score


def draw_text(surface, text, font, color, x, y):
    """Helper function to render and draw text on a surface."""
    # Assumes font was loaded successfully in setup
    text_surface = font.render(text, True, color) # Render text (antialias=True)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


'''----------------------------------LOOP-------------------------------'''
running = True
while running:
    # --- Handling input (EVENTS) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit the loop
        # Add other event handling here if needed (e.g., specific key presses for actions)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         # Do something on spacebar press
        #         pass

    # --- Game Logic Updates ---
    # Call the update() method on ALL sprites in the 'all_sprites' group.
    # This moves the player based on keys and moves/bounces the obstacles.
    all_sprites.update()

    # --- Collision Detection ---
    # Call our custom function to check for player collisions
    score = check_collisions(player, collectibles, obstacles)

    # --- Replenish Sprites (Optional - keeps the game going) ---
    # If too few collectibles, add more
    while len(collectibles) < 5: # Maintain at least 5 collectibles
        c = Collectible()
        all_sprites.add(c)
        collectibles.add(c)

    # If too few obstacles, add more
    while len(obstacles) < 3: # Maintain at least 3 obstacles
         o = Obstacle()
         all_sprites.add(o)
         obstacles.add(o)


    # --- Drawing ---
    # Fill the screen with a background color (draw this first!)
    screen.fill((40, 40, 60)) # A dark blue-grey background

    # Draw ALL sprites in the 'all_sprites' group onto the screen surface.
    # Pygame handles drawing each sprite's 'image' at its 'rect' position.
    all_sprites.draw(screen)

    # Draw the score text
    draw_text(screen, f"Score: {score}", game_font, YELLOW, 10, 10) # Top-left corner

    # --- Updating the window ---
    pygame.display.flip() # Make everything drawn visible

    # --- Frame Rate Control ---
    # Ensure the loop runs at a maximum of 60 frames per second
    clock.tick(60)

'''----------------------------------CLEANUP---------------------------'''
pygame.quit() # Uninitialize Pygame modules
sys.exit()    # Exit the program
